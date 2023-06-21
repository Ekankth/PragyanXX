# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL

import os, sys, asyncio
from random import choice
from .. import (Owner, handler, Sudos, LOGS_CHANNEL, DATABASE_URL)
from pyrogram import Client, filters
from pyrogram.types import Message

from PragyanX.data import raid_usage, raids
from PragyanX import Devs, res_grps
from PragyanX.functions import user_only, start_raid

from PragyanX.database import raid_db

@Client.on_message(filters.user(Sudos) & filters.command(["raid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["raid"], prefixes=handler))
async def raid(PragyanX: Client, e: Message):
      """ Start Raid """
      usage = raid_usage.raid
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        counts = int(Rizoel[0])
        if not counts:
          await e.reply_text(f"Gime raid Counts or use `{handler}.uraid` for Unlimited raid!")
          return
        hm = Rizoel[1]
        if not hm:
          await e.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await PragyanX.get_users(Rizoel[1])
        except:
           await e.reply_text("**Error:** User not found!")
           return
      elif e.reply_to_message:
        counts = int(Rizoel[0])
        try:
           user = await PragyanX.get_users(e.reply_to_message.from_user.id)
        except:
           user = e.reply_to_message.from_user 
      else:
        await e.reply_text(usage.format(handler))
        return

      if int(user.id) == Owner:
         await e.reply_text("This guy is Owner Of these Bots.")
         return
      if int(user.id) in Sudos:
         if e.from_user.id != Owner:
           await e.reply_text("This guy is a sudo users.")
           return

      await start_raid(PragyanX, e, counts, user)

      if LOGS_CHANNEL:
         try:
            await PragyanX.send_message(LOGS_CHANNEL, f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}")
         except Exception as a:
            print(a)
            pass


RUSERs = []

@Client.on_message(filters.user(Sudos) & filters.command(["rraid", "replyraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["rraid", "replyraid"], prefixes=handler))
async def rraid(PragyanX: Client, e: Message):
      global RUSERs
      user = await user_only(PragyanX, e, Owner, Sudos)

      if DATABASE_URL:
          check = raid_db.check(user.id)
          if check:
             await e.reply_text("User already in Raid list!")
             return
          raid_db.add_user(user.id)
      else:
          if int(user.id) in RUSERs:
             await e.reply_text("User already in Raid list!")
             return
          RUSERs.append(user.id)                
      mention = user.mention
      await e.reply_text(f"Reply Raid Activated On User {mention}")
            
      if LOGS_CHANNEL:
         try:
            await PragyanX.send_message(LOGS_CHANNEL, f"Activated Reply Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.user(Sudos) & filters.command(["draid", "dreplyraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["draid", "dreplyraid"], prefixes=handler))
async def draid(PragyanX: Client, e: Message):
      global RUSERs
      user = await user_only(PragyanX, e, Owner, Sudos)

      if DATABASE_URL:
         check = raid_db.check(user.id)
         if not check:
             await e.reply_text("User not in Raid list!")
             return 
         raid_db.rm_user(user.id)
      else:
         if int(user.id) not in RUSERs:
           await e.reply_text("User not in Raid list!")
           return
         RUSERs.remove(user.id)
      mention = user.mention
      await e.reply_text(f"Reply Raid Activated Successfully On User {mention}")
      
      if LOGS_CHANNEL:
         try:
            await PragyanX.send_message(LOGS_CHANNEL, f" Deactivated Reply Raid By User: {e.from_user.id} \n\n User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.all)
async def watcher(_, msg: Message):
    global RUSERs
    if int(msg.chat.id) in res_grps:
       return
    if DATABASE_URL:
       check = raid_db.check(msg.from_user.id)
       if check:
         await msg.reply_text(choice(raids.replyraids))
    else:
       if int(msg.from_user.id) in RUSERs:
         await msg.reply_text(choice(raids.replyraids))       

@Client.on_message(filters.user(Sudos) & filters.command(["rlist", "raidlist"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["rlist", "raidlist"], prefixes=handler))
async def raidlist(PragyanX: Client, message: Message):
    global RUSERs
    _reply = "**Raid users list - PragyanX** \n\n"
    if DATABASE_URL:
       data = raid_db.get_all_raiders()
       if len(data) > 0:
          for x in data:
             try:
                user = await PragyanX.get_users(x.user_id)
                _reply += f" × {user.mention} \n"
             except:
                _reply += f" × [{x.user_id}](tg://user?id={x.user_id}) \n"
       else:
          await message.reply_text("Not yet!")
          return
    else:
       if len(RUSERs) > 0:
          for x in RUSERs:
             try:
                user = await PragyanX.get_users(x)
                _reply += f" × {user.mention} \n"
             except:
                _reply += f" × [{x}](tg://user?id={x}) \n"
       else:
          await message.reply_text("Not yet!")
          return
    await message.reply_text(_reply)
