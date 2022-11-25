import os
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

#MongoDB URI to connect to the MongoDB cluster
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.ROCSTAR

