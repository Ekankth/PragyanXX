""" 
     PragyanX - Telegram Bots
     © PragyanX 2022-2023
"""


from .. import Owner, handler, Sudos, DATABASE_URL
from Pragyanx.database import gban_db
import random 

from pyrogram import Client, filters
from pyrogram.types import Message

from PragyanX import Devs
from PragyanX.functions import start_gban, start_ungban, start_gpromote, start_gdemote, user_reason, user_only, get_user


@Client.on_message(filters.user(Owner) & filters.command(["gban", "globalban"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["gban", "globalban"], prefixes=handler))
async def gban_(PragyanX: Client, message: Message):
    chat = message.chat
    user, reason = await user_reason(PragyanX, message, Owner, Sudos)
    if not reason:
       reason = "personal!"
    if DATABASE_URL:
       check = gban_db.check(user.id)
       if check:
         await message.reply_text(f"{user.mention} already in GBAN list!")
         return
       gban_db.gban(user.id, reason)
       await start_gban(PragyanX, message, user, reason)       
    else:
       await message.reply_text("Error! filled `DATABASE_URL`")


@Client.on_message(filters.user(Owner) & filters.command(["ungban", "unglobalban"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["ungban", "unglobalban"], prefixes=handler))
async def ungban_(PragyanX: Client, message: Message):
    chat = message.chat
    user = await user_only(PragyanX, message, Owner, Sudos)
    if DATABASE_URL:
       check = gban_db.check(user.id)
       if not check:
         await message.reply_text(f"{user.mention} not in GBAN list!")
         return
       gban_db.ungban(user.id)
       await start_ungban(PragyanX, message, user)
    else:
       await message.reply_text("Error! filled `DATABASE_URL`")
       return

@Client.on_message(filters.new_chat_members)
async def gban_watcher(PragyanX: Client, message: Message):
   user = message.from_user
   chat = message.chat
   if DATABASE_URL:
      check = gban_db.check(user.id)
      if check:
         gban_msg = f"""
**Alert ⚠️**

Gbanned user joined!

user: {user.mention}
reason: {check.reason}
         """
         try:
           await PragyanX.ban_chat_member(chat.id, user.id)
         except Exception as error:
           print(str(error))
         await PragyanX.send_message(chat.id, gban_msg)

@Client.on_message(filters.user(Sudos) & filters.command(["gbanlist", "glist", "gbans"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["gbanlist", "glist", "gbans"], prefixes=handler))
async def glist(PragyanX: Client, message: Message):
    _reply = "**Gbanned users list - PragyanX** \n\n"
    if DATABASE_URL:
       data = gban_db.get_all_gbanned()
       if len(data) > 0:
          for x in data:
             try:
                user = await PragyanX.get_users(x.user_id)
                _reply += f" × {user.mention} \n"
             except:
               _reply += f" × [{x.user_id}](tg://user?id={x.user_id}) \n"
          await message.reply_text(_reply)
          return
       else:
          await message.reply_text("Not yet!")
          return
    await message.reply_text("Ah. You didn't filled `DATABASE_URL`")