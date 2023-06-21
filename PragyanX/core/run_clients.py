
# Versions

from .clients import *
from PragyanX.config import *

from .version import __version__
from PragyanX import __version__ as pragyanx_vr
from pyrogram import __version__ as pyro_vr
import platform

from PragyanX.functions import start_PragyanX
from pyrogram import idle

def Run_PragyanX():
    if CLIENT:
       if ":" in CLIENT:
         start_pragyanX(Pragyan, "token")
       else:
         start_pragyanX(Pragyan, "session")

    if CLIENT2:
       if ":" in CLIENT2:
         start_pragyanX(Pragyan2, "token")
       else:
         start_pragyanX(Pragyan2, "session")
         
    if CLIENT3:
       if ":" in CLIENT3:
         start_pragyanX(Pragyan3, "token")
       else:
         start_pragyanX(Pragyan3, "session")
         
    if CLIENT4:
       if ":" in CLIENT4:
         start_pragyanX(Pragyan4, "token")
       else:
         start_pragyanX(Pragyan4, "session")
         
    if CLIENT5:
       if ":" in CLIENT5:
         start_pragyanX(Pragyan5, "token")
       else:
         start_pragyanX(Pragyan5, "session")
         
    if CLIENT6:
       if ":" in CLIENT6:
         start_pragyanX(Pragyan6, "token")
       else:
         start_pragyanX(Pragyan6, "session")
         
    if CLIENT7:
       if ":" in CLIENT7:
         start_pragyanX(Pragyan7, "token")
       else:
         start_pragyanX(Pragyan7, "session")
         
    if CLIENT8:
       if ":" in CLIENT8:
         start_pragyanX(Pragyan8, "token")
       else:
         start_pragyanX(Pragyan8, "session")
         
    if CLIENT9:
       if ":" in CLIENT9:
         start_pragyanX(Pragyan9, "token")
       else:
         start_pragyanX(Pragyan9, "session")

    if CLIENT10:
       if ":" in CLIENT10:
         start_pragyanX(Pragyan10, "token")
       else:
         start_pragyanX(Pragyan10, "session")
         
    if CLIENT11:
       if ":" in CLIENT11:
         start_pragyanX(Pragyan11, "token")
       else:
         start_pragyanX(Pragyan11, "session")
         
    if CLIENT12:
       if ":" in CLIENT12:
         start_pragyanX(Pragyan12, "token")
       else:
         start_pragyanX(Pragyan12, "session")
         
    if CLIENT13:
       if ":" in CLIENT13:
         start_pragyanX(Pragyan13, "token")
       else:
         start_pragyanX(Pragyan13, "session")
         
    if CLIENT14:
       if ":" in CLIENT14:
         start_pragyanX(Pragyan14, "token")
       else:
         start_pragyanX(Pragyan14, "session")
         
    if CLIENT15:
       if ":" in CLIENT15:
         start_pragyanX(Pragyan15, "token")
       else:
         start_pragyanX(Pragyan15, "session")
         
    if CLIENT16:
       if ":" in CLIENT16:
         start_pragyanX(Pragyan16, "token")
       else:
         start_pragyanX(Pragyan16, "session")
         
    if CLIENT17:
       if ":" in CLIENT17:
         start_pragyanX(Pragyan17, "token")
       else:
         start_pragyanX(Pragyan17, "session")
         
    if CLIENT18:
       if ":" in CLIENT18:
         start_pragyanX(Pragyan18, "token")
       else:
         start_pragyanX(Pragyan18, "session")
         
    if CLIENT19:
       if ":" in CLIENT19:
         start_pragyanX(Pragyan19, "token")
       else:
         start_pragyanX(Pragyan19, "session")

    if CLIENT20:
       if ":" in CLIENT20:
         start_pragyanX(Pragyan20, "token")
       else:
         start_pragyanX(Pragyan20, "session")
    
    print(f"PragyanX - [INFO]: Python Version - {platform.python_version()}")
    print(f"PragyanX - [INFO]: PragyanX Version - {__version__}")
    print(f"PragyanX - [INFO]: pyPragyanX Version - {pypragyanx_vr}")
    print(f"PragyanX - [INFO]: Pyrogram Version - {pyro_vr}")
    print(""" \n\n
     ╒═══════════════════════════╕
      Your PragyanX has been Deployed!!
      Visit @PragyanIITIAN for updates!
     ╘═══════════════════════════╛
    """)
    idle()
