# https://www.youtube.com/watch?v=nXynNB6XzAM&t=40s
# https://python.langchain.com/docs/introduction/
# pip install -qU "langchain[openai]"
# pip install -U langchain langchain-community
# pip install dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  # Importando LLMChain para encadear a execução corretamente
from dotenv import load_dotenv

load_dotenv()

def generate_cat_name(animal_type):
    llm = ChatOpenAI(temperature=0.6)

    prompt_animal_name = PromptTemplate(
        input_variables=['animal_type'],
        template="Você tem um {animal_type} filhote e gostaria de dar um nome diferente para ele. Informe-me uma lista de 5 nomes possíveis."
    )
    
    # Criando a cadeia corretamente
    chain = LLMChain(llm=llm, prompt=prompt_animal_name)

    response = chain.invoke(animal_type)  # Executa a cadeia corretamente
    return response["text"]

if __name__ == "__main__":
    print(generate_cat_name("gatinho branco"))
