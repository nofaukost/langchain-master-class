from dotenv import load_dotenv

load_dotenv()

from tools.tools import get_profile_url_tavily

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

def linkedin_lookup_agent(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page. Your answer should contain only a URL"""
    
    prompt_template = PromptTemplate(input_variables=["name_of_person"], template=template)
    
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func=get_profile_url_tavily,
            description="useful when you need to get the LinkedIn url of a person"
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools_for_agent, prompt=react_prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    
    linkedin_profile_url = result["output"]
    
    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_profile_url = linkedin_lookup_agent("Eden Marco")
    print(linkedin_profile_url)
