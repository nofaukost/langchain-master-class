from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

from agents.linkedin_lookup import linkedin_lookup_agent
from output_parsers import summary_parser, Summary

from typing import Tuple

from dotenv import load_dotenv

def ice_breaker_with_name(name: str) -> Tuple[Summary, str]:
    linkedin_profile_url = linkedin_lookup_agent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, mock=True)
    
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        \n{format_instructions}
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )
    
    llm_openai = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # chain_openai = summary_prompt_template | llm_openai | StrOutputParser()
    chain_openai = summary_prompt_template | llm_openai | summary_parser
    res_openai: Summary = chain_openai.invoke({"information": linkedin_data})
    
    # llm_ollama = ChatOllama(model="llama3.2")
    # chain_ollama = summary_prompt_template | llm_ollama | StrOutputParser()
    # res_ollama = chain_ollama.invoke({"information": information})
    
    print(res_openai)
    
    return res_openai, linkedin_data.get("profile_pic_url")
    
if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker_with_name("Eden Marco")
    
    
