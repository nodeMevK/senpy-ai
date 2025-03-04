import numpy as np
from database.models import LongMemory, ShortMemory
#from remotes.prompts import 
import ollama
from sqlalchemy.orm import Session


class MemoryManager:
    def __init__(self):
        pass

    def embedData(self, text: str):
        response = ollama.embed(self.llm, input)
        return response['embeddings']

    def getLongTermMemory(self):


        ''' get data from db '''
        return

    def getShortTermMemory(self):

        ''' get short term mem from db '''

        return

    def formatMemory(self):
        return
    
    def getLongMemory(self, db: Session):
        return db.query(LongMemory).all()
    
    def getShortMemory(self, db: Session):
        return db.query(ShortMemory).all()