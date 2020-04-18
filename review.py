# coding: utf-8
import pyowm
import telebot

#https://pypi.org/project/pyTelegramBotAPI/
#pip3 install pyTelegramBotAPI

token = '1237721078:AAECataq3K694n0n0MwJlJxAqx-3nbnar58'
api = 'e70a43b8a010c59d5309454867f6e529'
tb = telebot.TeleBot(token)

def start():
    tb.polling(none_stop=True)

@tb.message_handler(commands=['start'])
def send_welcome( message):
    tb.send_message(message.chat.id, "Привет, в каком вы городе или стране?")

@tb.message_handler(content_types=["text"])
def send_message( message):
    city = message.text
    weather = get_weather(city)

    if weather is None:
        tb.send_message(message.chat.id, "Хмм... я такого города и тем более страны не знаю.")
        tb.send_message(message.chat.id, "Попробуй еще раз.")
        return

    temp = weather.get_temperature('celsius')['temp']
    forecast = weather.get_detailed_status()
    recommendation = get_recommendation(temp)

    response = build_response(city, forecast, recommendation);

    tb.send_message(message.chat.id, answer)
    tb.send_message(message.chat.id, "Для какого города хотите еще узнать погоду?")

def get_weather(city):
    try:
        return pyowm.OWM(api, language="ru").weather_at_place(message.text).get_weather()
    except:
        return None

def get_recommendation(temp):
    if temp <= 10.0:
        return "На улице достаточно холодно, оденься тепло!"
    elif temp <= 20.0:
        return "На улице не так холодно, но легкую куртку лучше надеть!"
    else:
        return "На улице достаточно тепло, одевайся как хочешь."

def build_response(city, forecast, recommendation):
    return f"""
        {city} - место, где сейчас {forecast}
            Текущая температура: {temp} градусов цельсия.
            {recommendation}
        """
start()