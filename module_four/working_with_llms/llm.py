from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("gemini_key")

client = genai.Client(api_key=api_key)

def chat_with_gemini():
  try:
    while True: 
      user_prompt = input("Chat with Gemini: ")
      if (user_prompt == "quit"):
        break
      response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=[user_prompt]
      )

      # print(response.text)
      for chunk in response:
        print(chunk.text, end="")
  except ValueError as e:
    print(e)

chat_with_gemini()