import discord
from phue import Bridge

# Initialize the Hue bridge
b = Bridge('192.168.0.2')
b.connect()
b.get_api()

# Set the brightness and saturation for two lights
b.set_light(10, {'bri': 254, 'sat': 254})
b.set_light(5, {'bri': 254, 'sat': 254})

INDEX = 0
MESSAGE = None

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.content == '>hue':
            global INDEX, MESSAGE
            INDEX = 0
            MESSAGE = await message.channel.send("What color would you like my room lights to be?", reference=message)
            # Add reactions to the message
            for emoji in ['⚪', '🔴', '🟡', '🟠', '🟢', '🔵', '🟣', '🌈']:
                await MESSAGE.add_reaction(emoji)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        global INDEX, MESSAGE
        INDEX += 1
        print(str(INDEX))
        if INDEX > 8:
            # Set the light effects to 'none' when index is greater than 8
            b.set_light(10, 'effect', 'none')
            b.set_light(5, 'effect', 'none')
            emoji = str(payload.emoji)
            color_mappings = {
                '⚪': 41477,
                '🔴': 0,
                '🟡': 10998,
                '🟠': 7359,
                '🟢': 22661,
                '🔵': 45614,
                '🟣': 49189,
                '🌈': 'colorloop'
            }
            if emoji in color_mappings:
                hue_value = color_mappings[emoji]
                # Set the hue value for both lights based on the selected emoji
                b.set_light(10, 'hue', hue_value)
                b.set_light(5, 'hue', hue_value)
                await MESSAGE.edit(content=f'Room colors have been changed to: {emoji} !')

client = MyClient()
client.run('YOUR_TOKEN')
