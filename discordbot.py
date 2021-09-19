from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def sodayo(ctx):
    await ctx.send('そうだよ(迫真)')


@bot.command()
async def iiy(ctx):
    await ctx.send('いいよ!こいよ!')
    
@bot.command()
async def ko(ctx):
    await ctx.send('こ↑こ↓')
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
