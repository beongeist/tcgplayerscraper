import discord
import actions
import config
import mysql.connector



async def send_message(message, user_message, is_private):
    try:
        response = actions.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = config.my_token
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if (message.author.bot) or not (message.content.startswith('!') or message.content.startswith('?')):
            print(str(message.channel.name) == "bot-commands")

            print(isinstance(message.channel, discord.TextChannel))
            print((message.author.bot))
            print(message.content.startswith('!'))
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
