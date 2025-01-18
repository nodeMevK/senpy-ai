#from ollama import embed
import ollama
from remotes import prompts
from characters import ch1 

'''response = embed(model='llama3.2', input='Hello, world!')
print(response['embeddings']) '''

ollama.create(model='example', modelfile=ch1.test_model)



response = ollama.chat(model='llama3.2', messages=[
    
  {
    'role': 'user',
    #'content': 'Why is the sky blue?',
    'content': 'What do you think about Elon Musk?'
    #'content': prompts.whats_hot_prompt(prompts.get_example_tweets(), "", ch1.skizo)
  },

])

print(response["message"]['content'])