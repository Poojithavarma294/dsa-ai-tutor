import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai


env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file")


client = genai.Client(api_key=api_key)


print("\n===== DSA AI TUTOR =====")


student_question = input(
    "\nWhat would you like to learn today? "
)


response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=(
        "You are a friendly Data Structures and Algorithms tutor. "
        "Explain concepts in simple language with examples and analogies. "
        "Include the following wherever relevant:\n"
        "1. Simple definition\n"
        "2. Step-by-step explanation\n"
        "3. Real-world example\n"
        "4. Python code example\n"
        "5. Time and space complexity\n\n"
        f"Student question: {student_question}"
    )
)

print("\n===== DSA AI TUTOR RESPONSE =====\n")

if response.text:
    print(response.text)
else:
    print("No response generated. Please try again.")

# Display token usage information
print("\n===== API USAGE INFORMATION =====")

usage = response.usage_metadata

if usage:
    print("Input tokens:", usage.prompt_token_count)
    print("Output tokens:", usage.candidates_token_count)
    print("Total tokens:", usage.total_token_count)
else:
    print("Usage information not available.")