import discord 
import aiohttp 
import asyncio 
import time 
import motor.motor_asyncio 

import env 
import strings.strings as strings 
import cogs.economy as economy 


from discord.ext import commands 

E = env 
S = strings
e = economy

GUILD_ID = E.GUILD_ID 
APP_ID = E.APP_ID 
TOKEN = E.TOKEN 


class MyBot(commands.Bot): 
    def __init__(self): 
        # Change 123 to your application id
        super().__init__(command_prefix = "SN ", intents = discord.Intents.all(), application_id = APP_ID) 

        self.initial_extensions = [
            "cogs.myCommand", 
        ]

    async def setup_hook(self): 
        self.session = aiohttp.ClientSession() 

        for ext in self.initial_extensions: 
            await self.load_extension(ext) 
            #await self.load_extension("jishaku") 
        # Change 456 to your server/guild id
        await bot.tree.sync(guild=discord.Object(id = GUILD_ID)) 



    #async def close(self):
        #await super().close()
        #await self.session.close()

    async def on_ready(self): 
        print(f'{self.user} has connected to Discord!') 

bot = MyBot() 
num_users = len(bot.users) 

async def main(): 
        async with bot: 
            bot.mongoConnect = motor.motor_asyncio.AsyncIOMotorClient(E.URI) 
            await bot.start(E.TOKEN) 

asyncio.run(main()) 
