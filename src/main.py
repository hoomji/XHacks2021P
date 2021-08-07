# Importing the needed libraries
import os
import discord
from settings import Settings

# Commands
from commands.plotCommand import PlotCommand

# Importing the stay awake function
# from stayWake.stay_awake import stay_awake
# Ensures the bot runs 24/7
# stay_awake()

# Setting the discord client variable
bot = discord.Client()

commands = [PlotCommand(['plot'])]

settings = Settings()

# Showing that the bot is ready


@bot.event
async def on_ready():
    await bot.get_channel(settings.getAttribute("announce_channel_id")).send(settings.getAttribute("ready_message"))
    print(settings.getAttribute("ready_message"))


# Whenever there's a message, this function runs
@bot.event
async def on_message(message):
    # Ensures that a user is saying the commands and not the bot
    if message.author == bot:
      return
    
    if len(message.content) > 0 and message.content[0] != settings.getAttribute("command_prefix"):
      return
    
    # Check if the message was a command
    potentialCmdName = message.content.split(' ')[0][1::]
    
    done = False
    for cmd in commands:
      cmdNames = cmd.getNames()
      for cmdName in cmdNames:
        if(potentialCmdName == (cmdName)):
          await cmd.run(message)
          print("Command run: " + potentialCmdName)
          done = True
          break
      if done:
        break

# Running the bot
# INSERT YOUR BOT TOKEN ID
my_secret = os.environ['discordBot_token']
bot.run(my_secret)
