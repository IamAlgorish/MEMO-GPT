import os
import openai
import key

openai.api_key = key.apikey
import os
import openai

openai.api_key = key.apikey
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a mail to my gf",
  temperature=1,
  max_tokens=400,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
