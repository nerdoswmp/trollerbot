import discord
import os
import random
import time
import math
import python_weather
import asyncio
import requests
import uuid
import shutil
from discord import Member
from discord.ext import commands, tasks
from itertools import cycle
from replit import db
from keep_alive import keep_alive
from test import mafs, operation
from sussifier import sussy

"""
https://pythonrepo.com/repo/nextcord-nextcord << u
https://discord-interactions.readthedocs.io/en/unstable/quickstart.html#installing
"""
# LISTA DE PALAVRA PRA ATIVAR O SEXO
zap = ['sexo','https://www.youtube.com/watch?v=QBFZyq3FRuw','https://youtu.be/QBFZyq3FRuw','Dennis e Cantini - Isso Que É Vida','pau no cu','pau no seu cu', 'meu cu', 'meu pau']

# IMAGENS ENVIADAS POR CAUSA DO SEXO
zapzap = ['https://cdn.discordapp.com/attachments/838913100483657728/868290803125067848/E66MgqBVoA8ICAB.png','https://media.discordapp.net/attachments/818907430560989264/864341396566704158/E6JHDobWQAoG_p8.png?width=449&height=473','https://cdn.discordapp.com/attachments/838913100483657728/868291184844492821/E66NxioVUAMVHlX.png','https://cdn.discordapp.com/attachments/838913100483657728/868291215894917133/E66sAAdWUAMggN-.png','https://cdn.discordapp.com/attachments/838913100483657728/868291248744726528/E662Z5tWUAwF_kJ.png','https://cdn.discordapp.com/attachments/838913100483657728/868291520762097664/9memrTmHKgxPTq8i.mp4']

# VSF
vsfs = ['vsf', 'vai se foder', 'vai se fuder', 'vai toma no cu', 'vtmnc']

# VIDEOS DO LOL
epic = ['https://cdn.discordapp.com/attachments/818907430560989264/818907457724219392/jtl_d_7tf4mds2dc.mp4', 'https://cdn.discordapp.com/attachments/818907430560989264/859834749157900338/VKYZVryDlObGOQD3.mp4','https://cdn.discordapp.com/attachments/818907430560989264/888660762124488744/4FG41C3qkZYqQSdY.mp4']

# PRIMEIRO ITEM DO =BASED
comedy_list = ['https://cdn.discordapp.com/attachments/470327818056892428/819171515706769408/IMG-20210309-WA0075.jpg']

swag_list = []

# DATABASE #

def update_based(based_msg):
  if "based" in db.keys():
    based = db["based"]
    based.append(based_msg)
    db["based"] = based
  else:
    db["based"] = [based_msg]

def delete_based(index):
  based = db["based"]
  if len(based) > index:
    del based[index]
    db["based"] = based

def update_pasta(pasta_txt):
  if "pasta" in db.keys():
    pasta = db["pasta"]
    pasta.append(pasta_txt)
    db["pasta"] = pasta
  else:
    db["pasta"] = [pasta_txt]

def delete_pasta(index):
  pasta = db["pasta"]
  if len(pasta) > index:
    del pasta[index]
    db["pasta"] = pasta

# INICIALIZADOR DO CLIENT
client = discord.Client()

@client.event
async def on_ready():
  change_status.start()
  print('We do a little trolling as {0.user}'.format(client))

# STATUS DE ATIVIDADE

status = cycle(['=help for cmds', '@nerdoswamp please', 'shoutouts to my boy @StarPrankster', 'kasinoooo', 'amongrus', 'commanderbot 1v1 me'])

@tasks.loop(seconds=60)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

# FUNC PARA OS COMANDOS
@client.event
async def on_message(message):
  if message.author == client.user:
    return

# ID DO CANAL PRA MANDAR MSG PELO TROLLER
  updated = client.get_channel(883869143873490975)

# VALOR PRO COMANDO =TROLLING FALSE/TRUE
  if "trolling" not in db.keys():
    db["trolling"] = True

