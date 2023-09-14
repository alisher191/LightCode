import requests
import datetime
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

open_weather_token = "dc09ede661b9bf605e28c882ea1fc240"
bot_token = "6291187696:AAEqGl5vsU90W-mcHctAltTxwozhwRTK5xs"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply("Привет! Напиши название города")


@dp.message_handler()
async def get_weather(message):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang=ru")
        data = r.json()
        # pp(data)
        city = data["name"]
        des = data["weather"][0]["description"]
        cur_weath = data["main"]["temp"]
        press = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        await message.reply(f"⚡️☄️💥🔥🌪 {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')} 🌪🔥💥☄️⚡\n️"
                            f"Название города: {city}\n"
              f"Текущая погода: {des}\n"
              f"Температура воздуха: {cur_weath}°C\n"
              f"Атмосферное давление: {press} мм.рт.ст.\n"
              f"Влажность воздуха: {humidity}%\n"
              f"Скорость ветра: {wind} м/с\n"
              f"Код страны: {country}\n"
              f"Восход: {sunrise}")

    except Exception as ex:
        await message.reply("Проверьте название города!")


if __name__ == '__main__':
    executor.start_polling(dp)