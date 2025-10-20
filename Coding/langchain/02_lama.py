from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Prompt template for concise, step-by-step coding answers
template = """You are a highly skilled programming assistant.
You provide concise, precise, and step-by-step solutions for complex coding tasks.
Use clear explanations and focus on resolution, avoid unnecessary colloquial language.

Question: {question}
Answer:"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="gemma:2b")

# Create a RunnableSequence: prompt | model
chain = prompt | model

print("💡 Type 'exit' to quit the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    # Use invoke() instead of run() to avoid warnings
    msg = chain.invoke({"question": user_input})
    print(f"Ollama: {msg}\n")
