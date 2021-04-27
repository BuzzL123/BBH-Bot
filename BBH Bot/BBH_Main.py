import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
  print('We heve logged in as {0.user}'.format(client))
  
@client.event 
async def on_message(message):
  if message.author == client.user:
   return

  if 'fuck' in message.content or 'bitch' in message.content or 'dick' in message.content or 'pussy' in message.content or 'shit' in message.content or 'ass' in message.content or 'cum' in message.content:
    responses = ["Language!",
                 "Aaaaaaaaaaaaaaaaaaaaaaaa!!!!!!",
                 "STOP IT YOU MUFFIN"]
    await message.channel.send(f'{random.choice(responses)}!')

client.run(os.getenv('TOKEN'))