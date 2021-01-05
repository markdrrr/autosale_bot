import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
DATABASE = str(os.getenv("DATABASE"))
admins = [
    os.getenv("ADMIN_ID"),
]

QIWI_TOKEN = os.getenv("QIWI_TOKEN")
WALLET_QIWI = os.getenv("WALLET_QIWI")
QIWI_PUBKEY = os.getenv("QIWI_PUBKEY")

ip = os.getenv("ip")
POSTGRES_URL = F'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
