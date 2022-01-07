BOT_TOKEN = 'OTI4OTM0NzAzMTAzMzY5Mjc3.Ydf_2w.qAgN76c87V-VKDgSrFy6UUI-tN4'

import typing
import discord
from discord.ext import commands

import random
import time
import datetime

from bot_functions import SWEAR_WORDS, getTopicInfo, getMemeURL


BOT_COLOR = discord.Color.green()
ERROR_COLOR = discord.Color.red()
COMMAND_PREFIX = "-"
bot = commands.Bot(command_prefix=COMMAND_PREFIX)
bot.remove_command('help')
log_channel = None

@bot.event
async def on_ready():
    global log_channel
    print('{0.user} READY!'.format(bot))
    log_channel = bot.get_channel(928940594921889812)
    await log_channel.send('{0.user} READY!'.format(bot))


@bot.event
async def on_message(message):
    log = str(datetime.datetime.now()) +" : MESSAGE RECEIVED : " + str(message.author.name) + " : " + str(message.content)
    if message.channel != log_channel:
        print(log)
        await log_channel.send(log)
    if message.author == bot.user:
        return
    for word in SWEAR_WORDS:
        if word in message.content:
            embed = discord.Embed(description="{} please refrain from swearing!".format(message.author.mention),color=ERROR_COLOR)
            await message.delete()
            await message.channel.send(embed=embed)
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before,after):
    log = str(datetime.datetime.now()) +" : MESSAGE EDIT : " + str(after.author.name) + " : " + str(before.content) + " -> " + str(after.content)
    if after.channel != log_channel:
        print(log)
        await log_channel.send(log)
    
#HELP COMMAND
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Help",description="Use {}help <command> for extended information on a command.".format(COMMAND_PREFIX),color=BOT_COLOR)
    utility_commands = 'memberinfo\nserverinfo\ntopicinfo\nping\nremind\ndelmsgs\npollYN'
    fun_commands = "choose\nflip\nrps\nspoiler"
    embed.add_field(name="Utility Commands",value=utility_commands)
    embed.add_field(name="Fun Commands",value=fun_commands)    
    await ctx.send(embed=embed)
#UTILITY COMMANDS HELP
@help.command()
async def ping(ctx):
    embed = discord.Embed(title="Ping :computer:",description="Returns the web-socket ping of the user.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}ping".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}ping".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def memberinfo(ctx):
    embed = discord.Embed(title="Memberinfo :technologist:",description="Returns the information about a particular server member.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}memberinfo <member>".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}memberinfo **@xyzuser**".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def delmsgs(ctx):
    embed = discord.Embed(title="Delete Messages :x:",description="Deletes messages in a text channel. If number is not provided, it deletes 1 previous message. The user and bot must have manage message permission.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}delmsgs [number]".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{0}delmsgs 5\n{0}delmsgs".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="Serverinfo :information_source:",description="Returns the information about the server.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}serverinfo".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}serverinfo".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def pollYN(ctx):
    embed = discord.Embed(title="Poll Yes/No :bar_chart:",description="Creates a Yes/No Poll.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}pollYN <question>".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}pollYN should we xyz?".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def topicinfo(ctx):
    embed = discord.Embed(title="Topicinfo :information_source:",description="Returns the information about a particular topic from the web.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}topicinfo <topic>".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}topicinfo discord".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def remind(ctx):
    embed = discord.Embed(title="Remind :alarm_clock:",description="Creates a reminder for given time in seconds.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}remind <time> [reminder]".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{0}remind 5 Get Groceries\n{0}remind 5".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)

#FUN COMMANDS HELP
@help.command()
async def choose(ctx):
    embed = discord.Embed(title="Choose :thinking:",description="Returns a choice from the options provided!",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}choose <choices (space separated)>".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}choose a b c".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def flip(ctx):
    embed = discord.Embed(title="Flip :coin:",description="Flips a coin",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}flip".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}flip".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def rps(ctx):
    embed = discord.Embed(title="Rock Paper Scissors :rock: :newspaper: :scissors:",description="The traditional Rock-Paper-Scissors game. Type the command and then your choice. Let's see if you can beat our bot!",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}rps [choice]".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}rps rock".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def spoiler(ctx):
    embed = discord.Embed(title="Spoiler :shushing_face:",description="Censors a message as a spoiler.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}spoiler <message>".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}spoiler Ironman is dead.".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)
@help.command()
async def meme(ctx):
    embed = discord.Embed(title="Meme :shushing_face:",description="Censors a message as a spoiler.",color=BOT_COLOR)
    embed.add_field(name="Syntax",value="{}spoiler <message>".format(COMMAND_PREFIX))
    embed.add_field(name="Example",value="{}spoiler Ironman is dead.".format(COMMAND_PREFIX))
    await ctx.send(embed=embed)

#MODERATION
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member):
    await member.send("You have been kicked from the server.")
    await member.kick(reason="")

