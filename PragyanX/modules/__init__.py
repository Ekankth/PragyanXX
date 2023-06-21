from PragyanX.config import *
from PragyanX.core.version import __version__
from PragyanX import sudoser, RiZoeL 
from PragyanX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "PragyanX"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph//file/08445817174872b47cef8.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "PragyanX - by RiZoeLX"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **Master:** {owner_mention}
➠ **Python Version:** `{platform.python_version()}`
➠ **PragyanX Version:** `{__version__}`
➠ **Pyrogram Version:** `{pyro_vr}`
➠ **pyPragyanX Version:** `{pip_vr}`
➠ **Channel:** @RiZoeLX
━───────╮•╭───────━
➠ **Source Code:** [•Repo•](https://github.com/PragyanIITIAN/PragyanX)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from PragyanX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
