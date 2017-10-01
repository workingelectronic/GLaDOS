'''
Domotic sytem base on IOT and Telegram control
Designed by
    Javier García Blanco

Location
    El taller, Santander

'''

import time
import telebot
import random
import subprocess
from os import system


# Token del bot
#file = open("Token.txt", "r")
#Tok = file.read()
#print(Tok)
bot = telebot.TeleBot("")

# Los que pueden usar el bot
admin = []

# Su contraseña
PASSWORD = "ABC"

"""
Comienza el programa,sistema de autorización
"""

# Extracts the unique_code from the sent /start command.
def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

# if unique_code = ABC: # if the '/start' command contains a unique_code
@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    unique_code = extract_unique_code(message.text)
    if unique_code == PASSWORD:
        admin.append(cid)
        print(admin)
        bot.send_message(message.chat.id, text="Bienvenido amo, estoy a su servicio.")
        bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
        time.sleep(1)
        bot.send_message(message.chat.id,
                          """Para conocer las opciones disponibles dentro del sistema, por favor escriba *Ayuda*""",
                         parse_mode="Markdown")
        return

    else:
        bot.send_message(message.chat.id, "Contraseña *incorrecta* para mas informacion escriba */help*",
                         parse_mode="Markdown")


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, "Bot esta protegido por contraseña, para conocerla contacte con el administrador")
    bot.send_message(message.chat.id, "Para acceder envía el comando */start* seguido de la contraseña.",
                     parse_mode="Markdown")


"""
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
                        Una vez asigandos los id por administrados comienda los comandos
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
"""
@bot.message_handler(regexp="Ayuda")
def comando_ayuda(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_message(cid, """*::Bienvenido a la ayuda::*""", parse_mode="Markdown")
        markup = telebot.types.ReplyKeyboardMarkup()
        itembtna = telebot.types.KeyboardButton('Foto')
        itembtnv = telebot.types.KeyboardButton('Video')
        itembtnc = telebot.types.KeyboardButton('Comando')
        itembtnd = telebot.types.KeyboardButton('Vigilancia')
        itembtne = telebot.types.KeyboardButton('Luz')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(cid, "Pulse sobre una de las siguientes opciones:", reply_markup=markup)
    else:
        bot.send_message(cid, u"""No estas autorizado, contacta con mi amo.""")

@bot.message_handler(regexp=u"[Cc]omando[!\?]*")
def command_long_text(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_message(cid, "Ejecutando: " + message.text[len("/comando"):])
        bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
        time.sleep(2)
        bot.send_message(cid, "Resultado: ")
    else:

        bot.send_message(cid, u"""No estas autorizado, contacta con mi amo.""")

@bot.message_handler(regexp="Foto")
def photo(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        subprocess.check_call(["python3","camera.py"])
        pt= open("/home/pi/Desktop/photo.jpg",'rb')
        bot.send_photo(message.chat.id, pt)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c"))
        CleanUp="rm photo*.jpg"
        system(CleanUp)
    else:

        bot.send_message(cid, text="No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Video")
def video(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        subprocess.check_call(["python3","Video.py"])
        vd= open("/home/pi/Desktop/video.mp4",'rb')
        bot.send_video(message.chat.id, vd)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c"))
        CleanUp="rm video.mp4 video.h264"
        system(CleanUp)
    else:

        bot.send_message(cid, text="No estas autorizado, contacta con mi amo.")
        
@bot.message_handler(regexp="Vigilancia")
def vigilancia(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_message(cid, text="Activada.")
        subprocess.check_call(["python3","Movedetector.py"])
        bot.send_message(cid, text="Movimiento detectado.")
        photo()
        video()
    else:

        bot.send_message(cid, text="No estas autorizado, contacta con mi amo.")

"""
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
Apartado control de los ESP8266, el problema esta en la activación, así que va aquí a piñon, porque en
scripts a parte no espera a recibir una orden
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
"""

@bot.message_handler(regexp="Luz")
def comando_ayuda(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_message(message.chat.id, """*::Iluminación::*""", parse_mode="Markdown")
        markup = telebot.types.ReplyKeyboardMarkup()
        itembtna = telebot.types.KeyboardButton('Baño')
        itembtnv = telebot.types.KeyboardButton('Cocina')
        itembtnc = telebot.types.KeyboardButton('Salon')
        itembtnd = telebot.types.KeyboardButton('Cuarto')
        itembtne = telebot.types.KeyboardButton('Pasillo')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(cid, "Pulse sobre una de las siguientes opciones:", reply_markup=markup)
    else:
        bot.send_message(cid, u"""No estas autorizado, contacta con mi amo.""")

@bot.message_handler(regexp = "Salon")
@bot.message_handler(regexp = "Baño")
@bot.message_handler(regexp = "Cocina")
@bot.message_handler(regexp = "Salon")
@bot.message_handler(regexp = "Cuarto")
@bot.message_handler(regexp = "Pasillo")
def habitacion(message):
    cid = message.chat.id
    room = message.text
    result = cid in admin
    if result is True:
        print(message.text)
        subprocess.check_call(["python3", room+".py"])
        time.sleep(0.1)
        file = open("State.txt", "r")
        answer= file.read()
        bot.send_message(cid, answer)
        print(file.read())
    else:
        bot.send_message(cid, u"""No estas autorizado, contacta con mi amo.""")


"""
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
Parte humana, para dar respuesta ante posibles frustraciones. Javi lo considera fundamental =).
Seguro que Jaled tiene algo que contar sobre psicología y chorradas
Conviene ponerlo al final porque he comprobado que ante 2 comandos realiza el primero
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
"""


respuesta = ['Lo siento amo, no volverá a ocurrir','No me golpee amo, seré bueno',
             'ClipClap será mejor la próxima vez, lo prometo','Robot idiota, no volverá a ocurrir','Lo siento amo']

@bot.message_handler(regexp = "Idiota")
@bot.message_handler(regexp = "Inútil")
@bot.message_handler(regexp = 'Basura')
@bot.message_handler(regexp = "Puto")
@bot.message_handler(regexp = "Muerete")
@bot.message_handler(regexp = "Odio")
@bot.message_handler(regexp = "Asco")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, random.choice(respuesta))
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Mando")
@bot.message_handler(regexp="Digo")
@bot.message_handler(regexp="Calla")
@bot.message_handler(regexp="Ordeno")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Si amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Bien")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Robot aprende gracias a amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="eh")
@bot.message_handler(regexp="tu")
@bot.message_handler(regexp="Hola")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Hola amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")        
"""
--------------------------------------------------------------------------------------------------------
Respuesta ante comando no encontrado
--------------------------------------------------------------------------------------------------------
"""

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(1)
    bot.reply_to(message, "No es ninguna orden señor, escribame algo  que pueda hacer")

bot.polling()
