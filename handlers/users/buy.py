import datetime
from typing import Union

from aiogram import types

from keyboards.inline.menu_buy import categories_keyboard, items_keyboard, item_keyboard, menu_cd, buy_item, \
    confirm_keyboard
from loader import dp
from utils.db_api import product, staff, user, order


@dp.message_handler(text='Купить')
async def bot_start(message: types.Message):
    await list_categories(message)


@dp.callback_query_handler(text='cancel')
async def cancel(cl: types.CallbackQuery):
    print(cl)
    await cl.answer('Отменено')
    await cl.message.delete()
    bot = dp.bot
    await bot.send_message(cl.from_user.id, 'Отменено')


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, types.Message):
        await message.answer('<b>Выберете катигорию:</b>',
                             reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_items(callback: types.CallbackQuery, category, **kwargs):
    markup = await items_keyboard(category)
    await callback.message.edit_text('<b>Выберете товар:</b>',
                                     reply_markup=markup)


async def show_item(callback: types.CallbackQuery, category, item_id, **kwargs):
    markup = item_keyboard(category, item_id)
    item = await product.select_product(id=int(item_id))
    await callback.message.edit_text(f'<b>Выбран товар:</b> \n'
                                     f'{item.get("name")}\n'
                                     f'<b>Цена:</b> {item.get("price")}\n'
                                     f'<b>Выберете количество:</b>',
                                     reply_markup=markup)


async def confirm_item(callback: types.CallbackQuery, category, item_id, count):
    # првоеряем сколько выбрано и сколько в наличии
    item = await product.select_product(id=int(item_id))
    count_item_staff = await staff.get_count(product_id=item.get('id'), status=0)
    # условие если выбранное кличество привышает товаров в наличии
    if int(count) > int(count_item_staff):
        await callback.answer('Выберете меньше количества')
    else:
        markup = confirm_keyboard(category, item_id, count)
        item = await product.select_product(id=int(item_id))
        sum = int(item.get('price')) * int(count)
        await callback.message.edit_text(f'<b>Подтверждаете покупку?</b>\n'
                                         f'<b>Товар: {item.get("name")}\n</b>'
                                         f'<b>Количество:</b> {count}\n'
                                         f'<b>Сумма покупки:</b> {sum}',
                                         reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    print(callback_data)
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    item_id = callback_data.get('item_id')
    count = callback_data.get('count')

    levels = {
        '0': list_categories,
        '1': list_items,
        '2': show_item,
        '3': confirm_item
    }
    current_level_function = levels[current_level]
    await current_level_function(
        call,
        category=category,
        item_id=item_id,
        count=count
    )


@dp.callback_query_handler(buy_item.filter())
async def buying(call: types.CallbackQuery, callback_data: dict):
    item_id = int(callback_data.get('item_id'))
    count = int(callback_data.get('count'))
    item = await product.select_product(id=int(item_id))
    count_item_staff = await staff.get_count(product_id=item.get('id'), status=0)
    # условие если выбранное кличество привышает товаров в наличии
    if int(count) > int(count_item_staff):
        await call.answer('Выберете меньше количества')

    user_id = call.from_user.id
    item_user = await user.select_user(id=user_id)
    # сумма покупки
    purchase_amount = int(item.get('price')) * count

    # список staff для покупки
    product_id = item.get('id')
    list_staff = await staff.select_staff_limit(product_id=product_id, status=0, count=count)

    # проверяем что баланс не меньше суммы покупки
    if int(item_user.get('balance')) < purchase_amount:
        await call.answer('Недостаточно средств, попробуйте выбрать меньше')
    else:
        # списываем баланс
        new_balance = int(item_user.get('balance')) - purchase_amount
        await user.change_balance(item_user.get('id'), new_balance)

        # создаем заказ
        data = (datetime.datetime.now()).strftime("%d.%m.%Y %H:%M:%S")
        await order.add_order(user_id=user_id, product_id=product_id, data=data, sum=purchase_amount)
        item_order = await order.select_order(user_id=user_id, product_id=product_id, data=data)
        print('item_order', item_order)

        # изменяем статус покупки у объекта staff
        for el in list_staff:
            await staff.change_status(staff_id=int(el.get('id')), new_status=1)
            # создается объект staff_in_orders
            await staff.add_staff_in_orders(order_id=int(item_order.get('id')), staff_id=int(el.get('id')))

        # выгружаем staff в ответном сообщении
        text = str()
        for el in list_staff:
            text += f'Содержание товара: {el.get("staff")}'
        await call.message.edit_text(text)
