from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.prompts import load_prompt

from agent.config import get_llm_gemini, get_llm_openrouter
from agent.config.settings import LLM_PROVIDER, OPENROUTER_MODEL


class InspectorAgent:
    def __init__(self, temperatura:float = 0):
        if LLM_PROVIDER == "GEMINI":
            self.llm = get_llm_gemini(temperature=temperatura)
        else:
            self.llm = get_llm_openrouter(model=OPENROUTER_MODEL, temperature=temperatura)

        prompt = load_prompt("resources/prompts/inspector.yaml")
        self.agent = create_agent(
            model = self.llm,
            #tools=[],
            system_prompt=prompt.format(),
        )


    def agent_call(self, text: str) -> str:

        result = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": text
                    }
                ],
            },
        )

        final_text = self._extract_text(result["messages"][-1])

        final_text = (
            final_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return final_text
    
    @staticmethod
    def _extract_text(message) -> str:

        content = message.content

        if isinstance(content, str):
            return content

        if isinstance(content, list):

            texts = []

            for block in content:
                if isinstance(block, dict):
                    if block.get("type") == "text":
                        texts.append(
                            block.get("text", "")
                        )
            return "\n".join(texts)

        return str(content)

