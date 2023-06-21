from Pragyanx.config import *
from pyrogram import Client

"""Starting all clients"""
   
if  ":" in CLIENT:
   Pragyan = Client('PragyanX', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT, plugins=dict(root="PragyanX.modules.for_bot"))
   print("PragyanX - [INFO]: Bot token 1 Found")
else:
   Pragyan = Client('CLIENT', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT, plugins=dict(root="PragyanX.modules.for_id"))
   print("PragyanX - [INFO]: Client 1 Found")


if CLIENT2:
   if ":" in CLIENT2:
      Pragyan2 = Client('PragyanX2', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT2, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 2 Found")
   else:
      Pragyan2 = Client('CLIENT2', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT2, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 2 Found")
else:
   Pragyan2 = None
         
   
if CLIENT3:
   if ":" in CLIENT3:
     Pragyan3 = Client('PragyanX3', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT3, plugins=dict(root="PragyanX.modules.for_bot"))
     print("PragyanX - [INFO]: Bot token 3 Found")
   else:
     Pragyan3 = Client('CLIENT3', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT3, plugins=dict(root="PragyanX.modules.for_id"))
     print("PragyanX - [INFO]: Client 3 Found")
else:
   Pragyan3 = None
         

if CLIENT4:
   if ":" in CLIENT4:
      Pragyan4 = Client('PragyanX4', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT4, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 4 Found")
   else:
      Pragyan4 = Client('CLIENT4', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT4, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 4 Found")
else:
   Pragyan4 = None
         

if CLIENT5:
   if ":" in CLIENT5:
      Pragyan5 = Client('PragyanX5', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT5, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 5 Found")
   else:
      Pragyan5 = Client('CLIENT5', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT5, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 5 Found")
else:
   Pragyan5 = None
           

if CLIENT6:
   if ":" in CLIENT6:
      Pragyan6 = Client('PragyanX6', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT6, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 6 Found")
   else:
      Pragyan6 = Client('CLIENT6', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT6, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 6 Found")
else:
   Pragyan6 = None
             

if CLIENT7:
   if ":" in CLIENT7:
      Pragyan7 = Client('PragyanX7', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT7, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 7 Found")
   else:
      Pragyan7 = Client('CLIENT7', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT7, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 7 Found")
else:
   Pragyan7 = None
             

if CLIENT8:
    if ":" in CLIENT8:
      Pragyan8 = Client('PragyanX8', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT8, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 8 Found")
    else:
      Pragyan8 = Client('CLIENT8', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT8, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 8 Found")
else:
   Pragyan8 = None
             

if CLIENT9:
   if ":" in CLIENT9:
      Pragyan9 = Client('PragyanX9', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT9, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 9 Found")
   else:
      Pragyan9 = Client('CLIENT9', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT9, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 9 Found")
else:
   Pragyan9 = None
             

if CLIENT10:
   if ":" in CLIENT10:
      Pragyan10 = Client('PragyanX10', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT10, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 10 Found")
   else:
      Pragyan10 = Client('CLIENT10', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT10, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 10 Found")
else:
   Pragyan10 = None             

if CLIENT11:
   if ":" in CLIENT11:
      Pragyan11 = Client('PragyanX11', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT11, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 11 Found")
   else:
      Pragyan11 = Client('CLIENT11', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT11, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 11 Found")
else:
   Pragyan11 = None
             

if CLIENT12:
   if ":" in CLIENT12:
      Pragyan12 = Client('PragyanX12', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT12, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 12 Found")
   else:
      Pragyan12 = Client('CLIENT12', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT12, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 12 Found")
else:
   Pragyan12 = None
             

if CLIENT13:
   if ":" in CLIENT13:
      Pragyan13 = Client('PragyanX13', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT13, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 13 Found")
   else:
      Pragyan13 = Client('CLIENT13', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT13, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 13 Found")
else:
      Pragyan13 = None
             

if CLIENT14:
   if ":" in CLIENT14:
      Pragyan14 = Client('PragyanX14', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT14, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 14 Found")
   else:
      Pragyan14 = Client('CLIENT14', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT14, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 14 Found")
else:
   Pragyan14 = None
             

if CLIENT15:
   if ":" in CLIENT15:
      Pragyan15 = Client('PragyanX15', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT15, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 15 Found")
   else:
      Pragyan15 = Client('CLIENT15', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT15, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 15 Found")
else:
   Pragyan15 = None
             

if CLIENT16:
   if ":" in CLIENT16:
      Pragyan16 = Client('PragyanX16', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT16, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 16 Found")
   else:
      Pragyan16 = Client('CLIENT16', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT16, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 16 Found")
else:
   Pragyan16 = None
             

if CLIENT17:
   if ":" in CLIENT17:
      Pragyan17 = Client('PragyanX17', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT17, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 17 Found")
   else:
      Pragyan17 = Client('CLIENT17', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT17, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 17 Found")
else:
   Pragyan17 = None
             

if CLIENT18:
   if ":" in CLIENT18:
      Pragyan18 = Client('PragyanX18', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT18, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 18 Found")
   else:
      Pragyan18 = Client('CLIENT18', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT18, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 18 Found")
else:
   Pragyan18 = None
           

if CLIENT19:
   if ":" in CLIENT19:
      Pragyan19 = Client('PragyanX19', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT19, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 19 Found")
   else:
      Pragyan19 = Client('CLIENT19', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT19, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 19 Found")
else:
   Pragyan19 = None
        

if CLIENT20:
   if ":" in CLIENT20:
      Pragyan20 = Client('PragyanX20', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT20, plugins=dict(root="PragyanX.modules.for_bot"))
      print("PragyanX - [INFO]: Bot token 20 Found")
   else:
      Pragyan20 = Client('CLIENT20', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT20, plugins=dict(root="PragyanX.modules.for_id"))
      print("PragyanX - [INFO]: Client 20 Found")
else:
   Pragyan20 = None

