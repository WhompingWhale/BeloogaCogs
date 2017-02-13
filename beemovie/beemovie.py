import discord
from discord.ext import commands

class Mycog:
    """According to all known laws of aviation..."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """Bees Bees Bees"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
