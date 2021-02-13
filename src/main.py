import discord
import requests
import os
import json
import os
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix = '/')
client.remove_command("help")

token = os.getenv('DISCORD_TOKEN')
subject = ""
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=subject:" + subject)

bookList = {}

extensionList = ['cogs.help', 'cogs.searchSubject']

if __name__ == '__main__':
  for extension in extensionList:
    client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is ready.")
    jsonBookList = open('books.json')
    bookList = json.load(jsonBookList)
    print(bookList)
    print(response)


client.run(token)
