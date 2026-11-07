import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(override=True)

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Display available models
print("\n===== AVAILABLE GEMINI MODELS =====\n")

for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)