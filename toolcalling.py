from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from rich import print
load_dotenv()

@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

#tool binding
llm_with_tool = llm.bind_tools([get_text_length])

message = []
prompt = input("You: ")
query = HumanMessage(prompt)
message.append(query)

result = llm_with_tool.invoke(message)

message.append(result)

if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)
   

result = llm_with_tool.invoke(message)
final_text = result.content

if isinstance(final_text, list):
    final_text = "".join(
        part.get("text", str(part))
        for part in final_text
        if isinstance(part, dict)
    )
elif not isinstance(final_text, str):
    final_text = str(final_text)

print(final_text)