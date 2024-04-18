import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hikari.events import register
from Hikari import telethn as tbot


PHOTO = "https://mallucampaign.in/images/img_1712864065.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), **sᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴍᴀɴᴀɢᴇ ʙᴏᴛ\n\n"
  TEXT += "**ᴀᴋᴜ sᴇʟᴀʟᴜ ʜɪᴅᴜᴘ ᴅᴀɴ ʙᴇᴋᴇʀᴊᴀ** \n\n"
  TEXT += f"**ᴏᴡɴᴇʀ : [ᴏᴡɴᴇʀ](https://t.me/Usern4meDoesNotExist404)** \n\n"
  TEXT += f"**ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/ManagementTele_Bot?start=help"), Button.url("ᴅᴏɴᴀsɪ ​", "https://t.me/MusicStreamSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