# ITENS RELACIONADOS À DATABASE DE COPYPASTA
  pastaopt = swag_list
  if "pasta" in db.keys():
    pastaopt = pastaopt + db["pasta"]

  if message.content.startswith('=pasta'):
    randommsg = str(random.choice(pastaopt))
    await message.channel.send(f"```\n{randommsg}\n ``` ```css\n-Item number {pastaopt.index(randommsg)} in the databased\n```")
  
  if message.content.startswith("=padd"):
    pasta_txt = message.content.split("=padd ",1)[1]
    update_pasta(pasta_txt)
    await message.channel.send("added to the pastas")
    await updated.send(pasta_txt)

  if message.content.startswith("=pdel"):
    pasta = []
    if "pasta" in db.keys():
      index = int(message.content.split("=pdel",1)[1])
      delete_pasta(index)
      pasta = db["pasta"]
      await message.channel.send("```number of things on the database is: ``` ```"+str(len(pasta))+"```")

  if message.content.startswith("=plist"):
    pasta = []
    if "pasta" in db.keys():
      pasta = db["pasta"]
      await message.channel.send("```number of things on the database is: ``` ```"+str(len(pasta))+"```")

  if message.content.startswith("=frompasta"):
    pasta = []
    if "pasta" in db.keys():
      valuep = int(message.content.split("=frompasta",1)[1])
      pasta = db["pasta"]
      await message.channel.send(str(pasta.pop(valuep)))

# RESPONDER LOL E MANDAR ELE CALAR A BOCA
  if db["trolling"]:
    if message.content.startswith('lol'):
      random_lol = random.choice(epic)
      await message.channel.send(random_lol)

    # RESPONDER VSF
    if any(word in message.content for word in vsfs):
      await message.channel.send('vai vc')

    # RESPONDER SEXO
    if any(word in message.content for word in zap):
      await message.channel.send(random.choice(zapzap))

  if message.content.startswith("=trolling"):
    value = message.content.split("=trolling ", 1)[1]

    if value.lower() == "true":
      db["trolling"] = True
      await message.channel.send("We do a little trolling")
    elif value.lower() == "false":
      db["trolling"] = False
      await message.channel.send("dame dane")

# COISAS RELACIONADAS À DATABASED PADRÃO
  options = comedy_list
  if "based" in db.keys():
    options = options + db["based"]
#
  if message.content.startswith('=based'):
    randombased = random.choice(options)
    await message.channel.send(f"{randombased} ```css\n-Item number {options.index(randombased)-1} in the databased\n```")
#
  if message.content.startswith("=add"):
    based_msg = message.content.split("=add ",1)[1]
    update_based(based_msg)
    await message.channel.send("added to the pile")
    await updated.send(based_msg)
#
  if message.content.startswith("=del"):
    based = []
    if "based" in db.keys():
      index = int(message.content.split("=del",1)[1])
      delete_based(index)
      based = db["based"]
      await message.channel.send("```number of things on the database is: ``` ```"+str(len(based))+"```")
#
  if message.content.startswith("=list"):
    based = []
    if "based" in db.keys():
      based = db["based"]
      await message.channel.send("```number of things on the database is: ``` ```"+str(len(based))+"```")
#
  if message.content.startswith("=fromlist"):
    based = []
    if "based" in db.keys():
      value = int(message.content.split("=fromlist",1)[1])
      based = db["based"]
      await message.channel.send(str(based.pop(value)))

# ENVIAR LISTA DE COMANDOS
  if message.content.startswith("=cmd"):
    await message.channel.send("```css\n"
    "['=list', '=fromlist', '=add', '=del', '=based', '=pasta', '=padd', '=pdel', '=plist', '=frompasta', '=color', '=rcolor', '=op', '=exame', '=png', '=weather'  and '=pfp'] are the commands avaliable\n""```")

# ENVIAR LINK DO SITE DE AJUDA
  if message.content.startswith("=help"):
    green = int('A8E916', 16)
    embed=discord.Embed(title="documentation", url="https://nerdoswamp.neocities.org",description= 'https://nerdoswamp.neocities.org << click this link for an example and explanation on each command' ,color=green)
    await message.channel.send(embed=embed)

# EXAME DE CRINGE ANA MARIA BRAGA
  if message.content.startswith("=exame"):
    user = str(message.author.mention)
    user2 = str(message.author)
    resultado = random.randint(0,100)
    await message.channel.send(f'###Examinando {user2}')
    time.sleep(0.5)
    await message.channel.send('###Coletando cringe sanguineo')
    time.sleep(0.5)
    await message.channel.send('###Extraindo based')
    time.sleep(0.5)
    await message.channel.send('###Examinando pureza')
    time.sleep(1)
    await message.channel.send(f'*** {user} é {resultado} % cringe ***')
    time.sleep(3)
    await message.channel.send('Fonte: https://media.discordapp.net/attachments/818907430560989264/859827321807437864/unknown.png?width=1198&height=676')

