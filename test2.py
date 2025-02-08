from agent import TwitterAgent
from characters import ch1
from remotes import prompts

print("test running")

new_agent = TwitterAgent(ch1.skizo, "example", "llama3.2")
deepSeek_Agent = TwitterAgent(ch1.skizo, "example_deepseek", "deepseek-r1:1.5b")

new_agent.generateStreamResponse("What do you think about the current state of the crypto trenches?")
print("\n\n")
'''print("deepseek response")


deepSeek_Agent.generateStreamResponse("What do you think about the current state of the crypto trenches?")
print("\n\n")

print("whats hot deepseek\n")'''
#deepSeek_Agent.generateStreamResponse(prompts.whats_hot_without_character(prompts.get_example_tweets(), ""))