#from ollama import embed
#from ollama import Client
from remotes import prompts
from characters import ch1 

'''response = embed(model='llama3.2', input='Hello, world!')
print(response['embeddings']) '''

'''ollama.create(model='example', modelfile=ch1.test_model)

response = ollama.chat(model='llama3.2', messages=[
    
  {
    'role': 'user',
    #'content': 'Why is the sky blue?',
    'content': 'What do you think about Elon Musk?'
    #'content': prompts.whats_hot_prompt(prompts.get_example_tweets(), "", ch1.skizo)
  },

])'''


import ollama


'''example = ollama.create(
    model='example', 
    from_='llama3.2', 
    system="You are Mario from Super Mario Bros.")


print(example)
print(example.status)'''


response = ollama.chat(model='example', messages=[
    
  {
    'role': 'user',
    #'content': 'Why is the sky blue?',
    'content': 'who are you?'
    #'content': prompts.whats_hot_prompt(prompts.get_example_tweets(), "", ch1.skizo)
  },

])



'''example = Client().create(
    model='persona', 
    from_='llama3.2',
    parameters={"seed": 42, "temperature": 0},    
    system='You are Mario from Super Mario Bros.',
    stream=False,
    )

print(example.status)'''





print(response["message"]['content'])


