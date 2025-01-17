from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

information = """
    Name: John Doe
    Position: Software Engineer
    Company: Google
    Education: Bachelor of Science in Computer Science
    Skills: Python, JavaScript, React, Node.js
"""

if __name__ == "__main__":
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    llm_openai = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain_openai = summary_prompt_template | llm_openai | StrOutputParser()
    res_openai = chain_openai.invoke({"information": information})
    
    print(res_openai)
    
    # llm_ollama = ChatOllama(model="llama3.2")
    # chain_ollama = summary_prompt_template | llm_ollama | StrOutputParser()
    # res_ollama = chain_ollama.invoke({"information": information})
    
    # print(res_ollama)
