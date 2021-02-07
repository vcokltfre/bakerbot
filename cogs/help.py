import discord
from discord.ext import commands

class BakerHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Menu:",
            description="BakerBot is a discord multi-function bot designed to bring never-seen before fun features on discord!\n\n**Developers**\n`@vcokltfre#6868`\n`elf#2169`",
            color=0x87ceeb
        )
        cogs_to_display = []
        for cog, command in mapping.items():
            if not cog:
                continue
            if len(cog.get_commands()) > 0:
                cogs_to_display.append(f'`{cog.qualified_name}`')

        embed.add_field(name='**Modules**', value='\n'.join(cogs_to_display))
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(color=0x87ceeb)
        for command in cog.walk_commands():
            embed.add_field(name=command.qualified_name, value=f'{self.get_command_signature(command)}', inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_error_message(self, error):
        channel = self.get_destination()
        await channel.send(f":x: {error}")

    async def send_group_help(self, group):
        embed=discord.Embed(color=0x87ceeb)
        if isinstance(group, commands.Group):
            for command in group.commands:
                embed.add_field(name=command.qualified_name, value=self.get_command_signature(command), inline=False)
            channel = self.get_destination()
            await channel.send(embed=embed)

class HelpMenu(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(HelpMenu(bot))
