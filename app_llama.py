import ollama


print("running ")
response = ollama.chat(model='llama3.2', messages=[
    
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },

])

print("finished rendering")
print(response['message']['content'])