import discord
import requests
import json

def getMeme():
    response = requests.get('https://meme-api.com/gimme')
    jsonData = json.loads(response.text)
    return jsonData['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('meme'):
            await message.channel.send(getMeme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('xxxxxx') # replaced my token due to privacy.
