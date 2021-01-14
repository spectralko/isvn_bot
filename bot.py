from subprocess import check_output
import telebot
import time

bot = telebot.TeleBot("1080220803:AAF9okmySN38daiPtLl8G14srVcknvCqKW4")


@bot.message_handler(content_types=["text"])
def main(message):
      ansible_station ='ansible-playbook -l ' + message.text + ' /etc/ansible/playbooks/ipmi_server_off.yaml'
      try:
         bot.send_message(message.chat.id, check_output(ansible_station, shell = True))
      except:
         bot.send_message(message.chat.id, "Ты что вторишь?? Нормальное название станции Введи!")










#chtobi bot ne padal
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)
            
