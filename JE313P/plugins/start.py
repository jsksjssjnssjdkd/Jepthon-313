from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """**━━━━━━━━━━━━
اهـلا يـبـنـي.؟ {message.from_user.mention()} !
مـرحبآ بـك انــا بــوت اقـوم بــتـشـغـيـل الاغــانــي فـي الـمـڪـالـمـه الـصـوتـية .🤔❤؟
يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه
 +اضفني الى مجموعتك وارفعني رول بشڪل مع ڪامل الصلاحيات
 البوت يشتغل بالاوامر عربي وانجليزي
 لانضمام الحساب المساعد لتشغيل البوت اكتب انضم


  لمعرفة استخدامي بشڪل صحيح اضغط علي زر الاوامر. 🤔𝑫𝑬𝑽 [𝑾𝑶𝑹𝑳𝑫 𝑴𝑼𝑺𝑰𝑪 💗ˣ](t.me/WORLD_MUSIC_F)
━━━━━━━━━━━━━━━━━━**"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضغط هنا لأضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("المطور", "https://t.me/(Config_Dev")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضغط هنا لاضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("المطور", "https://t.me/(Config_Dev")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return
