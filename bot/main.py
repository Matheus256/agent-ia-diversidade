from bot import bot

def main():
    """
    Função principal que roda o bot
    """

    try:
        print("Iniciando bot! 🤖")
        bot.infinity_polling()
    except Exception as e:
        print(f"Erro no bot: {e}")


if "__main__" == __name__:
    main()