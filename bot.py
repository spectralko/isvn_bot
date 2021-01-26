import subprocess
import telebot
import time
import os

bot = telebot.TeleBot("1080220803:AAF9okmySN38daiPtLl8G14srVcknvCqKW4")


@bot.message_handler(commands=['off'])
def server_power_off(message):
	msg = bot.send_message(message.chat.id, "Введите назнание станции согласно списка: ")
	bot.register_next_step_handler(msg, station_name_off)
	
@bot.message_handler(commands=['ping'])
def server_power_off(message):
	msg = bot.send_message(message.chat.id, "Выедите назнание станции согласно списка: ")
	bot.register_next_step_handler(msg, station_name_ping)


def station_name_off(message):
      bot.send_message(message.chat.id, "Сервера выключаются, ожидайте...")
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + ' /etc/ansible/playbooks/ping.yaml', capture_output=True, shell=True, encoding="utf-8")
      try:
         bot.reply_to(message, ansible_station)
      except:
         bot.reply_to(message, "Ты что творишь?? Нормальное название станции Введи!")
         
def station_name_ping(message):
      bot.send_message(message.chat.id, "Проверяю сервера на доступность, ожидайте...")
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text + ' /etc/ansible/playbooks/ipmi_server_off.yaml', capture_output=True, shell=True, encoding="utf-8")
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
   
