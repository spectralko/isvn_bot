import subprocess
import telebot
import time
import os
import emoji
import re
from telebot import types

bot = telebot.TeleBot("xx")


@bot.message_handler(commands=['off'])
def server_power_off(message):
	msg = bot.send_message(message.chat.id, "Введите назнание станции согласно списка: ")
	bot.register_next_step_handler(msg, station_name_off)
	
@bot.message_handler(commands=['ping'])
def server_power_off(message):
	msg = bot.send_message(message.chat.id, "Введите назнание станции согласно списка: ")
	bot.register_next_step_handler(msg, station_name_ping)


def station_name_off(message):
      bot.send_message(message.chat.id, "Сервера выключаются, ожидайте... "+ emoji.emojize(':timer_clock:'))
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + '_IPMI /etc/ansible/playbooks/ping.yaml', capture_output=True, shell=True, encoding="utf-8").stdout
      ansible_station = ansible_station[ansible_station.find('PLAY RECAP'):]
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.188\b', 'Сервер 1', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.189\b', 'Сервер 2', ansible_station)
      ansible_station = re.sub(r'\b\d*\.\d*\.\d*\.190\b', 'Сервер 3', ansible_station)
      ansible_station = ansible_station.replace('skipped=0','').replace('rescued=0','').replace('ignored=0','').replace('*','').replace('changed=0', '').replace('failed=0', '')
      ansible_station = ansible_station.replace('PLAY RECAP','Отчет о выключении серверов на станции: ' + message.text)
      ansible_station = ansible_station.replace('ok=1', 'Выключился? ' + emoji.emojize(':green_circle:')).replace('ok=0', 'Выключился? ' + emoji.emojize(':red_circle:'))
      ansible_station = ansible_station.replace('unreachable=1', 'IMM2 доступен =' + emoji.emojize(':red_circle:')).replace('unreachable=0', 'IMM2 доступен ' + emoji.emojize(':green_circle:'))

      try:
         bot.reply_to(message, ansible_station)
      except:
         bot.reply_to(message, "Ты что творишь?? Нормальное название станции Введи!")
         
def station_name_ping(message):
      bot.send_message(message.chat.id, "Проверяю сервера на доступность, ожидайте... ")
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + ' /etc/ansible/playbooks/ipmi_server_off.yaml', capture_output=True, shell=True, encoding="utf-8").stdout
      ansible_station = ansible_station[ansible_station.find('PLAY RECAP'):]

      try:
         bot.reply_to(message, ansible_station)
      except:
         bot.reply_to(message, "Ты что творишь?? Нормальное название станции Введи!")










#Чтобы не падал
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop = True)
        except:
            time.sleep(10)
