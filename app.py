import os
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import question_prompt_template, solution_prompt_template, explanation_prompt_template
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI")

os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]=os.getenv("langsmit")
os.environ["LANGSMITH_PROJECT"]="csv-extraction"


app = FastAPI()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

@app.post("/ask")
async def ask(subjects: str, operations: str, input1: str, input2: str, questions_on: str):
    question_prompt = question_prompt_template.format(subjects=subjects, operations=operations, input1 = input1, input2=input2, questions_on=questions_on)
    question = llm.invoke(question_prompt)
 
    solution_prompt = solution_prompt_template.format(question = question.content)
    solution = llm.invoke(solution_prompt)

    explanation_prompt = explanation_prompt_template.format(question = question.content)
    explanation = llm.invoke(explanation_prompt)
    
    return {
        "question": question.content,
        "solution": solution.content,
        "explanation": explanation.content,
    }

