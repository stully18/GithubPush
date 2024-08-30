import textwrap
import google.generativeai as genai
from IPython.display import Markdown

def request(prompt):
    def to_markdown(text):
      text = text.replace('•', '  *')
      return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    genai.configure(api_key="AIzaSyAo2xHHRLjNMY1mAK2LkJvdDjrhffVfR8o")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    answer = response.text
    return answer