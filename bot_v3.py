import subprocess
import telebot
import time
import os
import emoji
import re
from telebot import types

line_name_01 = "01_Сокольническая"
line_name_02 = "02_Замоскворецкая"
line_name_03 = "03_Арбатско-Покровская"
line_name_04 = "04_Филёвская"
line_name_05 = "05_Кольцевая"
line_name_06 = "06_Калужско-Рижская"
line_name_07 = "07_Таганско-Краснопресненская"
line_name_08 = "08_Калининская"
line_name_09 = "09_Серпуховско-Тимирязевская"
line_name_10 = "10_Люблинская"
line_name_11 = "11_Каховская"
line_name_12 = "12_Бутовская"

#Объявляем ID бота
bot = telebot.TeleBot("xx")

#Инициируем инлайн клавиатуру
@bot.message_handler(commands = ['start'])
def inline_kb(message):
    markup = types.InlineKeyboardMarkup(row_width = 1)
    off_button = types.InlineKeyboardButton(text = "Выключить сервера", callback_data = "off")
    ping_button = types.InlineKeyboardButton(text = "Проверить сервера", callback_data = "ping")
    status_button = types.InlineKeyboardButton(text = "Проверить сервер на ошибки", callback_data = "status")
    bye_button = types.InlineKeyboardButton(text = "Остановить бота", callback_data = "bye")
    markup.add(off_button, ping_button, status_button, bye_button)
    bot.send_message(message.chat.id, "Что... Хозяин... Ннадо?? ", reply_markup = markup)
    
