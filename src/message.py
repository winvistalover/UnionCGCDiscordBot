from textwrap import wrap
import nextcord as discord
from nextcord.ext import commands


@client.event
async def on_message(message):
    # if client.user in message.mentions or message.channel.id in channels:
    if message.channel.id in channels and not message.content.startswith("//"):
        print(f"[ INFO ] Processing message '{message}'...")
        # for guild in client.guilds:
        for channel in channels:
            author = ""

            if str(owner) in str(message.author.id):
                author = f"{message.author.display_name} -  Owner"
            else:
                if message.author.id in staff:
                    author = f"{message.author.display_name} - Staff"
                else:
                    author = f"{message.author.display_name}"
            if message.reference is not None:
                referenced_message = await message.channel.fetch_message(
                    message.reference.message_id
                )
                original_author = referenced_message.embeds[0].author.name
                original_content = referenced_message.embeds[0].description
                if not message.content.startswith("https://tenor.com/view"):
                    embed = discord.Embed(
                        description=(
                            f"**Reply from {message.author.display_name}:**\n{message.content}\n\n**Original message by {original_author}:**\n {original_content}"
                        ),
                        color=discord.Color.random(),
                    )
                else:
                    embed = discord.Embed(
                        description=(
                            f"**Reply from {message.author.display_name}:**\n\n**Original message by {original_author}:**\n {original_content}"
                        ),
                        color=discord.Color.random(),
                    )
            else:
                if not message.content.startswith("https://tenor.com/view"):
                    embed = discord.Embed(
                        description=(f"{message.content}"),
                        color=discord.Color.random(),
                    )
                else:
                    embed = discord.Embed(
                        color=discord.Color.random(),
                    )

            if message.content.startswith("https://tenor.com/view"):
                embed.set_image(url=tenorgrabber.getgiflink(message.content))
            embed.set_author(name=author)
            embed.set_thumbnail(url=message.author.avatar)
            embed.set_footer(
                text=f"{message.guild.name} - {round(client.latency * 1000)}ms",
                icon_url=message.guild.icon,
            )
            try:
                print(
                    f"[ INFO ] userid: {message.author.id}, bot: {message.author.bot}"
                )
                if message.author.id == 975365560298795008:
                    msg = await client.get_channel(channel).send(embed=embed)
                    for mention in message.mentions:
                        await client.get_channel(channel).send(
                            f"<@{mention.id}> mentioned you in the above message!"
                        )
                    print(f"[ INFO ] Sent message in {message.guild}, {channel}.")
                    for attachment in message.attachments:
                        await client.get_channel(channel).send(
                            f"<@{message.author.id}> attachments don't work right now."
                        )
                    print(f"[ INFO ] Added attachments.")
                    await message.delete()
                    print("[ INFO ] Deleted OG message.")
                else:
                    if not message.author.bot:
                        msg = await client.get_channel(channel).send(embed=embed)
                        for mention in message.mentions:
                            await client.get_channel(channel).send(
                                f"<@{mention.id}> mentioned you in the above message!"
                            )
                        print(f"[ INFO ] Sent message in {message.guild}, {channel}.")
                        for attachment in message.attachments:
                            await client.get_channel(channel).send(
                                f"<@{message.author.id}> attachments don't work right now."
                            )
                        print(f"[ INFO ] Added attachments.")
                        await message.delete()
                        print("[ INFO ] Deleted OG message.")
            except discord.NotFound:
                pass
