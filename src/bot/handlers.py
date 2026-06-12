from agent.inspector import InspectorAgent
from bot.bot import bot_telegram
from shared.logger import configurar_logger

inspector_agent = InspectorAgent()
logger = configurar_logger()

@bot_telegram.message_handler(func=lambda message: True)
def receive_message(message):
    msg_user = message.text
    info = identificar_origem(message)
    print(f"Mensagem enviada: '{msg_user}'")
    logger.info(f"{info} \n")
    logger.info(f"Conteúdo da mensagem: \n _'{msg_user}'_ \n")

    agent_result = inspector_agent.agent_call(text=msg_user)
    print(agent_result)
    logger.info(f"Resultado do agente: \n {agent_result} \n")

    return msg_user

def identificar_origem(message):
    nome = message.from_user.first_name
    username = message.from_user.username if message.from_user.username else "Sem username"

    titulo_grupo = message.chat.title if message.chat.type != 'private' else "Conversa Privada"
    id_grupo = message.chat.id

    info = f"Usuário: {nome} (@{username})\nOrigem: {titulo_grupo} (ID: {id_grupo})"

    return info