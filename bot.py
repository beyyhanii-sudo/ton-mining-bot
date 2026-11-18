import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv(9015244243:AAFIwANFKYG5IJs52ZjKCwAJ0Hf9m0HO9AU)
WEB_APP_URL = "https://github.io"

import os
import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web

# Konfigürasyon kontrolü
TOKEN = os.getenv("9015244243:AAFIwANFKYG5IJs52ZjKCwAJ0Hf9m0HO9AU")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://beyyhanii-sudo.github.io/ton-mining-bot/")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    args = message.get_args()  # Örn: ref_12345 parametresini yakalar
    user_id = message.from_user.id
    
    # Kullanıcı referansla geldiyse burada veritabanına kaydedebilirsin
    if args:
        print(f"Kullanıcı {user_id}, {args} referans kodu ile katıldı.")

    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="⛏️ Madencilik Konsolunu Aç",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )
    
    welcome_text = (
        f"👑 **TON Cloud Mining Pro**'ya hoş geldin!\n\n"
        f"🆔 Telegram ID: `{user_id}`\n"
        f"⚡ Bulut tabanlı kazım motoruna bağlanmak için aşağıdaki butona tıkla."
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=keyboard)

async def handle_ping(request):
    return web.Response(text="Bot aktif ve çalışıyor!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    
    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
