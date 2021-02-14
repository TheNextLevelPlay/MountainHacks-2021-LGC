import discord
import json
import os

from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))
bookPath = os.path.join(directory, '../books.json')

class BookCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def printbook(self, ctx):
        jsonBookList = open(bookPath)
        bookList = json.load(jsonBookList)
        for i in range(len(bookList["books"])):
            await ctx.send(bookList["books"][i]["name"])
        print()
    
    @commands.command()
    async def addbook(self, ctx, *args):
        with open(bookPath) as json_file : # open file and copy all data
            books_loaded = json.load(json_file)
        books_loaded["books"].append({"name":' '.join(str(elem) for elem in args)})
        with open(bookPath,'w') as json_dumped :
            json.dump(books_loaded,json_dumped,indent = 4,sort_keys = True)

        await ctx.send("Book added!")


def setup(bot):
    bot.add_cog(BookCommand(bot))