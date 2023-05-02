import openai
openai.api_key_path = "./openAI/key"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": "Tell me a joke"}],
    max_tokens = 1024,
    temperature = 0.8)

message = completion.choices[0].message.content
print(message)
