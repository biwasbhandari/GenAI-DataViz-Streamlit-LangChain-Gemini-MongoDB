# Import necessary libraries

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# load our env
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
print(f"MongoDB URI: {MONGODB_URI}")

# Establishing a connection
client = MongoClient(MONGODB_URI)

# Providing a database and collection
db = client['MyTutorial']
collection = db['First Collection']

# Insert a document 

mydocument = {
    "video":"Youtube Video",
    "Description":"This is a youtube video"
}
insert_doc = collection.insert_one(mydocument)
print(f"Document Insert Successfull. The document id is: {insert_doc.inserted_id}")


# close connection
client.close()