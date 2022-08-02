import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

class welcome(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="discordembed")
    async def discordembed(self, ctx):
        embed=discord.Embed(title="Metodă de verificare", description="Pentru a putea avea acces la restul server-ului, trebuie să reacționezi utilizând emoticonul <:imperial:1004023820002279574>.", color=0xfff100)
        embed.set_author(name="Imperial România", icon_url="https://media.discordapp.net/attachments/928411916857126973/928426116253892608/novnbdalsjkvsanbpov.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/928411916857126973/928436594988449812/standard_4.gif")
        embed.set_footer(text="All Right Reserved ©️ Imperial România")
        await ctx.send(embed=embed)