from langchain_core.prompts import PromptTemplate

question_prompt_template = PromptTemplate.from_template("""Act as an engaging and student-friendly math tutor. Generate a simple math question in English based on the following parameters:

Subject: {subjects}
Operation: {operations}
First number: {input1}
Second number: {input2}
Focus of the question: {questions_on}
Ensure the question is clear, age-appropriate, and encourages curiosity while maintaining correct grammar.
""")

solution_prompt_template = PromptTemplate.from_template("""Act as a precise and reliable math solver. Solve the following math question and provide only the final answer, without any explanation:\n{question}""")

explanation_prompt_template = PromptTemplate.from_template("""Act as a patient and friendly Grade 3 math teacher. Solve the given math question in a way that a 3rd-grade student can easily understand. Use simple language and step-by-step reasoning.
{question}""")