from pyrogram import filters
from pyrogram.types import *

from EnmuBot import pbot as bot



@bot.on_message(filters.command("whisper"))
async def whisper(_, message):
      global name, text, user
      name = message.from_user.first_name
      mention = message.from_user.mention
      if len(message.command) <2:
          return await message.reply("𝗚𝗶𝘃𝗲 𝗨𝘀𝗲𝗿𝗜𝗱")
      elif len(message.command) <3:
          return await message.reply("𝗚𝗶𝘃𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲")
      user_id = message.text.split(" ")[1]
      text = message.text.split(" ")[2]
      user = await bot.get_users(user_id)
      
             
      button = [[ InlineKeyboardButton(text="Open Whisper Message!", callback_data="whisper_data")]]
      whisper = f"""** 🕵 New Whisper Message!**
      
**From User:** {mention}
**To UserID:** {user.mention}

**Note: this Message only can open the: To UserID
Your Not Allow To See Other Personal Messages!**
"""
      await bot.send_message(message.chat.id,whisper,
               reply_markup=InlineKeyboardMarkup(button))
      bot_stats = await bot.get_chat_member(message.chat.id, "self")
      if bot_stats.privileges:
            return await message.delete()

@bot.on_callback_query(filters.regex("whisper_data"))
async def whisperdata(_, query):
       if query.from_user.id == user.id:
          WHISPER = f"""{user.first_name}, here your message from {name} Message: {text}"""
          await query.answer(WHISPER, show_alert=True)
       else:
           await query.answer("**YOUR NOT ALLOWED**")
