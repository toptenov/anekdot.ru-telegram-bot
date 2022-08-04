import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'http://www.anekdot.ru/last/good/'
API_KEY = '5394247944:AAEmqAlE_FGGAv_ovvWEmOx3VVWfIrGoAUc'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [a.text for a in jokes]

jokes = parser(URL)
random.shuffle(jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Чтобы получить анекдот введите любую цифру:')

@bot.message_handler(content_types=['text'])
def send_jokes(message):
    if message.text.lower() in '1234567890':
        bot.send_message(message.chat.id, jokes[0])
        del jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру:')

bot.polling()
