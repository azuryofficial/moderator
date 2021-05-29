import motor.motor_asyncio as motor
from dotenv import dotenv_values

CLIENT: motor.AsyncIOMotorClient = motor.AsyncIOMotorClient(dotenv_values(".env")["DB"])
