import os
import random
import discord

# Variables
token = "TOKEN"
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

clientMessage = ""

# Methods
def get8ball():
    print("8ball run")
    x = random.randrange(0, 3)
    if( x == 0):
        print("Selected true 8ball message")
        with open("8ballTRUE.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
    if(x == 1):
        print("Selected medium 8ball message")
        with open("8ballUNKNOWN.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
    if(x == 2):
        print("Selected false 8ball message")
        with open("8ballFALSE.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
        
def printHelp():
    return "you already know how to do /help do /8ball [message] for a reply\n say racism for support!\n say [i need jesus] for help";

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    clientMessage = message

    if message.author == client.user:
        return
    
    if message.content.startswith("/8ball"):
        await message.channel.send(get8ball())

    if (client.user.mentioned_in(message)):
        await message.reply("fuck off please")

    if message.content.startswith("hello") or message.content.startswith("hi"):
        await message.reply("fuck off")
        
    if message.content.startswith("racism"):
        await message.add_reaction("❤")


    else:
        if message.content.startswith("i need jesus"):
            await message.channel.send("here pooki: https://duckduckgo.com/?t=ffab&q=jesus&iax=images&ia=images")


# Connect to discord servers and authorize
client.run(token)