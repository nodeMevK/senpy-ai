from memory.accessMemory import MemoryManager
from database.dbSetup import getDb, Session
#from sqlalchemy.orm import Session


manager = MemoryManager()

session = Session()
memories = manager.getShortMemory(session)

for memory in memories:
    dct = {
        "name": memory.username,
        "post": memory.post,
        "timestamp": memory.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
    
    }
    print(dct) 