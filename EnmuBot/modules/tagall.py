import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from EnmuBot import telethn
from EnmuBot.events import register as tomori


@tomori(pattern="^/tagall|@all|/all ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Hellow ~ Im Enmu And I Call All of you to Summon In My World Of Dreams Immediately"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](https://t.me/{x.username})"
    await event.reply(mentions)
    await event.delete()


@tomori(pattern="^/users|@users|/tagusers ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Users : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](https://t.me/{x.username})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__mod_name__ = "Tagger"
__help__ = """
──「 Mention all func 」──

Enmu Can Be a Mention Bot for your group.

Only admins can tag all.  here is a list of commands

❂ /tagall or @all (reply to message or add another message) To mention all members in your group, without exception.
❂ /cancel for canceling the mention-all.
"""
