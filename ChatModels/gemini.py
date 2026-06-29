import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set the environment variable (or load it from a .env file)
os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6ImpPodGXTxMbL178mTEZoeOgZsia48o6NIZs_DiUYKow"

# Initialize the model 
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Test the connection
response = llm.invoke("Hello, Gemini!")
print(response.content)
