import discord
import json


with open('discord.txt', 'r') as infile:
    discordkey = infile.read()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        channels = client.get_all_channels()
        for channel in channels:
            print("Channel: " + channel.name, channel.category)
            if channel.category == None:
                continue
            data = list()
            async for message in channel.history(limit=20000):
                #print(message.channel.name, message.author.name, message.content)
                info = {'author': message.author.name, 'date': str(message.created_at), 'content': message.content}
                data.append(info)
            with open(channel.name + '.json', 'w') as outfile:
                json.dump(data, outfile, indent=2)
        await client.close()


if __name__ == '__main__':
    print('Starting Discord Listener')
    client = MyClient()
    client.run(discordkey)