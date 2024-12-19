import discord
from discord.ext import commands

permisos=discord.Intents.default()
permisos.message_content=True

bot=commands.Bot(command_prefix="@", intents=permisos)

@bot.event
async def on_ready():
    print("El bot esta en linea")

bot.run("TOKEN")

@bot.command()
async def bienvenidos(ctx):
    await ctx.send("Bienvenido a tu bot \n Aqui puedes encontrar diferentes informaciones sobre el medio ambiente")

@bot.command()
async def descomposicion(ctx,*,objetos:str):
    tiempo_descompocision={
        "papel":"2 a 6 meses"
        "carton":"2 meses"
        "vidrio":"4000 años"
    }
    objeto=objeto.lower()
    if objeto in tiempo_descompocision:
        await ctx.send(f"El tiempo de descompi es : {tiempo_descompocision[objeto]}")
    else:
        await ctx.send("No tengo informacion sobre ese elmentos")
        bot.run("MTMxMDc3NTUzMzE3NjYyMzIwNA.GN-j17.nr4_p_DN9S2NIzA9Sdom7YcO9jSbGrK9YFDyo8")





bot.run("TOKEN")
