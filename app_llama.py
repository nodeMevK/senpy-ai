import ollama
from remotes import prompts
from characters import ch1


print("running ")
'''response = ollama.chat(model='llama3.2', messages=[
    
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },

])'''


response = ollama.chat(model='llama3.2', messages=[
    
  {
    'role': 'user',
    #'content': 'Why is the sky blue?',
    'content': prompts.whats_hot_prompt(prompts.get_example_tweets(), "", ch1.narcissist)
  },

])

print("finished rendering")
print(response['message']['content'])