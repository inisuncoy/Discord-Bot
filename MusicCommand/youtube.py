import discord

import youtube_dl

from discord.ext import commands
-----------------------------------------------
@cat.command(pass_context=True)
async def play(ctx):
    if not ctx.message.author.voice:
        await ctx.send('you are not connected to a voice channel')
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice.client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop = client.loop)
        voice_channel.play(player)
        
    await ctx.send(f'**Music:**{player.title}')
