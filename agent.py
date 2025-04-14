import ollama
import asyncio
from pydantic import BaseModel

''' 
    on final version have to change all instances of example back to agent. 
    only using example now to save space

'''

class Post(BaseModel):
    post: str

class PostList(BaseModel):
    posts: list[Post]


class Agent:
    def __init__(
            self, 
            system_prompt: str,
            _model_name: str, 
            _llm:str,
            name: str = "Agent",
            amt:int = -1,
            temp:int = 0.8,
        ):
        
        self.system = ollama.create(
            model=_model_name, 
            from_= _llm,
            parameters={"seed": 42, "temperature": temp, "num_predict": amt},    
            system=system_prompt,
            stream=False,
        )
        self.modelName = _model_name
        self.llm = _llm
        self.client = ollama.AsyncClient()
        self.name = name
        self.skills = []
        
        pass

    def generateResponse(self, prompt: str):
        response = ollama.chat(self.modelName, messages=[
            {
                'role': 'user',
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

    def generateStreamResponseWImage(self, prompt: str, image):
        messages = [
            {
                'role': 'user',
                'content': prompt,
                'images': [image]
            },
        ]

        for part in ollama.chat(self.modelName, messages=messages, stream=True):
            print(part['message']['content'], end='', flush=True)
        

    def calculateUserScore(self, users):
        pass

    async def asyncChat(self, prompt):
        print("waiting for response .. ")
        response = await self.client.generate(self.llm, prompt)
        print(response['response'])

    def agentEmbed(self,input):
        response = ollama.embed(self.llm, input)
        return response['embeddings']
    
    # return info for agent - llm, model name, 
    def agentInfo(self):
        return {
            "agent_name": "",
            "llm": self.llm,
            "model_name": self.modelName,
            "agent_name": self.name,
        }
    
    # a function to add new skills to agent
    def addSkills(self, skill):
        return
        
