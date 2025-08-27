from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrapping_linkedin_profile
from dotenv import load_dotenv

load_dotenv()
import os
key = os.environ['OPENROUTER_API_KEY']

if __name__ == '__main__':
    print("Hello Langchain")

    summary_template= """
        given the Linkedin information {information} about a person from I want you to create :
        1. a short summary
        2. two interestings facts about them

    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model="openai/gpt-oss-20b:free",api_key=key,base_url="https://openrouter.ai/api/v1")
    llm = ChatOllama(temperature=0, model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrapping_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/fabian-pappa-06198614a/")

    res = chain.invoke(input={"information":linkedin_data})
    print(f"RESPONSE----------- {res}")
