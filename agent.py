import ollama

''' 
    on final version have to change all instances of example back to agent. 
    only using example now to save space

'''

class TwitterAgent:
    def __init__(
            self, 
            system_prompt: str,
            _model_name: str, 
            llm:str 
            ):
        self.system = ollama.create(
            model=_model_name, 
            from_=llm,
            parameters={"seed": 42, "temperature": 0.8},    
            system=system_prompt,
            stream=False,
        )

        self.modelName = _model_name

        pass

    def generateResponse(self, prompt: str):
        response = ollama.chat(self.modelName, messages=[
            {
                'role': 'user',
                #'content': 'Why is the sky blue?',
                #'content': prompts.whats_hot_prompt(prompts.get_example_tweets(), "", ch1.skizo)
                'content': prompt,
            },
        ])
        return response['message']['content']
        

    def generateStreamResponse(self, prompt: str):
        messages = [
            {
                'role': 'user',
                'content': prompt,
            },
        ]

        for part in ollama.chat(self.modelName, messages=messages, stream=True):
            print(part['message']['content'], end='', flush=True)

        

    def calculateUserScore(self, users):
        pass

    def asyncChat(self, prompt):
        pass