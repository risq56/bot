import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)

token = ""

@bot.event
async def on_ready():
    print(f"""{Fore.RED}
███████     ████████       ████████████   {Fore.CYAN}  ████████████    {Fore.CYAN}    ████████████      {Fore.RED} ██          ██
██    ██       ██          ██               ██                  ██                 ██          ██
██    ██       ██          ██               ██                  ██                 ██          ██
██████       {Fore.RED}  ██          ██      █████    ██      █████     {Fore.RED}  █████████        {Fore.CYAN}  ██████████████
██             ██          ██         ██    ██         ██       ██                 ██          ██
██          ████████       ████████████     ███████████        {Fore.CYAN} ████████████       ██         {Fore.RED} ██""")

@bot.command()
async def dm(ctx):
    mention = ctx.author.mention
    embed=discord.Embed(title=f"Hello {mention} we are so happy to announce you that our spoofer is finaly released", description="**It's now or never !!!**\nIf you are interested you should go check the server <#861226650373062676> ", color=0x246aec)
    dm_message = "https://discord.gg/uPrayaUEe5"
    message = f"Hello {mention} we are so happy to announce you that our spoofer is finaly released\n\n**IT'S NOW OR NEVER !!!**\n\nIf you are interested you should go check the server <#861226650373062676> \n\nhttps://discord.gg/uPrayaUEe5"
    await ctx.message.delete()
    usernamessd = open("den_usernammes.txt","r")
    g = usernamessd.readlines()
    d = []
    for i in g:
        i = i.rstrip()
        d.append(i)
    print(d)
    usernamessd.close()
    con_usernamessd = open("den_usernammes.txt","r")
    con_g = con_usernamessd.readlines()
    con_d = []
    for i in con_g:
        i = i.rstrip()
        con_d.append(i)
    print(con_d)
    con_usernamessd.close()

    for member in ctx.guild.members:
        try:
            
            if str(member.id) in d:
                print(f"already dmed {member}")
                pass
            if member.id == bot.user.id:
                pass
            elif str(member.id) not in d:
                usernames = open("con_usernammes.txt","a")
                gogo = member.mention
                message = f"Hello {gogo} we are so happy to announce you that our spoofer is finaly released\n\n**IT'S NOW OR NEVER !!!**\n\nIf you are interested you should go check the server <#861226650373062676> \n\nhttps://discord.gg/uPrayaUEe5"
                await member.send(message)
                print(f"Sent to {member}")
                usernammes.writelines(str(member.id)+"\n")
                # To not be rate limited
                await asyncio.sleep(1)
            elif str(member.id) in con_d:
                print(f"already dmed {member}")
                pass
            elif str(member.id) not in con_d:
                usernames = open("con_usernammes.txt","a")
                gogo = member.mention
                message = f"Hello {gogo} we are so happy to announce you that our spoofer is finaly released\n\n**IT'S NOW OR NEVER !!!**\n\nIf you are interested you should go check the server <#861226650373062676> \n\nhttps://discord.gg/uPrayaUEe5"
                await member.send(message)
                print(f"Sent to {member}")
                usernammes.writelines(str(member.id)+"\n")
                # To not be rate limited
                await asyncio.sleep(1)
        except:
            usernames = open("den_usernammes.txt","a")
            print(f"Couldn't send to {member}")
            usernames.writelines(str(member.id)+"\n")

bot.run("")




