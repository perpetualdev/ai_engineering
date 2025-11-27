from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
import uvicorn
from google import genai
from google.genai import types
# from PIL import Image
import httpx
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

api_key = os.getenv("gemini_key")

client = genai.Client(api_key=api_key)

app = FastAPI(title="Chat With Gemini", version="1.0.0")

origins = [
  "http://localhost",
  "http://localhost:8080",
  "http://127.0.0.1:5500",
  "http://127.0.0.1:8000",
  "*" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class GeminiChat(BaseModel):
  prompt: str = Field(..., example="How does AI work?")
  selection: str = Field(..., example="text")
  persona: str | None = Field(default=None)
  # video_url: str | None = Field(default=None)
  doc_url: str | None = Field(default=None)
  # audio_url: str | None = Field(default=None)

@app.post("/chat")
def chatWithGemini(data: GeminiChat):
  model="gemini-2.5-flash"
  # prompt, data.selection, persona, video_url, doc_url, audio_url = data
  # print(data.selection)
  try:
    if data.selection == "text":
      response = client.models.generate_content_stream(
        model=model,
        contents=[data.prompt]
      )

      return {
        "response": response.text
      }
    elif data.selection == "persona":
      response = client.models.generate_content(
        model=model,
        config=types.GenerateContentConfig(
            system_instruction=data.persona),
        contents=data.prompt
      )

      return {
        "response": response.text
      }
    # elif data.selection == "image":
    #   prompt = (data.prompt)

    #   response = client.models.generate_content(
    #     model="gemini-2.5-flash-image",
    #     contents=[data.prompt],
    #   )

    #   for part in response.parts:
    #     if part.text is not None:
    #         print(part.text)
    #     elif part.inline_data is not None:
    #         image = part.as_image()
    #         image.save("generated_image.png")
    elif data.selection == "video":
      video_file_name = "video.mp4"
      video_bytes = open(video_file_name, 'rb').read()
      response = client.models.generate_content(
        model='models/gemini-2.5-flash',
        contents=types.Content(
          parts=[
            types.Part(
              inline_data=types.Blob(data=video_bytes, mime_type="video/mp4")
            ),
            types.Part(text=data.prompt)
          ]
        )
      )
      return {
        "response": response.text
      }
    elif data.selection == "docs":
      doc_data = httpx.get(data.doc_url).content

      prompt = [data.prompt]
      response = client.models.generate_content(
        model=model,
        contents=[
          types.Part.from_bytes(
            data=doc_data,
            mime_type='application/pdf',
          ),
          prompt])
      return {
        "response": response.text
      }
    elif data.selection == "audio":
      myfile = client.files.upload(file="voice-sample.mp3")
      prompt = data.prompt

      response = client.models.generate_content(
        model=model,
        contents=[data.prompt, myfile]
      )

      return {
        "response": response.text
      }
    elif data.selection == "code":
      response = client.models.generate_content(
        model=model,
        contents=data.prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(code_execution=types.ToolCodeExecution)]
        ),
      )
      full_response = ""
      
      for part in response.candidates[0].content.parts:
          if part.text is not None:
              full_response += part.text + "\n"
          if part.executable_code is not None:
              # Format the code nicely using markdown code block
              full_response += f"\n```python\n{part.executable_code.code}\n```\n"
          if part.code_execution_result is not None:
              # Include the calculation output
              full_response += f"\n**Calculation Output:**\n```\n{part.code_execution_result.output}\n```\n"

      return {
        "response": full_response
      }
    else:
      raise ValueError("No selection made")
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=8080)
