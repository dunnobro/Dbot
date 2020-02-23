import discord

client = discord.Client()


@client.event
async def on_message(message):
    print(message.content)  # Now every message sent will be printed to the console


client.run("NjgwOTc4NTY4MTA4NzAzNzYw.XlH7ew.BHJ3DgOJGYb6UU6j8z5rjh5YiM4")
