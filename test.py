from g4f.client import Client
import g4f


client = Client()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}],
    provider=g4f.Provider.Liaobots
)
print(response.choices[0].message.content)