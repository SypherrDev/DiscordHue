import discord
from phue import Bridge

b = Bridge('192.168.0.2')
b.connect()
b.get_api()
b.set_light(10, 'bri', 254)
b.set_light(10, 'sat', 254)
b.set_light(5, 'bri', 254)
b.set_light(5, 'sat', 254)



INDEX = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.content == '>hue':
            global INDEX
            global MESSAGE
            INDEX = 0
            MESSAGE = await message.channel.send("What color would you like my room lights to be?", reference=message)
            await MESSAGE.add_reaction('⚪')
            await MESSAGE.add_reaction('🔴')
            await MESSAGE.add_reaction('🟡')
            await MESSAGE.add_reaction('🟠')
            await MESSAGE.add_reaction('🟢')
            await MESSAGE.add_reaction('🔵')
            await MESSAGE.add_reaction('🟣')
            await MESSAGE.add_reaction('🌈')

    
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        global INDEX
        INDEX += 1
        print(str(INDEX))
        if(INDEX > 8):
            b.set_light(10, 'effect', 'none')
            b.set_light(5, 'effect', 'none')
            if(str(payload.emoji) == str("⚪")):
                b.set_light(10, 'hue', 41477)
                b.set_light(5, 'hue', 41477)
                await MESSAGE.edit(content='Room colors have been changed to: ⚪ !')
            
            if(str(payload.emoji) == str("🔴")):
                b.set_light(10, 'hue', 0)
                b.set_light(5, 'hue', 0)
                await MESSAGE.edit(content='Room colors have been changed to: 🔴 !')
            
            if(str(payload.emoji) == str("🟡")):
                b.set_light(10, 'hue', 10998)
                b.set_light(5, 'hue', 10998)
                await MESSAGE.edit(content='Room colors have been changed to: 🟡 !')
            
            if(str(payload.emoji) == str("🟠")):
                b.set_light(10, 'hue', 7359)
                b.set_light(5, 'hue', 7359)
                await MESSAGE.edit(content='Room colors have been changed to: 🟠 !')
            
            if(str(payload.emoji) == str("🟢")):
                b.set_light(10, 'hue', 22661)
                b.set_light(5, 'hue', 22661)
                await MESSAGE.edit(content='Room colors have been changed to: 🟢 !')
            
            if(str(payload.emoji) == str("🔵")):
                b.set_light(10, 'hue', 45614)
                b.set_light(5, 'hue', 45614)
                await MESSAGE.edit(content='Room colors have been changed to: 🔵 !')
            
            if(str(payload.emoji) == str("🟣")):
                b.set_light(10, 'hue', 49189)
                b.set_light(5, 'hue', 49189)
                await MESSAGE.edit(content='Room colors have been changed to: 🟣 !')

            if(str(payload.emoji) == str("🌈")):
                b.set_light(10, 'effect', 'colorloop')
                b.set_light(5, 'effect', 'colorloop')
                await MESSAGE.edit(content='Room colors have been changed to: 🌈 !')
            

                



client = MyClient()
client.run('OTUzMzc4NjMwOTUwNTg0MzQx.GtC0bL.NZgr4T8bPeBh6MJRJ4jw6RUIwLRBTe4D4slhyI')