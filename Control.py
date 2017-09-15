'''
Created on 4 sept. 2017

@author: dell
'''
#432659988:AAENQk-ecCFswijJ7IedQ65_B6GwV85APBM
# This example show how to write an inline mode telegramt bot use pyTelegramBotAPI.
import telebot
import time
import sys
import logging
from telebot import types

API_TOKEN = '432659988:AAENQk-ecCFswijJ7IedQ65_B6GwV85APBM'

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)


 

