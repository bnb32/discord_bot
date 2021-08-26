# bot.py
import os
from ban_users import users
import unicodedata
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    print(f'{member.name} has joined\n')
    if (any(u in member.name for u in users) or
        any(u in unicodedata.normalize('NFKC',member.name) for u in users) or
        any(u in unicodedata.normalize('NFKD',member.name) for u in users) or
        any(u in unicodedata.normalize('NFD',member.name) for u in users) or
        any(u in unicodedata.normalize('NFC',member.name) for u in users)):
        await member.ban(reason="banned for raiding", delete_message_days=7)
        print(f'{member.name} banned\n')

@client.event
async def on_ready():
    for guild in client.guilds:
        print(f'{client.user.name} has connected to {guild}!\n')

client.run(TOKEN)
