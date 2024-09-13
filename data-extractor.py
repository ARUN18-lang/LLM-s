from llm_axe.core import read_pdf, safe_read_json
from llm_axe.models import OllamaChat
from llm_axe.agents import DataExtractor

llm = OllamaChat(model="llama3:instruct")
info = read_pdf("../example.pdf")

data = DataExtractor(llm, reply_as_json = True, temperature=0.8)

res = data.ask(info, ["name", "email", "phone", "address"])

json = safe_read_json(res)
print(json)