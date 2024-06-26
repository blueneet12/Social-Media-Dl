from pyrogram import filters, Client as Mbot
import bs4, requests
from bot import DUMP_GROUP
from apscheduler.schedulers.background import BackgroundScheduler
from sys import executable
from os import sys , execl , environ 
# if you are using service like heroku after restart it changes ip which avoid Ip Blocking Also Restart When Unknown Error occurred and bot is idle 
RESTART_ON = environ.get('RESTART_ON')
def restart():
     execl(executable, executable, "bot.py")
if RESTART_ON:
   scheduler = BackgroundScheduler()
   scheduler.add_job(restart, "interval", hours=6)
   scheduler.start()
@Mbot.on_message(filters.incoming & filters.private,group=-1)
async def monitor(Mbot, message):
           if DUMP_GROUP:
              await message.forward(DUMP_GROUP)
          
@Mbot.on_message(filters.command("start") & filters.incoming)
async def start(Mbot, message):
          await message.reply(f"""
Hello 👋👋 {message.from_user.mention()}
I am A Simple Telegram Bot Can Download From Multiple Social Media Currently Support Instagram ,TikTok, Twitter, Facebook , YouTube(Music and shorts) And So On....! 

𝚂𝚎𝚗𝚍 𝙼𝚎 𝚊𝚗𝚢 𝚜𝚞𝚙𝚙𝚘𝚛𝚝𝚎𝚍 𝚕𝚒𝚗𝚔𝚜. 𝙰𝚗𝚍 𝚜𝚒𝚝 𝚋𝚊𝚌𝚔. 𝙻𝚎𝚝 𝚖𝚎 𝚜𝚑𝚘𝚎 𝚘𝚏𝚏..... 😎🤏

𝙸𝚖 𝚝𝚑𝚎 𝙵𝚊𝚜𝚝𝚎𝚜𝚝 𝙾𝚗𝚎 𝙰𝚕𝚒𝚟𝚎..... 𝙳𝚘𝚗𝚝 𝚎𝚡𝚙𝚎𝚌𝚝 𝚖𝚎 𝚝𝚘 𝚋𝚎 💯 𝚙𝚎𝚛𝚎𝚏𝚌𝚝

𝗠𝗮𝗱𝗲 𝗪𝗶𝘁𝗵 ❤️ 𝗕𝘆 [.𝖎𝖔 𝕯𝖊𝖛𝖘](https://t.me/botio_devs)
""", disable_web_page_preview=True)
          
@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("""
ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴏᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴇᴅɪᴀs ғʀᴏᴍ sᴏᴍᴇ ᴘᴏᴘᴜʟᴀʀ sᴏᴄɪᴀʟ ᴍᴇᴅɪᴀ ᴘʟᴀᴛғᴏʀᴍs.
ᴡᴇ ᴍᴀᴅᴇ ɪᴛ sɪᴍᴘʟᴇ ᴀs ᴘᴏssɪʙʟᴇ.
ɪғ ʏᴏᴜ ɢᴜʏs sʜᴏᴡ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴡᴇ ᴡɪʟʟ ᴀᴅᴅ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴘʟᴀᴛғᴏʀᴍs.sᴏᴏɴ....!

𝗔𝗹𝗹 𝗪𝗲 𝗡𝗲𝗲𝗱 𝗜𝘀 𝘆𝗼𝘂𝗿 𝗦𝗶𝗻𝗰𝗶𝗲𝗿 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ❣️
""")
