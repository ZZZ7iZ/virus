from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "50000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/d7f33299ed8c60ad82721.mp4")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3dd59102dc041f36e28d2.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/H_M_Dr")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/IIIlIIv")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5012406813").split()))


FAILED = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