#UTILITY COMMANDS
@bot.command()
async def memberinfo(ctx, member:discord.Member):
    embed = discord.Embed(title="Member Info",description="Returns the information about a particular server member!",color=BOT_COLOR)
    embed.add_field(name="Username",value=member.mention,inline=True)
    embed.add_field(name="ID",value=member.id,inline=True)
    embed.add_field(name="Top Role",value=member.roles[1].mention,inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by {}".format(ctx.author.name))
    await ctx.send(embed=embed)
@memberinfo.error
async def memberinfoError(ctx, error):
    embed = discord.Embed(color=ERROR_COLOR)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name="ERROR :warning:", value="member is a required argument!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    elif isinstance(error, commands.MemberNotFound):
        embed.add_field(name="ERROR :warning:", value="member not found!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    else:
        raise error
    await ctx.send(embed=embed)
    
@bot.command()
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(title="Server Info :information_source:", color=BOT_COLOR)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    info_msg = f":white_small_square: ID: **{ctx.guild.id}**\n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime('%a, %d %b %Y | %H:%M:%S %ZGMT')}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}**;\n\t\t**{text_channels}** Text, **{voice_channels}** Voice"
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ",
        value = info_msg)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by {}".format(ctx.author.name))
    await ctx.send(embed=embed)

@bot.command()
async def topicinfo(ctx,*,content:str):
    await ctx.send("Processing request :hourglass:")
    embed = discord.Embed(title="Topic Info :information_source:", color=BOT_COLOR)
    embed.add_field(name = f"Information About **{content}**: ",
        value = getTopicInfo(content))
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by {}".format(ctx.author.name))
    await ctx.send(embed=embed)
@topicinfo.error
async def topicinfoError(ctx, error):
    embed = discord.Embed(color=ERROR_COLOR)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name="ERROR :warning:", value="Provide a topic to search for!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    else:
        raise error
    await ctx.send(embed=embed)
@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong :ping_pong:", color=BOT_COLOR)
    embed.add_field(name="Latency", value=":clock2: "+str(round(bot.latency * 1000))+"ms", inline=True)
    await ctx.send(embed=embed)

@commands.bot_has_permissions(manage_messages=True)
@commands.has_permissions(manage_messages=True)
@bot.command(pass_context = True)
async def delmsgs(ctx, number:typing.Optional[int]=1):
    with ctx.channel.typing():
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=number)
        await ctx.send("Deleted {} message(s)".format(len(deleted)),delete_after=5)

@bot.command()
async def pollYN(ctx, *, content:str):
    embed = discord.Embed(title=f"{content} :bar_chart:", description="React to this message with ✅ for yes, ❌ for no.",color=BOT_COLOR)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url) 
    message = await ctx.channel.send(embed=embed)
    await message.add_reaction("✅")
    await message.add_reaction("❌")
@pollYN.error
async def pollYNError(ctx, error):
    embed = discord.Embed(color=ERROR_COLOR)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name="ERROR :warning:", value="Provide a poll question!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    else:
        raise error
    await ctx.send(embed=embed)

@bot.command()
async def spoiler(ctx,*,content:str):
    await ctx.message.delete()
    embed = discord.Embed(title="SPOILER ALERT!!! :warning: :shushing_face:", description="||{}||".format(content),color=BOT_COLOR)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Spoiler given by {}".format(ctx.author.name))
    await ctx.send(embed=embed)
@spoiler.error
async def spoilerError(ctx, error):
    embed = discord.Embed(color=ERROR_COLOR)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name="ERROR :warning:", value="No spoiler provided as argument!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    else:
        raise error
    await ctx.send(embed=embed)

@bot.command()
async def remind(ctx,duration,*,content:typing.Optional[str] = None):
    await ctx.send("Creating Reminder! :alarm_clock:")
    duration = float(duration)
    await ctx.send("Reminder Created! :alarm_clock:")
    # time.sleep(float(duration))
    time.sleep(duration)
    await ctx.send(ctx.author.mention)
    embed = discord.Embed(title="REMINDER!!! :alarm_clock:", description="{}".format("" if content is None else content),color=BOT_COLOR)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Reminder set by {}".format(ctx.author.name))
    await ctx.send(embed=embed)
@remind.error
async def remindError(ctx, error):
    embed = discord.Embed(color=ERROR_COLOR)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.add_field(name="ERROR :warning:", value="Missing arguments!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    elif isinstance(error, commands.CommandInvokeError):
        embed.add_field(name="ERROR :warning:", value="Pass time argument as seconds!\n Use {}help command for more info.".format(COMMAND_PREFIX))
        await ctx.send("Reminder not created! :alarm_clock:")
    else:
        raise error
    await ctx.send(embed=embed)



#FUN COMMANDS
@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))
@choose.error
async def chooseError(ctx, error):
    embed = discord.Embed(color=ERROR_COLOR)
    if isinstance(error, commands.CommandInvokeError):
        embed.add_field(name="ERROR :warning:", value="give something to choose!\n Use {}help command for more info.".format(COMMAND_PREFIX))
    else:
        raise error
    await ctx.send(embed=embed)

@bot.command()
async def flip(ctx):
    head_or_tails = ['HEADS','TAILS']
    await ctx.send("Flipping the :coin:! Make a call, Heads or Tails?")
    time.sleep(2)
    await ctx.send(":coin: **"+random.choice(head_or_tails)+"** it is!")

@bot.command()
async def rps(ctx):
    rps_choices = ['ROCK','PAPER','SCISSORS']
    await ctx.send("Let's see who win! Shall we? :smirk:")
    time.sleep(0.5)
    await ctx.send("ROCK... :rock:")
    time.sleep(1)
    await ctx.send("PAPER... :newspaper:")
    time.sleep(1)
    await ctx.send("SCISSORS... :scissors:")
    time.sleep(0.5)
    await ctx.send("Type your call if you haven't already!")
    time.sleep(2)
    bot_choice = random.choice(rps_choices)
    if bot_choice == 'ROCK':
        await ctx.send("I CHOOSE: **{}** :rock:".format(bot_choice))
    elif bot_choice == 'PAPER':
        await ctx.send("I CHOOSE: **{}** :newspaper:".format(bot_choice))
    elif bot_choice == 'SCISSORS':
        await ctx.send("I CHOOSE: **{}** :scissors:".format(bot_choice))

@bot.command()
async def meme(ctx):
    await ctx.send(getMemeURL())




bot.run(BOT_TOKEN)