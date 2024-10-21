import telebot
import requests
import json


bot = telebot.TeleBot(token='')
API = '9bf46d088e6326efbb3165de7a63a116'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,  "Hi! Welcome to the Weather Bot! Which City's Weather do you want to know?")

@bot.message_handler(content_types=['text'])
def get_text(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        weather_description = data['weather'][0]['main'].lower()

        if 'rain' in weather_description:
            bot.reply_to(message, f"Weather in {city.capitalize()}: {temp}°C, {weather_description.capitalize()} 🌧")
        elif 'cloud' in weather_description:
            bot.reply_to(message, f"Weather in {city.capitalize()}: {temp}°C, {weather_description.capitalize()} 🌥")
        elif 'snow' in weather_description:
            bot.reply_to(message, f"Weather in {city.capitalize()}: {temp}°C, {weather_description.capitalize()} 🌨")
        elif 'clear' in weather_description:
            bot.reply_to(message, f"Weather in {city.capitalize()}: {temp}°C, {weather_description.capitalize()} ☀️")
        else:
            bot.reply_to(message, f"Weather in {city.capitalize()}: {temp}°C, {weather_description.capitalize()} 🌤")

    else:
        bot.reply_to(message, f"Sorry {city.capitalize()} is not available")

bot.polling(none_stop=True)
