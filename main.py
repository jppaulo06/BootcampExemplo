from dotenv import load_dotenv
import maritalk
import os

load_dotenv()
chave = os.getenv("CHAVE")

model = maritalk.MariTalk(key=chave, model="sabia-3")
req = model.generate("Estou usando o sabiá num curso de desenvolvimento de chatbots com API e IA. Se apresente e recepcione os estudantes que estão te conhecendo hoje.")
print(req['answer'])
