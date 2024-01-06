import discord
import os
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def kodland(ctx):
    await ctx.send(f'Kodlanda Hoşgeldiniz!')

@bot.command()
async def name(ctx):
    await ctx.send(f'Merhaba Ben alex')

@bot.command()
async def sa(ctx):
    await ctx.send(f'as hg!')

@bot.command()
async def slm(ctx):
    await ctx.send(f'as!')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'sanada merhaba!')
#API
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    with open('images/resim1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    with open('images/resim2.jpeg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('images/resim3.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('images/resim4.jpeg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def randommeme(ctx):
    resimler_listesi = os.listdir('images') #['resim1.jpg', 'resim2.jpeg', 'resim3.png','resim4.jpeg']
    with open(f'images/{random.choice(resimler_listesi)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run("MTE4NTYwODQ4MjMyNjU3NzE4Mg.GQWvl4.hSZe9ugJEDY82lV1Xqkt9Z9E8M5sUgSoEXa-oo")
