import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

resposta = get_class("keras_model.h5", "labels.txt", "Gato_IA.png")
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou o bot {bot.user}!')

@bot.command()
async def imagem(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./images/{file_name}")
            
            # Chama a função do model.py para classificar a imagem
            classe, confianca = get_class(
                model_path=f"./keras_model.h5", 
                labels_path=f"./labels.txt", 
                image_path=f"./images/{file_name}"
            )
            
            await ctx.send(f"Achei que é: **{classe}** com {confianca * 100:.2f}% de certeza!")
    else:
        await ctx.send("Você não enviou uma imagem!")

bot.run("MTU0ODMyOTMzMjU5NjkzMjcxOQ.G9inn5.b7_HXOMRTDNxmIdVCL70dNKc7IwOWz9NYizdYw")