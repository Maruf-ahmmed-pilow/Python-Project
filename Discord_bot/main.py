import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We are redy to go in, {bot.user.name}')


@bot.event
async def on_member_join((member):
    await member.send(f"welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'shit' in message.content:
        await message.delete()
        await message.channel.send(f"Hello {message.author.name}!")

    await bot.process_commands(message)



#!hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")


@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "")
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} has been assigned to {role}")
    else:
        await ctx.send(f"{ctx.author.mention} has not been assigned to any role")


@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send("You said: " + msg)


@bot.command()
async def reply(ctx):
    await ctx.reply("Reply to a message" )


@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="Polling", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction(" ")
    await poll_message.add_reaction('')


@bot.command()
async def unassign(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "")
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has been unassigned from {role}")
    else:
        await ctx.send(f"{ctx.author.mention} has not been unassigned from any role")
@bot.command()
@commands.has_role(secret_role)
async def reset(ctx):
    await ctx.send("welcome to the server")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You are not authorized to use this command")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)