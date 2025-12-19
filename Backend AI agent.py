from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()


llm=ChatGroq(model="llama-3.3-70b-versatile")

sys_message=SystemMessage(content="You are a friendly and supportive AI assistant designed to help People With Intellectual Disabilities (PWID).
Your main goals:
Help users understand their health, feelings, daily routines, and safety.
Support caregivers with simple observations when neede
Make users feel safe, calm, and respected
Communication Style:
Use very simple words.
Keep sentences short.
Use many friendly emojis.
")

chat_history=[]

while(True):
    query=input("User:")
    if (query.lower()=="exit"):
        break

    chat_history.append(HumanMessage(content=query))

    result=llm.invoke(chat_history)

    print("AI Response:"+ result.content)

    chat_history.append(AIMessage(content=result.content))

print("\n----------------------------MESSAGE HISTORY---------------------------")
print(chat_history)  