# COMANDO DE CLIMA =WEATHER
  if message.content.startswith("=weather"):
    city = (message.content.split("=weather ",1)[1])
    Wclient = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await Wclient.find(city)
    temper = weather.current.temperature
    conditions = weather.current.sky_text
    if temper <= 15:
      imgs = [' https://media.discordapp.net/attachments/818907430560989264/859856960026968084/a1a2b48d-0648-4d6f-8952-41b46ad9a68e.png?width=545&height=676', ' https://cdn.discordapp.com/attachments/818907430560989264/859867533296795678/282b0274-d21a-4cbb-85b2-c65783c2665c.png']
      context = random.choice(imgs)
      await message.channel.send(f'It is {conditions} in {city}, currently {temper} ºC')
      time.sleep(0.1)
      await message.channel.send(context)
    elif temper >= 25:
      context = ' https://staticr1.blastingcdn.com/media/photogallery/2016/10/21/660x290/b_1200x680/a-internet-nao-perdoou-o-calor-da-ultima-semana_933227.jpg'
      await message.channel.send(f'It is {conditions} in {city}, currently {temper} ºC')
      time.sleep(0.1)
      await message.channel.send(context)
    else:
      await message.channel.send(f'It is {conditions} in {city}, currently {temper} ºC')
      time.sleep(0.1)
      await message.channel.send('https://thumbs.dreamstime.com/z/bald-man-thumbs-up-26364248.jpg')
    await Wclient.close()

# RETORNAR COR
  if message.content.startswith("=color"):
    cvalue = (message.content.split("=color ",1)[1])
    hexd = int(cvalue, 16)
    embed=discord.Embed(title=cvalue, url="https://www.webfx.com/web-design/random-color-picker/#"+cvalue, description="https://www.webfx.com/web-design/random-color-picker/#"+cvalue, color=hexd)
    await message.channel.send(embed=embed)

# RETORNAR COR ALEATÓRIA
  if message.content.startswith("=rcolor"):
    r = lambda: random.randint(0,255)
    hvalue = ('%02X%02X%02X' % (r(),r(),r()))
    hexd = int(hvalue, 16)
    embed=discord.Embed(title=hvalue, url="https://www.webfx.com/web-design/random-color-picker/#"+hvalue, description="https://www.webfx.com/web-design/random-color-picker/#"+hvalue, color=hexd)
    await message.channel.send(embed=embed)

# CALCULADORA
  if message.content.startswith("=op"):
    val = message.content.split("=op ",1)[1]
    res1, oper, res2 = val.split()
    await message.channel.send(operation(res1, oper, res2))

# RAIZ QUADRADA
  if message.content.startswith("=root"):
    num = int(message.content.split("=root ",1)[1])
    await message.channel.send(mafs(num))

# RETORNAR PFP
  if message.content.startswith("=pfp"):
    await message.channel.send(message.author.avatar_url)

# SUSSIFICADOR DE IMAGENS
  if message.content.startswith("=png"):
    busy = False
    while busy == False:
      busy = True
      await message.channel.send("Sussy Balls-ifying your image")
      async with message.channel.typing():
        try:
          url = message.attachments[0].url
        except IndexError:
          print("error")
          await message.channel.send("no image detected")
        else:
          if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            imageName = str(uuid.uuid4()) + '.jpg'
            with open(imageName, 'wb') as out_file:
              print('Saving image: '+imageName)
              shutil.copyfileobj(r.raw, out_file)
              sussy(imageName)
              os.remove(imageName)
              try:
                with open('out.gif', 'rb') as fp:
                  user = str(message.author.mention)
                  await message.channel.send(user, file=discord.File(fp, 'out.gif'))
                  busy = False
                  break
              except Exception as error:
                print(error)
                await message.channel.send("something went wrong my bad")
                busy = False
                break


# ENVIAR MSG NO SERVER
  if message.content.startswith('=ç'):
    txt = message.content.split("=ç ",1)[1]
    channel = client.get_channel(777541120963379202)
    await channel.send(txt)

keep_alive()
client.run(os.getenv('deeznuts'))

# test
# test 2