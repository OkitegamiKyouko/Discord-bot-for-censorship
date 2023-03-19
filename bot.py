import discord
from discord.ext import commands
from dictionary import token, admin_id, stopwords


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


async def notify_admin(message: discord.Message, word: str):
    guild = message.guild
    admin_user = guild.get_member(admin_id)
    if admin_user:
        await message.channel.send(f'{admin_user.mention}, this user "{message.author.mention}" said prohibited words.')
    else:
        await message.channel.send(f'There is no such admin with that ID.')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for word in stopwords:
        if word in message.content:
            await message.delete()
            await notify_admin(message, word)
            break

    await bot.process_commands(message)


bot.run(token)
