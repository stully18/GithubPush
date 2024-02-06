import openai

openai.api_key = "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"
def ai(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{prompt}"}])
    response = completion.choices[0].message.content
    return response