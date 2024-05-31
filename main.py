from highrise import BaseBot
from highrise import __main__
from collections import UserDict
from asyncio import run as arun
from highrise.models import SessionMetadata, User
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
from highrise import BaseBot, User, Position, SessionMetadata
import asyncio
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import *
from highrise.models import *
import time
from highrise.__main__ import *
from highrise.models import (AnchorPosition, CurrencyItem,Item,Position,SessionMetadata,User,)


class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class MyBot(BaseBot):

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.following_user = None 
          self.banned_users = {} 
          self.following_username = None
          super().__init__()
          self.user_positions = {}



    async def run(self, room_id, token):
           definitions = [BotDefinition(self, room_id, token)]
           await __main__.main(definitions)
        
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        while True:
            await self.highrise.chat("Welcome to the BMW Airplane building") 
            await self.highrise.chat("There is no love after the love of German cars") # حط مكان الرقم اي شي تبيه 
            await self.highrise.chat("No need to worry about the future")
            time.sleep(30) # الرقم هاد يعني كل متى يرسل الرساله 
if __name__== "__main__": 
    room_id = "66572359188d249f34649c8d"
    token = "764738b7b911cfeb0e5022d4b73e9354d918697492296a4ee6fb9de75ffb39a3"
    arun(MyBot().run(room_id, token))