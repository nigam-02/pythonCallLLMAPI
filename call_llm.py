import os
from dotenv import load_dotenv
from google import genai

#load api key from .env
load_dotenv()

#create the client using google gen ai library
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#call a google ai model
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain what is calling LLM through API in 2 sentences."
)

print(interaction.output_text)