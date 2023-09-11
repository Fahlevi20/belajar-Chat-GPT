import openai

openai.api_key ='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'
completion = openai.ChatCompletion.create(model="babbage", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)