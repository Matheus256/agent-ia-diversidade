from agent.inspector import InspectorAgent
from bot.bot import bot_telegram
from shared.logger import configurar_logger

inspector_agent = InspectorAgent()
logger = configurar_logger()

@bot_telegram.message_handler(func=lambda message: True)
def receive_message(message):
    msg_user = message.text
    print(f"Mensagem recebida: '{msg_user}'")
    logger.info(f"Mensagem recebida: \n _'{msg_user}'_")

    agent_result = inspector_agent.agent_call(text=msg_user)
    print(agent_result)
    logger.info(f"Resultado do agente: \n {agent_result}")

    return msg_user
