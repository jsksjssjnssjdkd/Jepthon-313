import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Ch_World_Music"
)

CAPTION = f"**سرعه الـبـنـج:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/Ch_World_music")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
