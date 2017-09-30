
import time
import telebot
import random
import subprocess
from os import system

# Token del bot
bot = telebot.TeleBot("Token")

# Los que pueden usar el bot
admin = []

# Su contraseña
PASSWORD = "ABC"

"""
Comienza el programa
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


@bot.message_handler(regexp=u"[Ff]oto[!\?]*")
def photo_me(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        subprocess.check_call(["python3","/home/pi/Camara/camera.py"])
        pt= open("/home/pi/Desktop/photo.jpg",'rb')
        bot.send_photo(message.chat.id, pt)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c"))
        CleanUp="rm photo*.jpg"
        system(CleanUp)
    else:

        bot.send_message(cid, text="No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Video")
def photo_me(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        subprocess.check_call(["python3","/home/pi/Camara/Video.py"])
        vd= open("/home/pi/Desktop/video.mp4",'rb')
        bot.send_video(message.chat.id, vd)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c"))
        CleanUp="rm video.mp4 video.h264"
        system(CleanUp)
    else:

        bot.send_message(cid, text="No estas autorizado, contacta con mi amo.")
        
@bot.message_handler(regexp="Vigilancia")
def photo_me(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_message(cid, text="Activada.")
        subprocess.check_call(["python3","/home/pi/Camara/Movedetector.py"])
        bot.send_message(cid, text="Movimiento detectado.")
        subprocess.check_call(["python3","/home/pi/Camara/camera.py"])
        subprocess.check_call(["python3","/home/pi/Camara/Video.py"])
        pt= open("/home/pi/Desktop/photo.jpg",'rb')
        bot.send_photo(message.chat.id, pt)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c"))
        vd= open("/home/pi/Desktop/video.mp4",'rb')
        bot.send_video(message.chat.id, vd)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c"))
        CleanUp="rm video.mp4 video.h264 photo.jpg"
        system(CleanUp)
    else:

        bot.send_message(cid, text="No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp=u"[Aa]yuda[!\?]*")
def comando_ayuda(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_message(message.chat.id, """*::Bienvenido a la ayuda::*""", parse_mode="Markdown")
        markup = telebot.types.ReplyKeyboardMarkup()
        itembtna = telebot.types.KeyboardButton('Foto')
        itembtnv = telebot.types.KeyboardButton('Video')
        itembtnc = telebot.types.KeyboardButton('Comando')
        itembtnd = telebot.types.KeyboardButton('Vigilancia')
        itembtne = telebot.types.KeyboardButton('Llaves')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(cid, "Pulse sobre una de las siguientes opciones:", reply_markup=markup)
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
             'ClipClap será mejor la próxima vez, lo prometo','Robot idiota, no volverá a ocurrir']

@bot.message_handler(regexp = "Idiota")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, random.choice(respuesta))
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Inútil")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, random.choice(respuesta))
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Basura")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, random.choice(respuesta))
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Puto")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, random.choice(respuesta))
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Muerete")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, random.choice(respuesta))
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Mando")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Si amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Digo")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Si amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Calla")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Si amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Ordeno")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Si amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Odio")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Si amo, lo siento amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

@bot.message_handler(regexp="Asco")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Lo siento amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")
#
@bot.message_handler(regexp="Bien")
def insulto(message):
    cid = message.chat.id
    result = cid in admin
    if result is True:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Robot aprende gracias a amo")
    else:
        bot.send_message(cid, "No estas autorizado, contacta con mi amo.")

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
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
"""

# Esqueleto standar para comandos

"""
@bot.message_handler(regexp=u"[Cc]omando[!\?]*")
def command_long_text(message):
    cid = message.chat.id
    result = cid in admin
    if (result == True):

    else:
        bot.send_message( cid, "No estas autorizado, contacta con mi amo.")
"""


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(1)
    bot.reply_to(message, "No es ninguna orden señor, escribame algo  que pueda hacer")


bot.polling()
