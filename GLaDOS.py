'''
Created on 4 sept. 2017

@author: dell
'''
#432659988:AAENQk-ecCFswijJ7IedQ65_B6GwV85APBM

import time
import telebot  
import os
from telebot import types

"""
Definicion de las variables locales y las contraseñas por usuario, quizás sería recomendable realizar una tupla
con el fin de automatizar el proceso de contraseñas pero habrá que darle una vuelta.
"""

#Token del bot 
bot = telebot.TeleBot("432659988:AAENQk-ecCFswijJ7IedQ65_B6GwV85APBM")

#Los que pueden usar el bot
admin1 = 000000000
admin2 = 000000000

#Su contraseña
PASSWORD1 = "ABC"      
PASSWORD2 = "123"

"""
Comienza el programa
"""

# Extracts the unique_code from the sent /start command.
def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

#if unique_code = ABC: # if the '/start' command contains a unique_code
@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id 
    unique_code = extract_unique_code(message.text)
    if unique_code == PASSWORD1:    
        global admin1
        admin1 = cid
        bot.send_message(message.chat.id, text="Bienvenido amo, estoy a su servicio.")
        bot.send_chat_action(cid, 'typing') # show the bot "typing" (max. 5 secs)
        time.sleep(2)
        bot.send_message(message.chat.id, """Para conocer las opciones disponibles dentro del sistema, por favor escriba *Ayuda*""", parse_mode="Markdown")
    elif unique_code == PASSWORD2:
        global admin2
        admin2 = cid
        bot.send_message(message.chat.id, text="Bienvenido amo, estoy a su servicio.")
        bot.send_chat_action(cid, 'typing') # show the bot "typing" (max. 5 secs)
        time.sleep(2)
        bot.send_message(message.chat.id, """Para conocer las opciones disponibles dentro del sistema, por favor escriba *Ayuda*""", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Contraseña *incorrecta* para mas informacion escriba */help*", parse_mode="Markdown")


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, "Bot esta protegido por contraseña, para conocerla contacte con el administrador")
    bot.send_message(message.chat.id, "Para acceder envía el comando */start* seguido de la contraseña.", parse_mode="Markdown")


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
    if (cid == admin1) or (cid == admin2):
        bot.send_message(cid, "Ejecutando: "+message.text[len("/comando"):])
        bot.send_chat_action(cid, 'typing') # show the bot "typing" (max. 5 secs)
        time.sleep(2)
        f = os.popen(message.text[len("/comando"):])
        result = f.read()
        bot.send_message(cid, "Resultado: "+result)
              
    else:

        bot.send_message( cid, u"""No estas autorizado, contacta con mi amo.""") 

 
 
@bot.message_handler(regexp=u"[Ff]oto[!\?]*")
def photo_me(message):
    cid = message.chat.id
    if (cid == admin1) or (cid == admin2):    
        photo = open("/home/dell/Imágenes/Webcam/2017-07-19-231950.jpg", 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, text="Fecha: " + time.strftime("%c")) 
 
    else:

        bot.send_message( cid,text= "No estas autorizado, contacta con mi amo.") 
 
@bot.message_handler(regexp=u"[Aa]yuda[!\?]*")
def comando_ayuda(message):
    cid = message.chat.id
    if (cid == admin1) or (cid == admin2):
        bot.send_message(message.chat.id, """*::Bienvenido a la ayuda::*""", parse_mode="Markdown")
        bot.send_message(message.chat.id, """Si desea recibir una *foto* escriba: *Foto*
Si desea las *llaves* puede controlar el *Drone*
Si desea activar el *Roomba* pulse *Roomba*
Si desea hacer *tal* escriba: *cual*""",parse_mode="Markdown")
        markup = types.ReplyKeyboardMarkup()
        itembtna = types.KeyboardButton('Foto')
        itembtnv = types.KeyboardButton('Roomba')
        itembtnc = types.KeyboardButton('Llaves')
        itembtnd = types.KeyboardButton('Movidas')
        itembtne = types.KeyboardButton('Llaves')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(cid, "Choose one letter:", reply_markup=markup)  
       
    
    else:

        bot.send_message( cid, u"""No estas autorizado, contacta con mi amo.""") 
 
 
    
# Esqueleto standar para comandos
"""
@bot.message_handler(regexp=u"[Cc]omando[!\?]*")
def command_long_text(message):

    cid = message.chat.id
    if (cid == admin1) or (cid == admin2):
        
        
    else:

        bot.send_message( cid, Text= "No estas autorizado, contacta con mi amo.")
"""    


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_chat_action(message.chat.id, 'typing') # show the bot "typing" (max. 5 secs)
    time.sleep(1)
    bot.reply_to(message, "No es ningua orden chato, vuelta a empezar")    



bot.polling()    
    
