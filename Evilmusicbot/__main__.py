
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Evilmusicbot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from Evilmusicbot import app, LOGGER
from Evilmusicbot.mrdarkprince import ignore_blacklisted_users
from Evilmusicbot.sql.chat_sql import add_chat_to_db

start_text = """
       f"""🙃 Hi {message.from_user.first_name}!

✨ I am êvilẞø† Music Player. 

🥳 I can play music in your Telegram Group's Voice Chat😉

⚜️ Use these buttons below to know more. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📔 Source Code 📔", url="https://github.com/jattpawan/evilbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group 💬", url="https://t.me/BLAC_USERBOT_GROUP"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel 📣", url="https://t.me/BLAC_USERBOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

