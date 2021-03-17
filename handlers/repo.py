from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("repo")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**êvilẞø†:** if you want musicbot like me then click on repo button to get my repo and click on SESSION button for gernating session and click on heroku botton to deploy me🤍  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎 Developer 😎", url="https://t.me/MrC_VENOM"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❣Group❣", url="https://t.me/tvseriezzz"
                    ),
                    InlineKeyboardButton(
                        "💜 Channel 💜", url="https://t.me/TV_SERIES_ON"
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
    
@Client.on_message(
    filters.command("repo")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        "**êvilẞø†:** if you want musicbot like me then click on repo button to get my repo and click on SESSION button for gernating session and click on heroku botton to deploy me🤍  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 Developer 💙", url="https://t.me/MrC_VENOM"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❣ Group ❣", url="https://t.me/tvseriezzz"
                    ),
                    InlineKeyboardButton(
                        "💜 Channel 💜", url="https://t.me/TV_SERIES_ON"
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
