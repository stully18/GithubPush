from google import genai
import pydantic_core
from pydantic import *

client = genai.Client(api_key="AIzaSyAo2xHHRLjNMY1mAK2LkJvdDjrhffVfR8o")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)