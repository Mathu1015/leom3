import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client as tgClient, enums
from tzlocal import get_localzone

# Fix for environments where no event loop exists yet
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# qBittorrent options setup
if not qbit_options:
    qbit_options = dict(xnox_client.app_preferences())
    del qbit_options["listen_port"]
    for k in list(qbit_options.keys()):
        if k.startswith("rss"):
            del qbit_options[k]
else:
    qb_opt = {**qbit_options}
    xnox_client.app_set_preferences(qb_opt)

# Aria2 options (currently disabled)
# aria2_options = aria2.client.get_global_option()
# a2c_glo = {op: aria2_options[op] for op in aria2c_global if op in aria2_options}
# aria2.set_global_options(a2c_glo)

bot = tgClient(
    "bot",
    TELEGRAM_API,
    TELEGRAM_HASH,
    bot_token=BOT_TOKEN,
    workers=1000,
    parse_mode=enums.ParseMode.HTML,
).start()

bot_loop = bot.loop
bot_name = bot.me.username

scheduler = AsyncIOScheduler(timezone=str(get_localzone()), event_loop=bot_loop)