#Логика работы клавиатуры
@bot.callback_query_handler(func = lambda call:True)
def callback_inline_main(call):

    if call.message:
        if call.data == "mainmenu":
            markup_back = types.InlineKeyboardMarkup(row_width=1)
            off_button = types.InlineKeyboardButton(text="Выключить сервера", callback_data="off")
            ping_button = types.InlineKeyboardButton(text="Пингануть сервера", callback_data="ping")
            status_button = types.InlineKeyboardButton(text="Ошибки серверов", callback_data="status")
            bye_button = types.InlineKeyboardButton(text="Остановить бота", callback_data="bye")
            markup_back.add(off_button, ping_button, status_button, bye_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите действие: ",reply_markup=markup_back)
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
        elif call.data == "mainlines":
            markup_lines = types.InlineKeyboardMarkup(row_width=3)
            line_01 = types.InlineKeyboardButton(text=line_name_01, callback_data="line_01")
            line_02 = types.InlineKeyboardButton(text=line_name_02, callback_data="line_02")
            line_03 = types.InlineKeyboardButton(text=line_name_03, callback_data="line_03")
            line_04 = types.InlineKeyboardButton(text=line_name_04, callback_data="line_04")
            line_05 = types.InlineKeyboardButton(text=line_name_05, callback_data="line_05")
            line_06 = types.InlineKeyboardButton(text=line_name_06, callback_data="line_06")
            line_07 = types.InlineKeyboardButton(text=line_name_07, callback_data="line_07")
            line_08 = types.InlineKeyboardButton(text=line_name_08, callback_data="line_08")
            line_09 = types.InlineKeyboardButton(text=line_name_09, callback_data="line_09")
            line_10 = types.InlineKeyboardButton(text=line_name_10, callback_data="line_10")
            line_11 = types.InlineKeyboardButton(text=line_name_11, callback_data="line_11")
            line_12 = types.InlineKeyboardButton(text=line_name_12, callback_data="line_12")
            backbutton = types.InlineKeyboardButton(text="🔙 в меню", callback_data="mainmenu")
            markup_lines.add(line_01,line_02,line_03,line_04,line_05,line_06,line_07,line_08,line_09,line_10,line_11,line_12,backbutton)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите линию ММ: ",reply_markup=markup_lines)
#            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)

 #Логика работы кнопки Выключения       
        elif call.data == "off":
            keyboard_off = types.InlineKeyboardMarkup(row_width=2)
            chooseline = types.InlineKeyboardButton(text="Выберите линию", callback_data="mainlines")
            backbutton = types.InlineKeyboardButton(text="🔙 К меню", callback_data="mainmenu")            
            keyboard_off.add(chooseline, backbutton)
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Где ☣выключить☣ сервера? ", reply_markup=keyboard_off)
#            bot.register_next_step_handler(msg, station_name_off)
            
 #Логика работы кнопки Cтатуса       
        elif call.data == "status":
            keyboard_status = types.InlineKeyboardMarkup(row_width=2)
            chooseline = types.InlineKeyboardButton(text="Выберите линию", callback_data="mainlines")
            backbutton = types.InlineKeyboardButton(text="🔙 К меню", callback_data="mainmenu")            
            keyboard_status.add(chooseline, backbutton)
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Где проверить здоровье сервера? ", reply_markup=keyboard_status)
#            bot.register_next_step_handler(msg, station_name_status)
            
#Логика работы кнопки пинг        
        elif call.data == "ping":
            keyboard_ping = types.InlineKeyboardMarkup(row_width=2)
            chooseline = types.InlineKeyboardButton(text="Выберите линию", callback_data="mainlines")
            backbutton = types.InlineKeyboardButton(text="🔙 К меню", callback_data="mainmenu")           
            keyboard_ping.add(chooseline, backbutton)
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Где ПИНГАНУТЬ сервера? ", reply_markup=keyboard_ping)
#            bot.register_next_step_handler(msg, station_name_ping)
            
#Логика работы кнопки пока
        elif call.data == "bye":
           bot.send_message(call.message.chat.id, "Удачи, друг!")
           bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)


        elif call.data == "line_01":
            markup_line_01 = types.InlineKeyboardMarkup(row_width = 2)
            line_01_station_01 = types.InlineKeyboardButton(text="01_Бульвар Рокоссовского", callback_data="line_01_station_01")
            line_01_station_02 = types.InlineKeyboardButton(text="02_Черкизовская", callback_data="line_01_station_02")
            line_01_station_03 = types.InlineKeyboardButton(text="03_Преображенская площадь", callback_data="line_01_station_03")
            line_01_station_04 = types.InlineKeyboardButton(text="04_Сокольники", callback_data="line_01_station_04")
            line_01_station_05 = types.InlineKeyboardButton(text="05_Красносельская", callback_data="line_01_station_05")
            line_01_station_06 = types.InlineKeyboardButton(text="06_Комсомольская", callback_data="line_01_station_06")
            line_01_station_07 = types.InlineKeyboardButton(text="07_Красные ворота", callback_data="line_01_station_07")
            line_01_station_08 = types.InlineKeyboardButton(text="08_Чистые пруды", callback_data="line_01_station_08")
            line_01_station_09 = types.InlineKeyboardButton(text="09_Лубянка", callback_data="line_01_station_09")
            line_01_station_10 = types.InlineKeyboardButton(text="10_Охотный ряд", callback_data="line_01_station_10")
            line_01_station_11 = types.InlineKeyboardButton(text="11_Библиотека Ленина", callback_data="line_01_station_11")
            line_01_station_12 = types.InlineKeyboardButton(text="12_Кропоткинская", callback_data="line_01_station_12")
            line_01_station_13 = types.InlineKeyboardButton(text="13_Парк Культуры", callback_data="line_01_station_13")
            line_01_station_14 = types.InlineKeyboardButton(text="14_Фрунзенская", callback_data="line_01_station_14")
            line_01_station_15 = types.InlineKeyboardButton(text="15_Спортивная", callback_data="line_01_station_15")
            line_01_station_16 = types.InlineKeyboardButton(text="16_Воробьевы горы", callback_data="line_01_station_16")
            line_01_station_17 = types.InlineKeyboardButton(text="17_Университет", callback_data="line_01_station_17")
            line_01_station_18 = types.InlineKeyboardButton(text="18_Проспект Вернадского", callback_data="line_01_station_18")
            line_01_station_19 = types.InlineKeyboardButton(text="19_Юго-Западная", callback_data="line_01_station_19")
            line_01_station_20 = types.InlineKeyboardButton(text="20_Тропарёво", callback_data="line_01_station_20")
            line_01_station_21 = types.InlineKeyboardButton(text="21_Румянцево", callback_data="line_01_station_21")
            line_01_station_22 = types.InlineKeyboardButton(text="22_Саларьево", callback_data="line_01_station_22")
            back_to_lines = types.InlineKeyboardButton(text="🔙 К выбору линии", callback_data="mainlines")
            markup_line_01.add(line_01_station_01, back_to_lines)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите Станцию ММ: ",reply_markup=markup_line_01)

        elif call.data == "line_01_station_01":
        	print (callback_data)
        	bot.send_message(call.message.chat.id, callback_data)
#        	bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)




            
                        





















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
      ansible_station = ansible_station.replace('unreachable=1', 'IMM2 доступен ' + "❌").replace('unreachable=0', "")
      try:
         bot.reply_to(message, ansible_station)
      except:
         bot.reply_to(message, "Ты что творишь?? Нормальное название станции Введи!\n\n/start")
         keyboard = types.InlineKeyboardMarkup()
         backbutton = types.InlineKeyboardButton(text="🔙", callback_data="mainmenu")
         keyboard.add(backbutton)
         bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Возврат в главное меню",reply_markup=keyboard)
         
#Логика работы функции проверки статуса  
def station_name_status(message):
      bot.send_message(message.chat.id, "Сейчас проверим здоровье серверов!\n\nЗапущена магия статуса, ожидайте... "+ "🧙")
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + '_IPMI /etc/ansible/playbooks/ping.yaml', capture_output=True, shell=True, encoding="utf-8").stdout
      ansible_station = ansible_station[ansible_station.find('PLAY RECAP'):]
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.188\b', 'Сервер 1', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.189\b', 'Сервер 2', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.190\b', 'Сервер 3', ansible_station)
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
            
