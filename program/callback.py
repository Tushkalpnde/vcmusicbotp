# Copyright (C) 2021 By MarrkMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **๐ฒโฏ๐๐ธโด๐โฏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ๐ช๐ต๐ต๐ธ๐๐ผ ๐๐ธ๐พ ๐ฝ๐ธ ๐น๐ต๐ช๐ ๐ถ๐พ๐ผ๐ฒ๐ฌ ๐ช๐ท๐ญ ๐ฟ๐ฒ๐ญ๐ฎ๐ธ ๐ธ๐ท ๐ฐ๐ป๐ธ๐พ๐น๐ผ ๐ฝ๐ฑ๐ป๐ธ๐พ๐ฐ๐ฑ ๐ฝ๐ฑ๐ฎ ๐ท๐ฎ๐ ๐ฃ๐ฎ๐ต๐ฎ๐ฐ๐ป๐ช๐ถ'๐ผ ๐ฟ๐ฒ๐ญ๐ฎ๐ธ ๐ฌ๐ฑ๐ช๐ฝ๐ผ!**
๐ก **๐๐ฒ๐ท๐ญ ๐ธ๐พ๐ฝ ๐ช๐ต๐ต ๐ฝ๐ฑ๐ฎ ๐๐ธ๐ฝ'๐ผ ๐ฌ๐ธ๐ถ๐ถ๐ช๐ท๐ญ๐ผ ๐ช๐ท๐ญ ๐ฑ๐ธ๐ ๐ฝ๐ฑ๐ฎ๐ ๐๐ธ๐ป๐ด ๐ซ๐ ๐ฌ๐ต๐ฒ๐ฌ๐ด๐ฒ๐ท๐ฐ ๐ธ๐ท ๐ฝ๐ฑ๐ฎ ยป ๐๐โด๐๐๐ถ๐๐น๐ ๐ท๐๐๐โด๐!**

๐ **๐ฏโด ๐๐โด๐ ๐ฝโด๐ ๐โด ๐๐โฏ ๐๐ฝ๐พ๐ ๐ทโด๐, ๐๐โฏ๐ถ๐โฏ ๐ธ๐๐พ๐ธ๐ โด๐ ๐๐ฝโฏ ยป โโฌ๐ถ๐๐พ๐ธ ๐ข๐๐พ๐นโฏ ๐ท๐๐๐โด๐!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ๐ฌ๐๐ ๐๐ ๐๐ ๐๐๐๐ ๐ฒ๐๐๐๐ โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ๐ฑ๐๐๐๐ ๐ถ๐๐๐๐", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐๐ฒ๐๐๐๐๐๐๐", callback_data="cbcmds"),
                    InlineKeyboardButton("โจ๐ฑ๐๐๐๐๐โจ", url=f"https://t.me/marrk85"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ๐ถ๐๐๐๐", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ๐ฒ๐๐๐๐๐๐", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐บ๐๐๐๐๐ ๐ช๐๐๐", url="https://github.com/marrk85/iron-video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the basic commands:

ยป /play (song name/link) - play music on video chat
ยป /stream (query/link) - stream the yt live/radio live music
ยป /vplay (video name/link) - play video on video chat
ยป /vstream - play live video from yt live
ยป /playlist - show you the playlist
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /lyric (query) - scrap the song lyric
ยป /search (query) - search a youtube video link

ยป /ping - show the bot ping status
ยป /uptime - show the bot uptime status
ยป /alive - show the bot alive info (in group)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the admin commands:

ยป /pause - pause the stream
ยป /resume - resume the stream
ยป /skip - switch to next stream
ยป /stop - stop the streaming
ยป /vmute - mute the userbot on voice chat
ยป /vunmute - unmute the userbot on voice chat
ยป /reload - reload bot and refresh the admin data
ยป /userbotjoin - invite the userbot to join group
ยป /userbotleave - order userbot to leave from group

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป /leaveall - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
