import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv(9015244243:AAFIwANFKYG5IJs52ZjKCwAJ0Hf9m0HO9AU)
WEB_APP_URL = "https://beyyhanii-sudo.github.io/ton-mining-bot/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="⛏️ Kazıma Başla", 
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    await message.answer(
        "🚀 *TON Cloud Mining'e Hoş Geldin!*\n\n"
        "• İlk aşama *Ücretsiz CPU* ile hemen kazıma başla.\n"
        "• TON cüzdanını bağlayarak CPU seviyeni kademeli yükselt ve kazım hızını katla!",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

async def main():
    print("Bot çalışıyor...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
