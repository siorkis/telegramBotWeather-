import pyowm              # weather's library 
import telebot            # bot's library 


tb = telebot.TeleBot("TOKEN") # bot's identification 


@tb.message_handler(commands=['start']) # bot sends the welcome message 
def send_welcome(message):
    tb.send_message(message.chat.id, "Привет, в каком вы городе/стране?\n")


@tb.message_handler(content_types=["text"]) # bot reads the massege from user
def send_message(message):
    try:                                     # checking user's message, does it city/country or not
        owm = pyowm.OWM('API', language="ru") 
        observation = owm.weather_at_place(message.text) #taking city from data base 
    except:                                              # case of wrong input 
        tb.send_message(message.chat.id, "Хмм... я такого города и тем более страны не знаю ((") 
        tb.send_message(message.chat.id, "Попробуй еще раз"
                                         ".")
    else:                                                 # case of correct input
        w = observation.get_weather()                     # getting information about weather in indicated place
        temp = w.get_temperature('celsius')['temp']       # getting information about temperature in indicated place
        answer = message.text + " - место, где сейчас " + w.get_detailed_status() + ".\n"
        answer += "Текущая температура: " + str(temp) + ' градусов цельсия\n\n'
        if temp <= 10.0:
            answer += "На улице достаточно холодно, оденься тепло!\n"
        elif temp <= 20.0:
            answer += "На улице не так холодно, но легкую куртку лучше надеть!\n"
        else:
            answer += "На улице достаточно тепло, одевайся как хочешь)\n"
        tb.send_message(message.chat.id, answer)           # bot sends message with weather to user 
        tb.send_message(message.chat.id, "Для какого города хотите еще узнать погоду?") # bot sends the ending massege


tb.polling(none_stop=True)       # bot don't stop sending messages 
