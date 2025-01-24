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
        