
import os
os.system("pip install discord.py-self")

import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from discord import Webhook, AsyncWebhookAdapter
try:
  import typing_extensions
  import colorama
  from colorama import Fore, Style, init
  from colorama import Fore as C
  from colorama import Style as S
  import os
  import aiohttp
  import server
  colorama.init()
except:
  import os
  os.system("pip install -r install.txt")
#-----------CONFIG-----------#

token = os.environ.get("TOKEN")
logger_url_nsfw = os.environ.get("URL_NSFW")
logger_url = os.environ.get("URL_NORMAL")
owner_id = int(os.environ.get("OWNER_ID"))
guild_id = int(os.environ.get("GUILD_ID"))

#-------------CODE-------------#

bot = commands.Bot(command_prefix="",
self_bot=True, case_insensitive=True)
bot.remove_command(name="help")



print("Logging in...")

@bot.event
async def on_connect():
  print(f"""
  {Fore.WHITE}
  {Style.DIM}
  Logged in {bot.user} - {bot.user.id}
  
  Logging messages
  {Fore.RESET}
  """)

#-------------------------------------------------------#

#-------------------------------------------------------#

#-------------------------------------------------------#

async def send_nsfw_log(message):
    async with aiohttp.ClientSession() as session:
                print(message.reference)
                msgIsReply = message.reference
                webhook = Webhook.from_url(str(logger_url_nsfw), adapter=AsyncWebhookAdapter(session))
                member = discord.Member
                if not message.attachments:
                    if msgIsReply is not None:
                        msgReply = await message.channel.fetch_message(message.reference.message_id)
                        
                        await webhook.send(f"***NSFW MESSAGE***```\n{message.content}```\n**Reply Content:**\n```\n{msgReply.content}```\n**Replying To: **{msgReply.author}\n<#{message.channel.id}> || {message.channel}\n** {[f'Direct Message' if message.guild == None else message.guild.name]}**".replace(f'{member.mention}', f'@{member.name}#{member.discriminator}').replace(f"<@!{owner_id}>", f"@botowner"), username=message.author.name,
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                    else:
                        await webhook.send(f"***NSFW MESSAGE***```\n{message.content}```\n<#{message.channel.id}> || {message.channel}\n** {[f'Direct Message' if message.guild == None else message.guild.name]}**".replace(f'{member.mention}', f'@{member.name}#{member.discriminator}').replace(f"<@!{owner_id}>", f"@botowner"), username=message.author.name,
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                        
                else:
                    if msgIsReply is not None:
                        msgReply = await message.channel.fetch_message(message.reference.message_id)
                        
                        await webhook.send(f"***NSFW MESSAGE***```\n[Attachment name: {message.attachments[0].filename}]\n```Attachment url:\n{message.attachments[0].url}\n\n```\n{message.content}```\n**Reply Content:**\n```\n{msgReply.content}```\n**Replying To: **{msgReply.author}\n<#{message.channel.id}> || {message.channel}\n** {[f'Direct Message' if message.guild == None else message.guild.name]}**".replace(f'{member.mention}', f'@{member.name}#{member.discriminator}').replace(f"<@!{owner_id}>", f"@botowner"), username=message.author.name,
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                    else:
                        await webhook.send(f"***NSFW MESSAGE***```\n[Attachment name: {message.attachments[0].filename}]\n```Attachment url:\n{message.attachments[0].url}\n\n```\n{message.content}```\n<#{message.channel.id}> || #{message.channel}\n**{[f'Direct Message' if message.guild == None else message.guild.name]}**", username=message.author.name, 
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                  
                    


async def send_normal_log(message):
        async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(str(logger_url), adapter=AsyncWebhookAdapter(session))
                member = discord.Member
                msgIsReply = message.reference
                if not message.attachments:
                    if msgIsReply is not None:
                        msgReply = await message.channel.fetch_message(message.reference.message_id)
                        
                        await webhook.send(f"```\n{message.content}```\n**Reply Content:**\n```\n{msgReply.content}```\n**Replying To: **{msgReply.author}\n<#{message.channel.id}> || {message.channel}\n** {[f'Direct Message' if message.guild == None else message.guild.name]}**".replace(f'{member.mention}', f'@{member.name}#{member.discriminator}').replace(f"<@!{owner_id}>", f"@botowner"), username=message.author.name,
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                    else:
                        await webhook.send(f"```\n{message.content}```\n<#{message.channel.id}> || {message.channel}\n** {[f'Direct Message' if message.guild == None else message.guild.name]}**".replace(f'{member.mention}', f'@{member.name}#{member.discriminator}').replace(f"<@!{owner_id}>", f"@botowner"),username=message.author.name,
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                    
                else: 
                    if msgIsReply is not None:
                        msgReply = await message.channel.fetch_message(message.reference.message_id)
                        
                        await webhook.send(f"```\n[Attachment name: {message.attachments[0].filename}]\n```Attachment url:\n{message.attachments[0].url}\n\n```\n{message.content}```\n**Reply Content:**\n```\n{msgReply.content}```\n**Replying To: **{msgReply.author}\n<#{message.channel.id}> || {message.channel}\n** {[f'Direct Message' if message.guild == None else message.guild.name]}**".replace(f'{member.mention}', f'@{member.name}#{member.discriminator}').replace(f"<@!{owner_id}>", f"@botowner"), username=message.author.name,
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
                    else:
                        await webhook.send(f"```\n[Attachment name: {message.attachments[0].filename}]\n```Attachment url:\n{message.attachments[0].url}\n\n```\n{message.content}```\n<#{message.channel.id}> || #{message.channel}\n**{[f'Direct Message' if message.guild == None else message.guild.name]}**", username=message.author.name, 
avatar_url=message.author.avatar_url, 
allowed_mentions=discord.AllowedMentions(everyone=False))
        
#-------------------------------------------------------#

@bot.event
async def on_message(message):
    if message.guild.id != guild_id:
        return
    
    if message.channel.name == "nsfw":
        await send_nsfw_log(message)
        
    else:
        await send_normal_log(message)


try:
	server.keep_alive()
	bot.run(token)
except discord.LoginFailure as err:
    print(f"{Fore.RED}Client failed to log in. {Fore.WHITE}Error: {err}  {Fore.RESET}")
except Exception as err:
    print(f"{Fore.RED}An error occured:{Fore.WHITE} {err} {Fore.RESET}")