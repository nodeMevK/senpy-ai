from agent import Agent
import threading
import multiprocessing

class Swarm:
    def __init__(self, _agents: list[Agent]):

        self.agents = _agents

        def coordinatedThinkingThreading(prompt: str):
            threads = []
            for agent in self.agents:
                thread = threading.Thread(target=agent.generateStreamResponse, args=(prompt,))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            return


        def coordinatedThinkingProcessing(prompt: str):
            processes = []
            for agent in self.agents:
                process = multiprocessing.Process(target=agent.generateStreamResponse, args=(prompt,))
                processes.append(process)
                process.start()

            for process in processes:
                process.join()

            return 
        

        pass