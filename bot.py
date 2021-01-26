import subprocess
import telebot
import time
import os

bot = telebot.TeleBot("1080220803:AAF9okmySN38daiPtLl8G14srVcknvCqKW4")





@bot.message_handler(content_types = ['text'])
def station_name(message):
      ansible_station = subprocess.run('ansible-playbook -l ' + message.text[1:] + ' /etc/ansible/playbooks/ping.yaml', capture_output=True, shell=True, encoding="utf-8").stdout.strip("\n*PLAY")
#      ansible_station = ansible_station
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
