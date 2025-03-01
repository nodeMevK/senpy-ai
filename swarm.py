from agent import Agent
import threading
import multiprocessing

class Swarm:
    def __init__(self, _agents: list[Agent], _manager: Agent):

        self.agents = _agents
        self.managerAgent = _manager

        pass

    # function where manager agent decides score of agent reponses
    # actually might fix this with a pedantic approach 
    def managerScore(self, agentResponses: list):
        for response in agentResponses:
            self.managerAgent.generateStreamResponse("")

        return
        
    def coordinatedThinkingThreading(self, prompt: str):
        threads = []
        for agent in self.agents:
            thread = threading.Thread(target=agent.generateStreamResponse, args=(prompt,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return


    def coordinatedThinkingProcessing(self, prompt: str):
        processes = []
        for agent in self.agents:
            process = multiprocessing.Process(target=agent.generateStreamResponse, args=(prompt,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return 
    
    # return info on agents  
    def swarmInfo(self):
        ls = []
        for agent in self.agents:
            ls.add(agent.agentInfo)
        return ls
    

        