import discord
from discord import app_commands
import json


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=ur guild here))
    print("Ready!")

BOT_TOKEN = "ur token here"
CUSTOMER_ROLE = "Subscriber"
DEFAULT_COLOR = 0xFF0000

@tree.command(
    name="link",
    description="Connect your token to our server",
    options=[
        app_commands.CommandOption(
            type=app_commands.OptionType.STRING,
            name="token",
            description="Your bot token",
            required=True,
        ),
    ],
)
async def link_command(interaction: app_commands.CommandInteraction, token: str):
    with open("users.json", "r") as f:
        users = json.load(f)

    if interaction.user.id not in users:
        users[interaction.user.id] = {"token": token, "discord_id": interaction.user.id}

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    await interaction.response.send_message("Your token has been saved.")


client.run(BOT_TOKEN)