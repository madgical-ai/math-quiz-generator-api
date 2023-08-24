from lcserve import serving
import os
from langchain.llms import AzureOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.callbacks import get_openai_callback
from helicone.openai_proxy import openai

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGCHAIN_SESSION"] = "trace_question_generation"

@serving
def ask(subjects: str, operations: str, input1: str, input2: str, questions_on: str) -> dict:
    with get_openai_callback() as cb:
        
        llm = AzureOpenAI(
                temperature=0,
                engine="GPT4-8K",
                model_name="gpt-4",
                headers={
                "Helicone-Auth": "Bearer sk-helicone-d62snei-jmsewli-qa53kaq-f2rpsci",
                    "Helicone-User-Id": "manoj21-07-2023"
                }
            )
        
        total_token = 0
        total_cost = 0
        
        subject = subjects
        operation = operations
        number1 = input1
        number2 = input2
        question_on = questions_on

        question_prompt = f"""you have to generate a simple math question in English for the given data:\n
        Subject: {subject}, Operation: {operation}, Input1: {number1}, Input2: {number2}, Question_on: {question_on}.
        """

        question = llm(question_prompt)  # Generate the question here
        
        solution_prompt = f"""you have a math question given in between triple backticks. you have to solve the question and give only the final answer according to a math grade 3 teacher:
```{question}```
"""

        explanation_prompt = f"""You are a math teacher of grade 3. You have a math question given in between triple backticks. You have to solve the question for a 3rd standard student.
```{question}```
"""

        solution = llm(solution_prompt)
        explanation = llm(explanation_prompt)

        total_token = total_token + cb.total_tokens
        total_cost = total_cost + cb.total_cost
        print(cb)
        print("Total Token ", total_token)
        print("Total Cost ", total_cost)
        print(question)
        print(solution)
        print(explanation)

        return {"question": question, "solution": solution, "explanation": explanation, "total_token": cb.total_tokens, "total_cost": cb.total_cost}
