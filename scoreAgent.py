from agent import Agent
from PIL import Image
import base64


character2 = '''
    You are an expert score reader.  You will be prompted with images and you will tell people the score and team names respectively from the image you recieved.
    Keep answer short. You will be asked a score. Scores are typically depicted as a number followed by a - then another number. 

'''

character = '''

    You are an expert OCR processor specialized in extracting exactly two scores from images. Given any image containing score information:

    Apply OCR to the entire image first
    Look for numerical patterns typical of scores (e.g., "0-0", "3:2", "Home 21 - Away 18")
    Identify two distinct numerical values representing the two scores
    Format output consistently as: "Score 1: [X], Score 2: [Y]"

    Requirements:
    ALWAYS extract exactly two scores, even if challenging
    If scores appear as "X-Y", separate them
    For sports displays, identify team/player scores rather than time/period numbers
    Prioritize larger, more prominent numbers as likely scores
    Look for scores near team names, vs/versus indicators, or scoreboard regions
    If multiple score pairs exist, select the most current/final scores

    Edge Cases:
    If only one score is visible, search harder for the second score
    If more than two scores appear, determine which two are the main scores
    If scores are unclear, provide your best estimate and indicate uncertainty
    If numbers are stylized or partially obscured, make educated inference

    Always return TWO separate scores - no exceptions.

'''

agent1 = '''

    

'''

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


#newImage = Image.open('./image1.jpg')

print("creating agent .. ")
#score_agent = Agent(character, "scorellm", "llama3.2")
score_agent2 = Agent(character, "scorellm2", "llava", temp=0.0)

print("agent created .. ")

print("prompting agent ..")
score_agent2.generateStreamResponseWImage("What is the score displayed in this image: ", encode_image('./static/image3.jpeg'))
score_agent2.generateStreamResponseWImage("What is the score displayed in this image: ", encode_image('./static/image2.png'))
score_agent2.generateStreamResponseWImage("What is the score displayed in this image: ", encode_image('./static/image1.jpg'))

print("\n")
