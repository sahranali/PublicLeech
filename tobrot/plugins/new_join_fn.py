#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text(" Contact : https://t.me/iamomkarofficial", quote=True)
    channel_id = str(AUTH_CHANNEL)[4:]
    message_id = 99
    # display the /help message
    await message.reply_text(
        f"[Welcome !!](https://t.me/publicleechgroups)\n\nPlease read the Pinned Message\n\nReply these commands to Magnet link: \n`/leech@public_leechbot` \n`/leech@public_leechbot archive`\n`/ytdl@public_leechbot`\n`/savethumbnail@public_leechbot`\n`/clearthumbnail@public_leechbot`\n\n If still getting some problems try checking chat or tag and ask admins in chat.\n\n Check out our Channel for older uploads : @publicleechmovie ",
        quote=True
    )


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
