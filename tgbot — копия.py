import pyowm
import telebot


tb = telebot.TeleBot("TOKEN")


@tb.message_handler(commands=['start'])
def send_welcome(message):
    tb.send_message(message.chat.id, "Привет, в каком вы городе/стране?\n")


@tb.message_handler(content_types=["text"])
def send_message(message):
    try:
        owm = pyowm.OWM('e70a43b8a010c59d5309454867f6e529', language="ru")
        observation = owm.weather_at_place(message.text)
    except:
        tb.send_message(message.chat.id, "Хмм... я такого города и тем более страны не знаю ((")
        tb.send_message(message.chat.id, "Попробуй еще раз"
                                         ".")
    else:
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        answer = message.text + " - место, где сейчас " + w.get_detailed_status() + ".\n"
        answer += "Текущая температура: " + str(temp) + ' градусов цельсия\n\n'
        if temp <= 10.0:
            answer += "На улице достаточно холодно, оденься тепло!\n"
        elif temp <= 20.0:
            answer += "На улице не так холодно, но легкую куртку лучше надеть!\n"
        else:
            answer += "На улице достаточно тепло, одевайся как хочешь)\n"
        tb.send_message(message.chat.id, answer)
        tb.send_message(message.chat.id, "Для какого города хотите еще узнать погоду?")


tb.polling(none_stop=True)
