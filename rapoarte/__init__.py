from .rapoarte import rapoarte

async def setup(bot):
    bot.add_cog(rapoarte(bot))