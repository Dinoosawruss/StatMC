import discord
from discord.ext import commands

import sqlite3


class EmbedColour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['embedcolor','ec'])
    @commands.has_permissions(administrator=True)
    async def embedcolour(self, ctx, colour):
        conn = sqlite3.connect("./data/guildSettings.db")

        sql = '''SELECT * FROM Guild 
                WHERE ID=? AND Patreon="True"'''
        
        curr = conn.cursor()
        args = (ctx.guild.id,)
        curr.execute(sql, args)

        if len(curr.fetchall()) == 1:
            sql = f"""UPDATE Guild
                    SET EmbedColour=?
                    WHERE ID=?"""
            
            args = (str(int(colour,base=16)), ctx.guild.id,)
            curr.execute(sql, args)
            
            conn.commit()

            sql = f'''SELECT * FROM Guild 
                WHERE ID=?'''
            
            args = (ctx.guild.id,)
            curr.execute(sql, args)
            colour = int(curr.fetchone()[2])
            
            embed = discord.Embed(title="Sample Embed", description="This is a sample embed to show what the new colour will look like", color=colour)

            await ctx.send(f"{ctx.author.mention} embed colour updated!")
            await ctx.send(embed=embed)

        else:
            await ctx.send(f"{ctx.author.mention} sorry but this is a patreon exclusive command. Please consider becoming a patreon at https://www.patreon.com/statmc")



def setup(bot):
    bot.add_cog(EmbedColour(bot))
