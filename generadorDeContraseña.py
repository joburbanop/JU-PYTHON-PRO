import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repetirMensaje(ctx,*,mesaje):
    await ctx.send(mesaje)
    
@bot.command()
async def guardar_y_enviar(ctx,*,texto):
    canal_id="1229596545687621694"

    canal_destino=bot.get_channel(int(canal_id))

    if canal_destino is None:
        await ctx.send("el canal no existe")
        return
    await canal_destino.send(texto)
    
    await  ctx.send("mensaje enviado al canal juegos")


bot.run("MTIyOTU5ODA5NDg3ODgzODgyNQ.GWx-dd.z7WuJV0d2MlmIX3ZDkc-oNVjK4NQrahpt-um2k")
