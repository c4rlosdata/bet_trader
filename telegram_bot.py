import telebot
import logging

# Configurações do Telegram Bot
token = '5991206275:AAEmAMdY_7Ri6-n9CRyrTgEom3eo9rGKV-0'
chat_id = '-1001819887243'
bot = telebot.TeleBot(token)

def enviar_mensagem_telegram(mensagem):
    try:
        bot.send_message(chat_id, mensagem, disable_web_page_preview=True, parse_mode='HTML')
        logging.info("Mensagem enviada com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {e}")

