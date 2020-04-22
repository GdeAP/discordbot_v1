

# Basic Discord Bot
# 2020


# IMPORT

import discord
from discord.ext import commands
import os

# INIT 

client = commands.Bot(command_prefix = '$') 	# Command Prefix 

# Events

@client.event 	
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
	print("Bot is ready") 	# Tell the bot ready

@client.event
async def on_member_join(member):			
	print(f'{member} has joined a server') 	# Member has join

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server') 	# Member has left

# Commands

@client.command()
async def ping(ctx):
	await ctx.send(f'The ping is {round(client.latency * 1000)}ms') 	# Ping

@client.command()
async def clear(ctx, amount=20):
	await ctx.channel.purge(limit=amount) 								# Clear

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason) 									# Kick @member (reason)
	
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason) 									# Ban @member (reason)
	await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()	
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users: 										# Unban
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
 																		# Load & Unload
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')


# Run

client.run('Your token') 	# Token(Write your token here)
