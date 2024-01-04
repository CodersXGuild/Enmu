import html
import re
import os
import requests
import datetime
import platform
import time

from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
from pyrogram.types import CallbackQuery
from platform import python_version
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events
from pyrogram import Client, filters
from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update, MessageEntity, __version__ as ptbver, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_html
    
from EnmuBot import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    INFOPIC,
    dispatcher,
    StartTime,
    SUPPORT_CHAT,
)
from EnmuBot.__main__ import STATS, TOKEN, USER_INFO
from EnmuBot.modules.sql import SESSION
import EnmuBot.modules.sql.userinfo_sql as sql
from EnmuBot.modules.disable import DisableAbleCommandHandler
from EnmuBot.modules.sql.global_bans_sql import is_user_gbanned
from EnmuBot.modules.sql.users_sql import get_user_num_chats
from EnmuBot.modules.helper_funcs.chat_status import sudo_plus
from EnmuBot.modules.helper_funcs.extraction import extract_user
from EnmuBot.modules.helper_funcs.decorators import enmucallback as ENMUCALLBACK
from EnmuBot import telethn

app = Client("deletekrde")

ENMU_IMG = 'https://telegra.ph/file/efc8c427511970fff58f6.jpg'

def get_id(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat
    msg = update.effective_message
    user_id = extract_user(msg, args)

    if user_id:

        if msg.reply_to_message and msg.reply_to_message.forward_from:

            user1 = message.reply_to_message.from_user
            user2 = message.reply_to_message.forward_from

            msg.reply_text(
                f"<b>ID:</b>\n"
                f"• {html.escape(user2.first_name)} - <code>{user2.id}</code>.\n"
                f"• {html.escape(user1.first_name)} - <code>{user1.id}</code>.",
                parse_mode=ParseMode.HTML,
            )

        else:

            user = bot.get_chat(user_id)
            msg.reply_text(
                f"{html.escape(user.first_name)}'s id is <code>{user.id}</code>.",
                parse_mode=ParseMode.HTML,
            )

    elif chat.type == "private":
        msg.reply_text(
            f"Your id is <code>{chat.id}</code>.",
            parse_mode=ParseMode.HTML,
        )

    else:
        msg.reply_text(
            f"This group's id is <code>{chat.id}</code>.",
            parse_mode=ParseMode.HTML,
        )


def gifid(update: Update, context: CallbackContext):
    msg = update.effective_message
    if msg.reply_to_message and msg.reply_to_message.animation:
        update.effective_message.reply_text(
            f"Gif ID:\n<code>{msg.reply_to_message.animation.file_id}</code>",
            parse_mode=ParseMode.HTML,
        )
    else:
        update.effective_message.reply_text("Please reply to a gif to get its ID.")


def info(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat
    user_id = extract_user(update.effective_message, args)

    if user_id:
        user = bot.get_chat(user_id)

    elif not message.reply_to_message and not args:
        user = message.from_user

    elif not message.reply_to_message and (
        not args
        or (
            len(args) >= 1
            and not args[0].startswith("@")
            and not args[0].isdigit()
            and not message.parse_entities([MessageEntity.TEXT_MENTION])
        )
    ):
        message.reply_text("I can't extract a user from this.")
        return

    else:
        return

    rep = message.reply_text("<code>Searching In Database.....</code>", parse_mode=ParseMode.HTML)

    text = (
        f"╔═━「<b> Search Result:</b> 」\n\n"
        f"ID: <code>{user.id}</code>\n"
        f"First Name: {html.escape(user.first_name)}"
    )

    if user.last_name:
        text += f"\nLast Name: {html.escape(user.last_name)}"

    disaster_level_present = False

    if user.id == OWNER_ID:
        text += "\n\nThe Disaster Of This Person Is Dᴇᴍᴏɴ Kɪɴɢ."
        disaster_level_present = True
    elif user.id in DEV_USERS:
        text += "\n\nThis user is member of ᴜᴘᴘᴇʀ ᴍᴏᴏɴs."
        disaster_level_present = True
    elif user.id in DRAGONS:
        text += "\n\nThe Disaster Of This Person Is ʟᴏᴡᴇʀ ᴍᴏᴏɴs."
        disaster_level_present = True
    elif user.id in DEMONS:
        text += "\n\nThe Disaster Of This Person Is Xʟᴏᴡᴇʀᴍᴏᴏɴs."
        disaster_level_present = True
    elif user.id in TIGERS:
        text += "\n\nThe Disaster Of This Person Is ᴅᴇᴍᴏɴs."
        disaster_level_present = True
    elif user.id in WOLVES:
        text += "\n\nThe Disaster Of This Person Is Xᴅᴇᴍᴏɴs."
        disaster_level_present = True

    try:
        user_member = chat.get_member(user.id)
        if user_member.status == "administrator":
            result = requests.post(
                f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={chat.id}&user_id={user.id}",
            )
            result = result.json()["result"]
            if "custom_title" in result.keys():
                custom_title = result["custom_title"]
                text += f"\n\nTitle:\n<b>{custom_title}</b>"
    except BadRequest:
        pass

    for mod in USER_INFO:
        try:
            mod_info = mod.__user_info__(user.id)
        except TypeError:
            mod_info = mod.__user_info__(user.id, chat.id)
        if mod_info:
            text += "\n\n" + mod_info

    if INFOPIC:
        try:
            username=update.effective_user.username
            profile = context.bot.get_user_profile_photos(user.id).photos[0][-1]
            context.bot.sendChatAction(chat.id, "upload_photo")
            context.bot.send_photo(
            chat.id,
            photo=profile,
                caption=(text),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Support", url="https://t.me/TitanHeadQuaters"),
                            InlineKeyboardButton(
                                "User", url=f"tg://user?id={user.id}"),
                        ],
                        [
                            InlineKeyboardButton("❌", callback_data="demlemte_btn")
                        ],
                    ]    
                ),
                parse_mode=ParseMode.HTML,
            )

           
        # Incase user don't have profile pic, send normal text
        except IndexError:
            message.reply_text(
                text, 
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Support", url="https://t.me/TitanHeadQuaters"),
                            InlineKeyboardButton(
                                "User", url=f"tg://user?id={user.id}"),
                        ],
                        [
                            InlineKeyboardButton("❌", callback_data="demlemte_btn")
                        ],
                    ]
                ),
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True
            )

    else:
        message.reply_text(
            text, parse_mode=ParseMode.HTML,
        )


    rep.delete()


