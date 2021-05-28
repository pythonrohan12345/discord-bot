from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(bot.latency * 1200)}ms")

@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["it is certain",
    "it is decidedly",
    "without a doubt",
    "Yes - definatly",
    "You may reply on it",
    "As i see it yes",
    "Most likely",
    "Outlook good",
    "signs point to yes",
    "Reply hence, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "concentrate and ask again",
    "Dont count on it",
    "my reply is no",
    "my sources say no",
    "Outlook not so good",
    "very doubtfull"]
    await ctx.send(f"Questions {question}\nAnswer: {random.choice(responses)}")

@bot.command()
async def clear(ctx, amount=15):
    await ctx.channel.purge(limit = amount)

@bot.command()
async def kick(ctx, member : discord.Member,*, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return
        

bot.run(Token)