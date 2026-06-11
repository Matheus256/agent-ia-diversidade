from bot import bot

@bot.message_handler(func=lambda message: True)
def receive_message(message):

    msg_user = message.text
    print(msg_user)
    return msg_user
