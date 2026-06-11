from agent.inspector import InspectorAgent
from bot.bot import bot_telegram


inspector_agent = InspectorAgent()

@bot_telegram.message_handler(func=lambda message: True)
def receive_message(message):
    msg_user = message.text
    print(f"Mensagem recebido: '{msg_user}'")

    agent_result = inspector_agent.agent_call(text=msg_user)
    print(agent_result)

    return msg_user
