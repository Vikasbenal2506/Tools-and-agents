from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# 1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Model
# model = ChatMistralAI(model="mistral-small-2506")
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# 3. Output Parser
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke("Machine Learning")
print(result)