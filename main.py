import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)


TOKEN = os.getenv("TOKEN")
CHINA_ID = os.getenv("CHINA_ID")
CANAL_ID = os.getenv("CANAL_ID")

@bot.event
async def on_ready():
    print(f"Bot COMEÇOU")

@bot.command()
async def ola(ctx):
    await ctx.reply("Olá turu pom?")



@bot.event
async def on_presence_update(before, after):

    # Ignora qualquer outro usuário
    if after.id != CHINA_ID:
        return

    # Ignora se o status não mudou
    if before.status == after.status:
        return

    canal = bot.get_channel(CANAL_ID)

    if canal is None:
        return

    if after.status == discord.Status.online:
        await canal.send(f"{after.display_name} detectado!")
        # await canal.send(f"🟢 {after.display_name} ficou online!")

    elif after.status == discord.Status.offline:
        await canal.send(f"{after.display_name} sumiu!")
        # await canal.send(f"⚫ {after.display_name} ficou offline!")

bot.run(TOKEN)
