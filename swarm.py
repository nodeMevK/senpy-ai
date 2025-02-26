from agent import Agent
import threading
import multiprocessing

class Swarm:
    def __init__(self, _agents: list[Agent]):

        self.agents = _agents

        def coordinatedThinking(prompt: str):
            threads = []
            for agent in self.agents:
                thread = threading.Thread(target=agent.generateStreamResponse, args=(prompt,))

            return 
        

        pass