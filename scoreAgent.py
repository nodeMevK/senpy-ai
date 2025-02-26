from agent import Agent
from PIL import Image
import base64


character = '''
    You are an expert score reader.  You will be prompted with images and you will tell people the score and team names respectively from the image you recieved.
    Keep answer short. You will be asked a score. Scores are typically depicted as a number followed by a - then another number. 

'''

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


#newImage = Image.open('./image1.jpg')

print("creating agent .. ")
#score_agent = Agent(character, "scorellm", "llama3.2")
score_agent2 = Agent(character, "scorellm2", "llava", temp=0.2)

print("agent created .. ")

print("prompting agent ..")
score_agent2.generateStreamResponseWImage("What is the score displayed in this image: ", encode_image('./static/image3.jpeg'))
print("\n")
