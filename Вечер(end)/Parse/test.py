import requests
import datetime

# Token
open_weather_token = 'dc09ede661b9bf605e28c882ea1fc240'

# Принимаем название города
city = input()


r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru")
data = r.json()


city = data["name"]
des = data["weather"][0]["description"]
cur_weath = data["main"]["temp"]
press = data["main"]["pressure"]
humidity = data["main"]["humidity"]
wind = data["wind"]["speed"]
country = data["sys"]["country"]
sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])


print(f"⚡️☄️💥🔥🌪 {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')} 🌪🔥💥☄️⚡\n️"
                    f"Название города: {city}\n"
        f"Текущая погода: {des}\n"
        f"Температура воздуха: {cur_weath}°C\n"
        f"Атмосферное давление: {press} мм.рт.ст.\n"
        f"Влажность воздуха: {humidity}%\n"
        f"Скорость ветра: {wind} м/с\n"
        f"Код страны: {country}\n"
        f"Восход: {sunrise}")
