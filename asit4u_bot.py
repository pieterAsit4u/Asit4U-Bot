import discord
import myconfig

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!' + ' ' + message.author.display_name + '! What would you like for lunch?')


client.run(myconfig.bot_token)