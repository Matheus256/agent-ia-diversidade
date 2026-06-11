from bot.bot import bot_telegram


def main():
    """
    Função principal que roda o bot
    """

    try:
        print("Iniciando bot! 🤖")
        bot_telegram.infinity_polling()
    except Exception as e:
        print(f"Erro no bot: {e}")


if "__main__" == __name__:
    main()