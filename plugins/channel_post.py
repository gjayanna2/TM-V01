#(©)Codexbotz
import aiohttp
import asyncio
from moviepy.video.io.VideoFileClip import VideoFileClip
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait
from plugins.data import ODD, EVEN ,BOTEFITMSG, FOMET
from plugins.cbb import DATEDAY
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from datetime import datetime
from helper_func import encode
from pyshorteners import Shortener
import string
import re


SAPI = "c5dbea7703b576144630660355aaa3dbd3a59cc5"
SSLINK = "upshrink.com"
@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["date"]))
async def date(bot, message):
    dat = await message.reply_text("Select Date.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.text & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    current_time = datetime.now()
    file = message.video or message.document
    # filname= media.file_name.split("S0")[0]#[1][2]etc
    ############# FOR UTSAV BOT ##################
    filname = re.split("S\d", file.file_name)[0]#[1][2]etc
    ############# FOR DS BOT ##################
    # filname = re.split(current_time.strftime("%B"), media.file_name)[0]#[1][2]etc
    #botfsno= re.findall("S0.+E\d+\d", media.file_name)
    fn = str(file.file_name.split("_")[0])
    file_folder = f'{Config.DOWNLOAD_LOCATION}/{fn}{str(random_char(5))}'
    file_path = f'{file_folder}/{file.file_name.split(".")[0]}.mp4'
    output_folder = f'{file_path}/Parts'
    video_length = file.file_size
    try:   
        if filname in ODD.keys():
            # chtid=int(ODD[filname][3])
            pic=ODD[filname][0]
            ms = await message.reply_text(text=f"Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....") 
            try:
            	await client.download_media(message = message , file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
            except Exception as e:
            	return await ms.edit(e)
            await ms.edit(text="DL complete")
            SL_URL=ODD[filname][1]
            SL_API=ODD[filname][2]
            bot_msg = await message.reply_text("Please Wait...!", quote = True, disable_web_page_preview = True)
            await asyncio.sleep(1)
        elif media.file_name in media.file_name:
            bot_msg = await message.reply_text("Please Wait...!", quote = True)
            link = await conv_link(client , message)
            sslink= await get_short(SSLINK, SAPI, link)
            await bot_msg.edit(f"<b>Here is your link</b>\n\n{link}\n\n<code>{link}</code>\n\nShort Link\n<code>{sslink}</code>")
        else:
            reply_text = await message.reply_text("❌Don't send me messages directly I'm only for serials!")

    except:
        await message.reply_text("Invalid DATE, Please set DATE again /date...?")
    
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    Tlink = f"https://telegram.me/{client.username}?start={base64_string}"
    Slink = await get_short(SL_URL, SL_API, Tlink)
    await bot_msg.edit("Analysing..!")
    await asyncio.sleep(1)
    await bot_msg.edit("Editing..!")
    await bot_msg.edit("Trying to send Poster.. ▣ ▢ ▢")
    await asyncio.sleep(1)
    await bot_msg.edit("Trying to send Poster.. ▣ ▣ ▢")
    await asyncio.sleep(1)
    await bot_msg.edit("Trying to send Poster.. ▣ ▣ ▣")
    await asyncio.sleep(1)

    await bot_msg.edit("Poster sent successfully...!")
    e_pic = await client.send_photo(chat_id=int(-1001956515516), photo=pic, caption= FOMET.format(DATEDAY[-1], Slink, Slink))
    #await bot_msg.edit(BOTEFITMSG.format(filname, botfsno[0], Tlink, Slink, DATEDAY[0]))
    await bot_msg.edit(BOTEFITMSG.format(filname, Tlink, Slink, DATEDAY[0]))
    
async def get_short(SL_URL, SL_API, Tlink):
    # FireLinks shorten
    try:
        api_url = f"https://{SL_URL}/api"
        params = {'api': SL_API, 'url': Tlink}
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, params=params, raise_for_status=True) as response:
                data = await response.json()
                url = data["shortenedUrl"]
        return url
    except Exception as error:
        return error

async def conv_link(client , message):
    try:
       post_message = await message.copy(chat_id = CHANNEL_ID, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = CHANNEL_ID, disable_notification=True)
    except Exception as e:
        print(e) 
        await client.send_message(message.chat.id, "Somthing is Wrong")
    converted_id = post_message.id * abs(CHANNEL_ID)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    # await client.send_massage(message.chat.id , f"<b>Here is your link</b>\n\n{link}\n\n<code>{link}</code>", disable_web_page_preview = True)
    return link
    
@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass




#generate random characters for location(path)
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

# splitting given video into equal parts
async def split_parts(file_path, parts, file_folder):
    video = VideoFileClip(file_path)
    video_length = video.duration
    duration_per_part = video_length / parts
    d = int(duration_per_part)
    output_folder = os.makedirs(f'{file_folder}/Parts')
    output_folder = f'{file_folder}/Parts'
    for i in range(parts):
        start_time = i * duration_per_part
        output_file = os.path.join(output_folder, f"part{i+1}.mp4")
        cmd = f"ffmpeg -i {file_path} -ss {start_time} -t {duration_per_part} -c copy {output_file}"
        subprocess.check_output(cmd, shell=True)
    return output_folder,d

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "ᴅ, ") if days else "") + \
        ((str(hours) + "ʜ, ") if hours else "") + \
        ((str(minutes) + "ᴍ, ") if minutes else "") + \
        ((str(seconds) + "ꜱ, ") if seconds else "") + \
        ((str(milliseconds) + "ᴍꜱ, ") if milliseconds else "")
    return tmp[:-2] 

def humanbytes(size):    
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'ʙ'

def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time

async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:        
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["⬢" for i in range(math.floor(percentage / 5))]),
            ''.join(["⬡" for i in range(20 - math.floor(percentage / 5))])
        )            
        tmp = progress + Config.PROGRESS_BAR.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),            
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",               
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="close")]])                                               
            )
        except:
            pass
