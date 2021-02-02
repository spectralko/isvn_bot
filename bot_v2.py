import subprocess
import telebot
import time
import os
import emoji
import re
from telebot import types
#Объявляем ID бота
bot = telebot.TeleBot("1080220803:AAF9okmySN38daiPtLl8G14srVcknvCqKW4")

#Инициируем инлайн клавиатуру
@bot.message_handler(commands=['start'])
def inline_kb(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    off_button = types.InlineKeyboardButton(text="Выключить сервера", callback_data="off")
    ping_button = types.InlineKeyboardButton(text="Проверить сервера", callback_data="ping")
    bye_button = types.InlineKeyboardButton(text="Остановить бота", callback_data="bye")
    line_01_button = types.InlineKeyboardButton(text="01_Сокольническая", callback_data="line_01")
    line_02_button = types.InlineKeyboardButton(text="02_Замоскворецкая", callback_data="line_02")
    line_03_button = types.InlineKeyboardButton(text="03_Арбатско-Покровская", callback_data="line_03")
    line_04_button = types.InlineKeyboardButton(text="04_Филевская", callback_data="line_04")
    line_05_button = types.InlineKeyboardButton(text="05_Кольцевая", callback_data="line_05")
    line_06_button = types.InlineKeyboardButton(text="06_Калужско-Рижская", callback_data="line_06")
    line_07_button = types.InlineKeyboardButton(text="07_Таганско-Краспропесненская", callback_data="line_07")
    line_08_button = types.InlineKeyboardButton(text="08_Калининская", callback_data="line_08")
    line_8a_button = types.InlineKeyboardButton(text="8а_", callback_data="line_8a")
    line_09_button = types.InlineKeyboardButton(text="09_Серпуховско-Тимирязевская", callback_data="line_09")
    line_10_button = types.InlineKeyboardButton(text="10_Люблинская", callback_data="line_10")
    line_11_button = types.InlineKeyboardButton(text="11_Каховская", callback_data="line_11")
    line_12_button = types.InlineKeyboardButton(text="12_Бутовская", callback_data="line_12")
#    line_14_button = types.InlineKeyboardButton(text="", callback_data="line_14")
    markup.add(off_button, ping_button, bye_button)
    bot.send_message(message.chat.id, "Что... Хозяин... Ннадо?? ", reply_markup=markup)
#Логика работы клавиатуры
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.message:
        if call.data == "mainmenu":
            markup_back = types.InlineKeyboardMarkup(row_width=2)
            off_button = types.InlineKeyboardButton(text="Выключить сервера", callback_data="off")
            ping_button = types.InlineKeyboardButton(text="Проверить сервера", callback_data="ping")
            bye_button = types.InlineKeyboardButton(text="Остановить бота", callback_data="bye")
            markup_back.add(off_button, ping_button, bye_button)
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите действие",reply_markup=markup_back)
 #Логика работы кнопки Выключения       
        elif call.data == "off":
            keyboard = types.InlineKeyboardMarkup()
            backbutton = types.InlineKeyboardButton(text="🔙", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Возврат в главное меню",reply_markup=keyboard)
            msg = bot.send_message(call.message.chat.id, "На какой станции ☣выключить☣ сервера?: ")
            bot.register_next_step_handler(msg, station_name_off)
#Логика работы кнопки пинг        
        elif call.data == "ping":
            msg = bot.send_message(call.message.chat.id, "Введите назнание станции для проверки доступности: ")
            bot.register_next_step_handler(msg, station_name_ping)
            keyboard = types.InlineKeyboardMarkup()
            backbutton = types.InlineKeyboardButton(text="🔙", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Возврат в главное меню",reply_markup=keyboard)
#Логика работы кнопки пока
        elif call.data == "bye":
            bot.send_message(call.message.chat.id, "Удачи друг!")

def callback_inline_lines(call):
    if call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
    elif call.data == "line_01":
        
#Логика работы функции выключения
def station_name_off(message):
      bot.send_message(message.chat.id, "⚠Сейчас будет происходить выключение серверов!⚠\n\nЗапущена магия выключения, ожидайте... "+ "🧙")
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + '_IPMI /etc/ansible/playbooks/ping.yaml', capture_output=True, shell=True, encoding="utf-8").stdout
      ansible_station = ansible_station[ansible_station.find('PLAY RECAP'):]
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.188\b', 'Сервер 1', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.189\b', 'Сервер 2', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.190\b', 'Сервер 3', ansible_station)
      ansible_station = ansible_station.replace('skipped=0','').replace('rescued=0','').replace('ignored=0','').replace('*','').replace('changed=0', '').replace('failed=0', '')
      ansible_station = ansible_station.replace('PLAY RECAP','Отчет о выключении серверов на станции: ' + message.text)
      ansible_station = ansible_station.replace('ok=1', 'Выключился? ' + "✅").replace('ok=0', 'Выключился? ' + "❌")
      ansible_station = ansible_station.replace('unreachable=1', 'IMM2 доступен ' + "❌").replace('unreachable=0', '')

      try:
         bot.reply_to(message, ansible_station)
      except:
         bot.reply_to(message, "Ты что творишь?? Нормальное название станции Введи!\n\n/start")
         keyboard = types.InlineKeyboardMarkup()
         backbutton = types.InlineKeyboardButton(text="🔙", callback_data="mainmenu")
         keyboard.add(backbutton)
         bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Возврат в главное меню",reply_markup=keyboard)
#Логика работы функции пинг         
def station_name_ping(message):
      bot.send_message(message.chat.id, "Сейчас проверим пинг до серверов!\n\nЗапущена магия пинга, ожидайте... "+ "🧙")
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + '_IPMI /etc/ansible/playbooks/ping.yaml', capture_output=True, shell=True, encoding="utf-8").stdout
      ansible_station = ansible_station[ansible_station.find('PLAY RECAP'):]
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.1\b', 'Сервер 1', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.2\b', 'Сервер 2', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.3\b', 'Сервер 3', ansible_station)
      ansible_station = ansible_station.replace('skipped=0','').replace('rescued=0','').replace('ignored=0','').replace('*','').replace('changed=0', '').replace('failed=0', '')
      ansible_station = ansible_station.replace('PLAY RECAP','Отчет о выключении серверов на станции: ' + message.text)
      ansible_station = ansible_station.replace('ok=1', 'Выключился? ' + "✅").replace('ok=0', 'Выключился? ' + "❌")
      ansible_station = ansible_station.replace('unreachable=1', 'IMM2 доступен ' + "❌").replace('unreachable=0', "✅")

      try:
         bot.reply_to(message, ansible_station)
      except:
         bot.reply_to(message, "Ты что творишь?? Нормальное название станции Введи!\n\n/start")
         keyboard = types.InlineKeyboardMarkup()
         backbutton = types.InlineKeyboardButton(text="🔙", callback_data="mainmenu")
         keyboard.add(backbutton)
         bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Возврат в главное меню",reply_markup=keyboard)

#Чтобы не падал
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop = True)
        except:
            time.sleep(10)
