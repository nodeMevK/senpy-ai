import ollama

class TwitterAgent:
    def __init__(self, system_prompt: str):
        self.system = ollama.create(
            model='agent', 
            from_='llama3.2',
            parameters={"seed": 42, "temperature": 0},    
            system=system_prompt,
            stream=False,
        )

        pass

    def generateResponse(self, prompt):
        response = ollama.chat(model='agent', messages=[
            {
                'role': 'user',
                #'content': 'Why is the sky blue?',
                #'content': prompts.whats_hot_prompt(prompts.get_example_tweets(), "", ch1.skizo)
                'content': prompt
            },
        ])
        return response['message']['content']
        

    def generateStreamResponse(self, prompt):
        messages = [
            {
                'role': 'user',
                'content': prompt,
            },
        ]

        for part in ollama.chat('agent', messages=messages, stream=True):
            print(part['message']['content'], end='', flush=True)

        

    def calculateUserScore(self, users):
        pass


    
