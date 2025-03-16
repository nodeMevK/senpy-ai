from agent import Agent
import threading
import multiprocessing

manager_logic = '''
    Assess the reponses from these agents. Rate them on a scale from 1-10, 10 being the best. 
    The rating should assess the correctness and 

'''

class Swarm:
    def __init__(self, _agents: list[Agent], _manager: Agent):

        self.agents = _agents
        self.managerAgent = _manager

        pass

    # function where manager agent decides score of agent reponses
    # actually might fix this with a pedantic approach 
    # might not need to loop through, instead just check them all at once instead of 1 by 1
    def managerScore(self, agentResponses: list, managerLogic: str):

        prompt = ''''''
        for response in agentResponses:
            self.managerAgent.generateStreamResponse(prompt)

        return 
    

    # for I/O bound tasks    
    def coordinatedThinkingThreading(self, prompt: str):
        threads = []
        for agent in self.agents:
            thread = threading.Thread(target=agent.generateStreamResponse, args=(prompt,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return


    # for CPU intensive tasks
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
    # need to find a spot for manager info might just make new function for it 
    def swarmInfo(self):
        ls = []
        for agent in self.agents:
            ls.add(agent.agentInfo)
        return ls
    

    # function ot add to list of agents
    def addAgent(self, agent: Agent):
        self.agents.append(agent)
        return

    # function to remove agent from list
    def removeAgent(self, agent: Agent):
        return
    

        