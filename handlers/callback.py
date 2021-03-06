

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
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
        f"""<b>๐ผ **ูุฑุญุจุง , {query.message.from_user.mention} !** \n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ูุณูุญ ูู ุจุชุดุบูู ุงูููุณููู ุนูู ุงููุฌููุนุงุช ูู ุฎูุงู ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ูู Telegram ุงูุฌุฏูุฏุฉ!**

 **ูุนุฑูุฉ ุฌููุน ุงูุฃูุงูุฑ ุจูุช ูููููุฉ ุนูููุง ูู ุฎูุงู ุงูููุฑ ุนูู ุฒุฑ ยป ๐ ุงูุฃูุงูุฑ !**

 ููููุฉ ุงุณุชุฎุฏุงู ูุฐุง ุจูุชุ ูุฑุฌู ุงูุถุบุท ุนูู ยป ุฏููู ุงููุณุชุฎุฏู !**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        " ุฃุถููู ุฅูู ูุฌููุนุชู", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        " ุฏููู ุงููุณุชุฎุฏู   ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "๐ ูุงูุงูุฑ", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "ุงููุทูุฑ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        " ููุงู  ุงููููุงุช", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ูฐ๐ูฐูฐ๐ู๐ ูู๐ูฐูฐ๐ูู ๐ฆูู๐ู๐ฑู๐ูฐ๐ ๐ฆ โน", url=f"https://t.me/U_U_U_Q")
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ูุฑุญุจุง ุจูู ูู ูุงุฆูุฉ ุงููุณุงุนุฏุฉ : </b>

โ โ โ โ โ โ โ โ โ โ โ
ูู ูุฐู ุงููุงุฆูุฉ ููููู ูุชุญ ุงูุนุฏูุฏ ูู ููุงุฆู ุงูุฃูุงูุฑ ุงููุชุงุญุฉ ูู ูู ูุงุฆูุฉ ุงูุฃูุฑ ููุงู ุฃูุถุง ุดุฑุญ ููุฌุฒ ููู ุฃูุฑ .

- Powered by DetroitSogbot ๐ธ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๏ธุงูุงูุงูุฑ ุงูุงุณุงุณูู", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ฝ๏ธุงูุงูุงูุฑ ุงููุชูุฏูู ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ฆน๐ป๏ธุงูุงูุฑ ุงูุงุฏูููู", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐๏ธุงูุงูุฑ ุงููุทูุฑูู", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐๏ธุงูุงูุฑ ุงููุงูู", callback_data="cbowner"
                    )
                ],
              
                [
                    InlineKeyboardButton(
                        "๐ก ุงูุฑุฌูุน ุงูู ุงููุณุงุนุฏู", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ ููุง ุงูุฃูุงูุฑ ุงูุฃุณุงุณูุฉ</b>
โ โ โ โ โ โ โ โ โ โ โ
- ุจุญุซ ุนู ุงุบููู ( ุงุณู ุงูุงุบููุฉ ู /Play )
- ุชุดุบูู ุงูุฃุบููุฉ ูุจุงุดุฑุฉ ูู ุงูููุชููุจ 
( ุฃุณู ุงูุงุบููุฉ ู /Ytp ) .
- ุชุดุบูู ุงูุฃุบููุฉ ุจุงุณุชุฎุฏุงู ููู ุตูุชู 
( /Stream ) . 
- ุฅุธูุงุฑ ุฃุบููุฉ ุงููุงุฆูุฉ ูู ูุงุฆูุฉ ุงูุงูุชุธุงุฑ 
( /Playlist )
- ุชูุฒูู ุงุบููุฉ ูู ุงูููุชููุจ :
( ุฃุณู ุงูุงุบููุฉ ู /Vsong ) 
ููุจุญุซ ุนู ููุทุน ููุฏูู ุจุงูููุชููุจ 
( ุฃุณู ุงูุงุบููุฉ ู /Search ) 
- ุชูุฒูู ููุฏูู ูู ุงูููุชููุจ ุจุงูุชูุตูู 
( ุงุณู ุงูููุฏูู ู / Vsong ) 
โ โ โ โ โ โ โ โ โ โ โ
-ุชุดุบูู ุงูููุณููู ูู ุงูุงุชุตุงู ( /Play )
( /cplayer ) ุฅุธูุงุฑ ุงูุฃุบููุฉ ุฃุซูุงุก ุงูุจุซ -
- ุฅููุงู ุงูููุณููู ุงููุดุชุบูุฉ ูุคูุชูุง 
( /cpause )
- ุงุณุชุฆูุงู ุชููู ุงูุจุซ ูุคูุชุงู ( /cresume )
( /cskip ) ุชุฎุทู ุงูุฃุบููุฉ -
( /cend ) ูู ุจุฅููุงุก ุชุฏูู ุงูููุณููู -
- ุชุญุฏูุซ ุงูุฐุงูุฑุฉ ุงููุคูุชุฉ :
( /admincache )
(/userbotjoin ) ูู ุจุฏุนูุฉ ุงููุณุงุนุฏ

ุจููุงุณุทูุฉ ุงูููุจุฑูุฌ ุงุญูุฏ ุณููุฑููุง

 __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ธ๏ธ ูุง ูู ุงูุฃูุงูุฑ ุงููุชูุฏูุฉ </b>

 ๐ธ๏ธ ูุง ูู ุงูุฃูุงูุฑ ุงููุชูุฏูุฉ /
 โ โ โ โ โ โ โ โ โ โ โ
( /start ) ุชุดุบูู ุงูุจูุช ูู ุงููุฌููุนู
( /cache ) ุจุชุญุฏูุซ ูุงุฆูุฉ ุงูุฅุฏุงุฑุฉ
ุชุญุฏูุซ ุฐุงูุฑุฉ ุงูุชุฎุฒูู ุงููุคูุช( /cache )
( /ping ) ุชุญูู ูู ุญุงูุฉ ุงูุจูุช
( /uptime ) ุชุญูู ูู ุญุงูุฉ ููุช ุชุดุบูู
( /id ) ุฅุธูุงุฑ ูููุฉ ุงููุณุชุฎุฏู ูุบูุฑูุง""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ธ๏ธููุง ูู ุฃูุงูุฑ ุงููุดุฑู </b>

โ โ โ โ โ โ โ โ โ โ โ
ุนุฑุถ ุญุงูุฉ ุชุดุบูู ( /player )
ุฅููุงู ุชุดุบูู ุงูููุณููู ูุคูุชูุง ( /pause )
ุงุณุชุฆูุงู ุชู ุฅููุงู ุงูููุณููู ูุคูุชูุง ( /pause )
( /skip ) ุงูุชูู ุฅูู ุงูุฃุบููุฉ ุงูุชุงููุฉ
( /stop ) ุฅููุงู ุชุดุบูู ุงูููุณููู
ุฏุนูุฉ ุงููุณุงุนุฏ ููุงูุถูุงู 
ุฅูู ูุฌููุนุชู ( /userbotjoin ) 
ุงููุณุชุฎุฏู ุงููุตุฑุญ ูู ุจุงุณุชุฎุฏุงู ุจุฑูุงูุฌ Music bot ( /auth )
ุบูุฑ ูุตุฑุญ ุจู ูุงุณุชุฎุฏุงู ุจุฑูุงูุฌ ุชุชุจุน ุงูููุณููู ( /deauth )
ุงูุชุญ ููุญุฉ ุงูุชุญู ุฅุนุฏุงุฏุงุช ุงููุดุบู 
( /control ) 
/delcmd (on | off) - ุชูููู / ุชุนุทูู ููุฒุฉ del cmd
/musicplayer ูุดุบู ุงูููุณููู (ุชุดุบูู ุฅููุงู) - ุชุนุทูู / ุชูููู ูุดุบู ุงูููุณููู ูู ูุฌููุนุชู
/b ู /tb (ุงูุญุธุฑ / ุงูุญุธุฑ ุงููุคูุช) - ูุณุชุฎุฏู ูุญุธูุฑ ุจุดูู ุฏุงุฆู ุฃู ูุคูุช ูู ุงููุฌููุนุฉ
/ub - ุฅูู ูุณุชุฎุฏู ุบูุฑ ูุญุธูุฑ ุชู ุญุธุฑู ูู ุงููุฌููุนุฉ
/m ู /tm (ูุชู ุงูุตูุช / ูุชู ุงูุตูุช ุงููุคูุช) - ูุชู ุตูุช ุงููุณุชุฎุฏู ูู ุงููุฌููุนุฉ ุจุดูู ุฏุงุฆู ุฃู ูุคูุช
/um - ูุฅูุบุงุก ูุชู ุตูุช ุงููุณุชุฎุฏู ุงูุฐู ุชู ูุชูู ูู ุงููุฌููุนุฉ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ ููุง ุฃูุงูุฑ ุงููุทูุฑ </b>
โ โ โ โ โ โ โ โ โ โ โ
( /userbotleaveall ) ุงููุบุงุฏุฑุฉ ูู ุงููุฌููุนุฉ
ุงููุบุงุฏุฑุฉ ูู ุฌููุน ุงููุฌููุนุงุช ( /trought )
ุงุฑุณุงู ุฑุณุงูุฉ ุจุซ ( /gcast )
( /stats ) ุฅุธูุงุฑ ุฅุญุตุงุฆูุฉ ุงูุจูุช
( /rmd ) ุฅุฒุงูุฉ ูุงูุฉ ุงููููุงุช ุงูุชู ุชู ุชูุฒูููุง""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฆน๐ป ููุง ูู ุฃูุงูุฑ ุงููุงูู :</b>
โ โ โ โ โ โ โ โ โ โ โ
ุงุธูุงุฑ ุงุญุตุงุฆูุงุช ุงูุจูุช ( /stats )
ุงุฑุณุงู ุงุฐุงุนู ูู ุงูุจูุช ( /broadcast )
ุญุธุฑ ูุณุชุฎุฏู 
( ูุนุฑู ุงููุณุชุฎุฏู ู /block )
ุงูุบุงุก ุญุธุฑ ุงููุณุชุฎุฏู 
( ูุนุฑู ุงููุณุชุฎุฏู ู /unblock )
ูุฑุคูุฉ ุงููุญุธูุฑูู ( /blocklist )
โ โ โ โ โ โ โ โ โ โ โ
ููุงุญุธุฉ: ูููู ุชูููุฐ ุฌููุน ุงูุฃูุงูุฑ ุงูุชู ูููููุง ูุฐุง ุงูุจูุช ูู ูุจู ูุงูู ุงูุจูุช ุฏูู ุฃู ุงุณุชุซูุงุกุงุช . ๐ธ. _""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ููููุฉ ุงุณุชุฎุฏุงู ูุฐุง ุงูุจูุช:

1.) ุฃููุงุ ุฅุถุงูุฉ ูู ุฅูู ูุฌููุนุชู.
2.) ุซู ุชุฑููุฉ ูู ููุณุคูู ูุฅุนุทุงุก ุฌููุน ุงูุฃุฐููุงุช ุจุงุณุชุซูุงุก ุงููุดุฑู ูุฌููู.
3.) ุฅุถุงูุฉ @{ASSISTANT_NAME} ุฅูู ูุฌููุนุชู ุฃู ุงูุชุจ  /userbotjoin  ูุฏุนูุชูุง.
4.) ุชุดุบูู ุงูุฏุฑุฏุดุฉ ุงูุตูุชูุฉ ุฃููุง ูุจู ุงูุจุฏุก ูู ุชุดุบูู ุงูููุณููู. _""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ ุงูุงูุงูุฑ", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ป ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐ธููุง ูุงุฆูุฉ ุงูุชุญูู ูู ุงูุจูุช :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("โธ pause", callback_data="cbpause"),
                    InlineKeyboardButton("โถ๏ธ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("โฉ skip", callback_data="cbskip"),
                    InlineKeyboardButton("โน end", callback_data="cbend"),
                ],
                [InlineKeyboardButton("๐ธ๏ธุงูุงูุฑ ุงููุดุฑููู ", callback_data="cbdelcmds")],
                [InlineKeyboardButton("๐ธ๏ธุงุนุฏุงุฏุงุช ุงููุฌููุนู", callback_data="cbgtools")],
                [InlineKeyboardButton("๐ป ุงูุบุงุก", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ูุฐู ูู ููุฒุฉ ุงููุนูููุงุชn :</b>
๐ผ ** ุงูููุฒุฉ: ** ุชุญุชูู ูุฐู ุงูููุฒุฉ ุนูู ูุธุงุฆู ูููููุง ุญุธุฑ ููุชู ุงูุตูุช ูุฅูุบุงุก ุงูุญุธุฑ ูุฅูุบุงุก ูุชู ุตูุช ุงููุณุชุฎุฏููู ูู ูุฌููุนุชู.
ูููููู ุฃูุถูุง ุชุญุฏูุฏ ููุช ููุญุธุฑ ูุนููุจุงุช ูุชู ุงูุตูุช ูุฃุนุถุงุก ูุฌููุนุชู ุจุญูุซ ูููู ุชุญุฑูุฑูู ูู ุงูุนููุจุฉ ูู ุงูููุช ุงููุญุฏุฏ.
โ ** ุงูุงุณุชุฎุฏุงู: **
1๏ธโฃ ุญุธุฑ ุงููุณุชุฎุฏู ูุญุธุฑู ูุคูุชูุง ูู ูุฌููุนุชู:
   ยปุงูุชุจ` / b ุงุณู ุงููุณุชุฎุฏู / ุงูุฑุฏ ุนูู ุงูุฑุณุงูุฉ` ุญุธุฑ ุจุดูู ุฏุงุฆู
   ุงูุชุจ `/ tb username / ุงูุฑุฏ ุนูู ุงูุฑุณุงูุฉ / ุงููุฏุฉ` ุญุธุฑ ุงููุณุชุฎุฏู ูุคูุชูุง
   ยปุงูุชุจ` / ub username / ุฑุฏ ุนูู ุงูุฑุณุงูุฉ` ููุณุชุฎุฏู ุบูุฑ ูุญุธูุฑ
2๏ธโฃ ูุชู ููุชู ุงููุณุชุฎุฏู ูุคูุชูุง ูู ูุฌููุนุชู:
   ยปุงูุชุจ` / m ุงุณู ุงููุณุชุฎุฏู / ุงูุฑุฏ ุนูู ุงูุฑุณุงูุฉ` ูุชู ุงูุตูุช ุจุดูู ุฏุงุฆู
   ุงูุชุจ `/ tm ุงุณู ุงููุณุชุฎุฏู / ุงูุฑุฏ ุนูู ุงูุฑุณุงูุฉ / ุงููุฏุฉ` ูุชู ุงููุณุชุฎุฏู ูุคูุชูุง
   ยปุงูุชุจ` / um ุงุณู ุงููุณุชุฎุฏู / ุฑุฏ ุนูู ุงูุฑุณุงูุฉ` ูุฅูุบุงุก ูุชู ุตูุช ุงููุณุชุฎุฏู
๐ ููุงุญุธุฉ: cmd / b ู / tb ู / ub ูู ูุธููุฉ ูููุณุชุฎุฏู ุงููุญุธูุฑ / ุบูุฑ ุงููุญุธูุฑ ูู ูุฌููุนุชู ุ ุจูููุง / m ู / tm ู / um ูู ุฃูุงูุฑ ููุชู / ุฅูุบุงุก ูุชู ุตูุช ุงููุณุชุฎุฏู ูู ูุฌููุนุชู""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ก Go Back", callback_data="cbback")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ูุฐู ูู ูุนูููุงุช ุงูููุฒุฉ :</b>
        
**๐ก ุงูููุฒุฉ:** ุญุฐู ูู ุงูุฃูุงูุฑ ุงููุฑุณูุฉ ูู ูุจู ุงููุณุชุฎุฏููู ูุชุฌูุจ ุงูุจุฑูุฏ ุงููุฒุนุฌ ูู ูุฌููุนุงุช !

โ ูุซุงู:**

 1๏ธโฃูุชุดุบูู ุงูููุฒุฉ :
     ยป `/delcmd on`
    
 2๏ธโฃ ูุฅููุงู ุชุดุบูู ุงูููุฒุฉ:
     ยป  `/delcmd off`
      
โก  by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ูุฑุญุจูุง ุจูู ุ ูุฑุญุจูุง ุจูู ูู ูุงุฆูุฉ ุงููุณุงุนุฏุฉ !</b>

**ูู ูุฐู ุงููุงุฆูุฉ ุ ููููู ูุชุญ ุงูุนุฏูุฏ ูู ููุงุฆู ุงูุฃูุงูุฑ ุงููุชุงุญุฉ ุ ููู ูู ูุงุฆูุฉ ุฃูุงูุฑ ููุฌุฏ ุฃูุถูุง ุดุฑุญ ููุฌุฒ ููู ุฃูุฑ **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๏ธุงูุงูุงูุฑ ุงูุงุณุงุณูู", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ฝ๏ธุงูุงูุงูุฑ ุงููุชูุฏูู", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ฆน๐ป๏ธุงูุงูุฑ ุงูุงุฏูููู", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐๏ธุงูุงูุฑ ุงููุทูุฑูู", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐๏ธุงูุงูุฑ ุงููุงูู", callback_data="cbowner"
                    )
                ],
        
                [
                    InlineKeyboardButton(
                        "๐ก ุงูุฑุฌูุน", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ููููุฉ ุงุณุชุฎุฏุงู ูุฐุง ุงูุจูุช:

1.) ุฃููุงุ ุฅุถุงูุฉ ูู ุฅูู ูุฌููุนุชู.
2.) ุซู ุชุฑููุฉ ูู ููุณุคูู ูุฅุนุทุงุก ุฌููุน ุงูุฃุฐููุงุช ุจุงุณุชุซูุงุก ุงููุดุฑู ูุฌููู.
3.) ุฅุถุงูุฉ @{ASSISTANT_NAME} ุฅูู ูุฌููุนุชู ุฃู ุงูุชุจ /userbotjoin ูุฏุนูุชูุง.
4.) ุชุดุบูู ุงูุฏุฑุฏุดุฉ ุงูุตูุชูุฉ ุฃููุง ูุจู ุงูุจุฏุก ูู ุชุดุบูู ุงูููุณููู.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
