import asyncio
import datetime
import json
import logging
import sqlite3
from pathlib import Path

import discord
from discord.ext import commands

from func import options

def config_load():
    with open('data/config.json', 'r', encoding='utf-8-sig') as doc:
        return json.load(doc)

async def run():
    config = config_load()
    bot = Bot(config=config,
              description=config['description'])
    bot.remove_command("help")

    try:
        await bot.start(config['token'])
    except KeyboardInterrupt:
        await bot.logout()


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=self.get_prefix_,
            description=kwargs.pop('description')
        )
        self.start_time = None
        self.app_info = None

        self.loop.create_task(self.track_start())
        self.loop.create_task(self.load_all_extensions())

    async def track_start(self):
        await self.wait_until_ready()
        self.start_time = datetime.datetime.utcnow()

    async def get_prefix_(self, bot, message):
        prefix = ['?']
        return commands.when_mentioned_or(*prefix)(bot, message)

    async def load_all_extensions(self):
        await self.wait_until_ready()
        await asyncio.sleep(1) 
        cogs = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                self.load_extension(f'cogs.{extension}')
                print(f'loaded {extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__} : {e}'
                print(f'failed to load extension {error}')
            print('-' * 10)

    async def on_ready(self):
        print('-' * 10)
        self.app_info = await self.application_info()
        print(f'Logged in as: {self.user.name}\n'
              f'Using discord.py version: {discord.__version__}\n'
              f'Owner: {self.app_info.owner}')
        print('-' * 10)
    
    async def on_guild_join(self, guild):
        conn = sqlite3.connect("./data/guildSettings.db")

        sql = f"""INSERT INTO Guild(ID,Patreon,EmbedColour,Prefix) 
                VALUES(?,"False","16711680","?")"""
            
        cur = conn.cursor()
        args = (guild.id,)
        cur.execute(sql, args)

        conn.commit()

        embed = discord.Embed(title="StatMC", description="Thank you for inviting StatMC!\n\nPlease use `?help` for a list of commands", color=16711680)
        embed.set_thumbnail(url=options.dinoLogo)

        await guild.text_channels[0].send(embed=embed)

        print(f'Added to new guild: {guild.name}')
        print('-'*10)

    async def on_command(self, ctx):
        print(f'Command run by: {ctx.author}\n'
              f'Run in server: {ctx.guild.name}\n'
              f'Command: {ctx.command}')
        print('-'*10)
    
    async def on_command_error(self, ctx, error):
        await ctx.send(f'Sorry {ctx.author.mention} something appears to have gone wrong with this command...')

        print(error)
        print('-'*10)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
