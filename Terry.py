#os stuff
import os
import random
import logging

#Discord Stuff
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
prefix = '>'
bot = commands.Bot(command_prefix=prefix)

#  Bad Words and Phrases
with open("badwords.txt") as file: # bad-words.txt contains one blacklisted phrase per line
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log',encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'{bot.user.name} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# Responses like Möp-Se / Moderation
@bot.event
async def on_message(message):
     print('{0.author.display_name}:'.format(message) , message.content)
     if message.author.name == bot.user.name:
          return
     if message.content == 'Möp':
          response = 'Se'
          await message.channel.send(response)
          
     elif message.content == 'hello':
          response = 'Hello {0.author.display_name}'.format(message)
          await message.channel.send(response)
     
     elif message.channel.is_nsfw():
            if message.author.name == bot.user.name:
                return
            elif any(bad_word in message.content for bad_word in bad_words):
             #user = message.author
             response = '{} No You, '.format(message.author.mention)
             respo = message.content
             await message.channel.send(response + respo)
             #await message.delete()
            

     elif any(bad_word in message.content for bad_word in bad_words):
         response = '{}, your message has been censored.'.format(message.author.mention)
         await message.channel.send(response)
         await message.delete() 
        
     #elif message.content =='':
     #     response = ''
     await bot.process_commands(message)

# Admin commands
#@bot.command(name='create-channel')
#@commands.has_role('MOD')
#async def create_channel(ctx, channel_name='pray4terry'):
#    guild = ctx.guild
#    existing_channel = discord.utils.get(guild.channels, name=channel_name)
#    if not existing_channel:
#        print(f'Creating a new channel: {channel_name}')
#        await guild.create_text_channel(channel_name)


# Commands for Devs
@bot.command(name='test', help='Just a Test Command')
@commands.has_role('Entwickler')
async def test(ctx):
    user = ctx.author
    response = "ICH TESTE ALLES WAS GEHT"
    await user.send(response)

# Commands
@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = ['I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        ('Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'),]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='hello', help='Mention the Author')
async def hello(ctx):
    response = 'Hello {0.author.display_name}'.format(ctx)
    print('Hello {0.author.display_name}'.format(ctx))
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='ping', help='Checks the response time of the Bot')
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.command(name='tech', help='Calling the Tech support')
async def tech(ctx):
    techid = '<@218491330869985290>'
    response = '{0.author.display_name} needs Support %s'.format(ctx) % techid
    print(response)
    await ctx.send(response)
#@bot.command(name='tyra', help='Command to Mention only Tyraction')
#async def tyra(ctx):
#    tyraid ='<@263752448584187904>:'
#    response = '{0.author.display_name} triggered Tyra %s
#    SwiftRage'.format(ctx)% tyraid
#    print(response)
#    await ctx.send(response)

# Events
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        user = ctx.author
        await user.send('You do not have the correct role for this command.')

bot.run(TOKEN)