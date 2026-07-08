from src.llm.groq_client import ask_llm

response = ask_llm(
    system_prompt="You are a helpful AI assistant.",
    user_prompt="Reply with exactly: Groq connection successful!"
)

print(response)