def demlemte_btn(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    chat = update.effective_chat
    user = update.effective_user
    query.message.delete()
    bot.answer_callback_query(query.id, text="Deleted!")
    return ""

    
def about_me(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    user_id = extract_user(message, args)

    user = bot.get_chat(user_id) if user_id else message.from_user
    info = sql.get_user_me_info(user.id)

    if info:
        update.effective_message.reply_text(
            f"*{user.first_name}*:\n{escape_markdown(info)}",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
    elif message.reply_to_message:
        username = message.reply_to_message.from_user.first_name
        update.effective_message.reply_text(
            f"{username} hasn't set an info message about themselves yet!",
        )
    else:
        update.effective_message.reply_text("There isnt one, use /setme to set one.")


def set_about_me(update: Update, context: CallbackContext):
    message = update.effective_message
    user_id = message.from_user.id
    if user_id in [777000, 1087968824]:
        message.reply_text("Error! Unauthorized")
        return
    bot = context.bot
    if message.reply_to_message:
        repl_message = message.reply_to_message
        repl_user_id = repl_message.from_user.id
        if repl_user_id in [bot.id, 777000, 1087968824] and (user_id in DEV_USERS):
            user_id = repl_user_id
    text = message.text
    info = text.split(None, 1)
    if len(info) == 2:
        if len(info[1]) < MAX_MESSAGE_LENGTH // 4:
            sql.set_user_me_info(user_id, info[1])
            if user_id in [777000, 1087968824]:
                message.reply_text("Information Updated!")
            elif user_id == bot.id:
                message.reply_text("I have updated my info with the one you provided!")
            else:
                message.reply_text("Information Updated!")
        else:
            message.reply_text(
                "The info needs to be under {} characters! You have {}.".format(
                    MAX_MESSAGE_LENGTH // 4,
                    len(info[1]),
                ),
            )

@sudo_plus
def stats(update: Update, context: CallbackContext):
    stats = "<b>╒═══「 Bot Statistics 」</b>\n\n" + "\n".join(
        [mod.__stats__() for mod in STATS]
    )
    result = re.sub(r"(\d+)", r"<code>\1</code>", stats)
    result += "\n\n<b>╘══「 By <a href='tg://user?id=2005266280'>Prime Flame</a> 」</b>"
    update.effective_message.reply_photo(
        ENMU_IMG, result, parse_mode=ParseMode.HTML
    )
def about_bio(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message

    user_id = extract_user(message, args)
    user = bot.get_chat(user_id) if user_id else message.from_user
    info = sql.get_user_bio(user.id)

    if info:
        update.effective_message.reply_text(
            "*{}*:\n{}".format(user.first_name, escape_markdown(info)),
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
    elif message.reply_to_message:
        username = user.first_name
        update.effective_message.reply_text(
            f"{username} hasn't had a message set about themselves yet!\nSet one using /setbio",
        )
    else:
        update.effective_message.reply_text(
            "You haven't had a bio set about yourself yet!",
        )


def set_about_bio(update: Update, context: CallbackContext):
    message = update.effective_message
    sender_id = update.effective_user.id
    bot = context.bot

    if message.reply_to_message:
        repl_message = message.reply_to_message
        user_id = repl_message.from_user.id

        if user_id == message.from_user.id:
            message.reply_text(
                "Ha, you can't set your own bio! You're at the mercy of others here...",
            )
            return

        if user_id in [777000, 1087968824] and sender_id not in DEV_USERS:
            message.reply_text("You are not authorised")
            return

        if user_id == bot.id and sender_id not in DEV_USERS:
            message.reply_text(
                "I Trust only My Master to set my bio.",
            )
            return

        text = message.text
        bio = text.split(
            None, 1,
        )  # use python's maxsplit to only remove the cmd, hence keeping newlines.

        if len(bio) == 2:
            if len(bio[1]) < MAX_MESSAGE_LENGTH // 4:
                sql.set_user_bio(user_id, bio[1])
                message.reply_text(
                    "Updated {}'s bio!".format(repl_message.from_user.first_name),
                )
            else:
                message.reply_text(
                    "Bio needs to be under {} characters! You tried to set {}.".format(
                        MAX_MESSAGE_LENGTH // 4, len(bio[1]),
                    ),
                )
    else:
        message.reply_text("Reply to someone to set their bio!")

def __user_info__(user_id):
    bio = html.escape(sql.get_user_bio(user_id) or "")
    me = html.escape(sql.get_user_me_info(user_id) or "")
        
__help__ = """
──「 Info 」──
    *ID:*
     /id*:* get the current group id. If used by replying to a message, gets that user's id.
     /gifid*:* reply to a gif to me to tell you its file ID.
    
    *Self addded information:* 
     /setme <text>*:* will set your info
     /me*:* will get your or another user's info.
    
    *Information others add on you:* 
     /bio*:* will get your or another user's bio. This cannot be set by yourself.
     /setbio <text>*:* while replying, will save another user's bio 
    
    *Overall Information about you:*
     /info*:* get information about a user. 
    
    *Uinfo*
     /uinfo*:* use this and check yourself.
    
    *json Detailed info:*
     /json*:* Get Detailed info about any message.
    
    """

SET_BIO_HANDLER = DisableAbleCommandHandler("setbio", set_about_bio, run_async=True)
GET_BIO_HANDLER = DisableAbleCommandHandler("bio", about_bio, run_async=True)
STATS_HANDLER = CommandHandler(["stats", "statistics"], stats, run_async=True)
ID_HANDLER = DisableAbleCommandHandler("id", get_id, run_async=True)
GIFID_HANDLER = DisableAbleCommandHandler("gifid", gifid, run_async=True)
INFO_HANDLER = DisableAbleCommandHandler("info", info, run_async=True)
DELETE_BUTTON_HANDLER = CallbackQueryHandler(demlemte_btn, pattern=r"demlemte_")
SET_ABOUT_HANDLER = DisableAbleCommandHandler("setme", set_about_me, run_async=True)
GET_ABOUT_HANDLER = DisableAbleCommandHandler("me", about_me, run_async=True)

dispatcher.add_handler(STATS_HANDLER)
dispatcher.add_handler(ID_HANDLER)
dispatcher.add_handler(GIFID_HANDLER)
dispatcher.add_handler(INFO_HANDLER)
dispatcher.add_handler(SET_BIO_HANDLER)
dispatcher.add_handler(GET_BIO_HANDLER)
dispatcher.add_handler(SET_ABOUT_HANDLER)
dispatcher.add_handler(GET_ABOUT_HANDLER)
dispatcher.add_handler(DELETE_BUTTON_HANDLER)

__mod_name__ = "Info"
__command_list__ = ["setbio", "bio", "setme", "me", "info"]
__handlers__ = [
    ID_HANDLER,
    GIFID_HANDLER,
    INFO_HANDLER,
    SET_BIO_HANDLER,
    GET_BIO_HANDLER,
    SET_ABOUT_HANDLER,
    GET_ABOUT_HANDLER,
    STATS_HANDLER,
    DELETE_BUTTON_HANDLER,
]
