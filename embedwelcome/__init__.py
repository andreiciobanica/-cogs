from .embedwelcome import welcome

async def setup(bot):
    bot.add_cog(welcome(bot))