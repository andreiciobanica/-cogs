import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

class rapoarte(commands.Cog):
    politiegrade = [
        999558907800322141,
        999564403403931698,
        999493801448054794
    ]
    
    diicotgrade = [
        999558907800322141,
        999494666355482636,
        999494669492826162
    ]
    
    smurdgrade = [
        999558907800322141,
        999495021462040636,
        999495026084163645
    ]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="rapoartepolitie")
    async def rapoartepolitie(self, ctx, serverId, discordId):
            verif = False
            for x in permisiuni.politiegrade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        name = 'rapoarte-' + serverId + '-' + discordId
                        c = discord.utils.get(ctx.guild.categories, id=999720906303746168)
                        await ctx.guild.create_text_channel(name=name, category=c)
                        verif = True
                if verif == True:
                    break
                    
    @commands.command(name="rapoartediicot")
    async def rapoartediicot(self, ctx, serverId, discordId):
            verif = False
            for x in permisiuni.diicotgrade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        name = 'rapoarte-' + serverId + '-' + discordId
                        c = discord.utils.get(ctx.guild.categories, id=999720937295446067)
                        await ctx.guild.create_text_channel(name=name, category=c)
                        verif = True
                if verif == True:
                    break
                    
    @commands.command(name="rapoartesmurd")
    async def rapoartediicot(self, ctx, serverId, discordId):
            verif = False
            for x in permisiuni.smurdgrade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        name = 'rapoarte-' + serverId + '-' + discordId
                        c = discord.utils.get(ctx.guild.categories, id=999720963849605190)
                        await ctx.guild.create_text_channel(name=name, category=c)
                        verif = True
                if verif == True:
                    break