from agent import TwitterAgent
from characters import ch1


new_agent = TwitterAgent(ch1.skizo)

new_agent.generateStreamResponse("What do you think about the current state of the crypto trenches?")

