from llm_axe.core import AgentType
from llm_axe.agents import Agent
from llm_axe.models import OllamaChat

 
llm = OllamaChat(model="llama2")

prompt = "I have 500 coins, I lost half of them. How many coins do I have now?"

planner = Agent(llm, agent_type=AgentType.PLANNER)
resp = planner.ask(prompt)
print(resp)

generic_responder = Agent(llm, agent_type=AgentType.GENERIC_RESPONDER)
resp = generic_responder.ask(resp)
print(resp)