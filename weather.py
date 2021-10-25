import discord
import python_weather
import time

async def weather(city, msg):
    Wclient = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await Wclient.find(city)
    temper = weather.current.temperature
    conditions = weather.current.sky_text
    if temper <= 15:
      imgs = [' https://media.discordapp.net/attachments/818907430560989264/859856960026968084/a1a2b48d-0648-4d6f-8952-41b46ad9a68e.png?width=545&height=676', ' https://cdn.discordapp.com/attachments/818907430560989264/859867533296795678/282b0274-d21a-4cbb-85b2-c65783c2665c.png']
      context = random.choice(imgs)
      await msg.channel.send(f'It is {conditions} in {city}, currently {temper} ºC')
      time.sleep(0.1)
      await msg.channel.send(context)
    elif temper >= 25:
      context = ' https://staticr1.blastingcdn.com/media/photogallery/2016/10/21/660x290/b_1200x680/a-internet-nao-perdoou-o-calor-da-ultima-semana_933227.jpg'
      await msg.channel.send(f'It is {conditions} in {city}, currently {temper} ºC')
      time.sleep(0.1)
      await msg.channel.send(context)
    else:
      await msg.channel.send(f'It is {conditions} in {city}, currently {temper} ºC')
      time.sleep(0.1)
      await msg.channel.send('https://thumbs.dreamstime.com/z/bald-man-thumbs-up-26364248.jpg')
    await Wclient.close()