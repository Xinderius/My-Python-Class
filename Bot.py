import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
mensaje = None

bot = commands.Bot(command_prefix='$', intents=intents)

listamensajes = [
    '''Reducir al máximo las cosas que tiramos, como las bolsas de plástico; reutilizar todo 
    aquello que es aprovechable, como el jersey del hermano mayor, y guardar el papel o
      las latas para que se puedan reciclar.''',
      '''
Si reciclas, puedes reutilizar; si reutilizas, puedes reducir; 
si reduces, generarás un impacto importante sobre el medio ambiente
 y abrirás el camino seguro para que tus hijos y nietos puedan disfrutar de un 
 planeta limpio.
'''
'''Las «tres R«, nombre con el que habitualmente se conoce
 este circuito ecológico, tienen una dimensión cronológica 
 que se desenvuelve a lo largo del proceso del consumo:
   previo a la decisión de adquirir un producto, durante el uso de él 
   y una vez culminada su faceta productiva en la sociedad.''']

def mensajes():
    global mensaje
    mensaje = random.choice(listamensajes)

@bot.command()
async def rrr(ctx):
    mensajes()
    await ctx.send(mensaje)


bot.run("aca va el token")
