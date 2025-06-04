#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20314087"))
API_HASH = environ.get("API_HASH", "bb5b852b38f4eae21e83be783348a41c")
BOT_TOKEN = environ.get("BOT_TOKEN", "AAHLfgoWwE3IBHMVQ_WyfouR0Nyaw8S0Phg")
OWNER = int(environ.get("OWNER", "5405432233"))
CREDIT = "𝄟⃝‌🐬🇳suraj🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5405432233').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
