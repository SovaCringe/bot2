from setting import *
import discord
from discord.ext import commands
from discord import app_commands
import json
from pip._vendor import requests
import asyncio
import random
import time
import logging
from datetime import datetime, timezone, timedelta
from webserver import keep_alive
import os
from redditSave import saveReddit

logging.basicConfig(
    filename=
    f"logs/{datetime.now(timezone(timedelta(hours=3))).strftime('%d_%m_%Y_%H-%M')}.log",
    filemode='w',
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%d.%b.%y %H:%M:%S',
    level=logging.INFO)

f = open('config.json', 'r', encoding='UTF-8')
data = json.load(f)
f.close()


def dumpJson(data_):
    f = open(f'config.json', 'w', encoding='UTF-8')
    json.dump(data_, f)
    f.close()


def no_rights(interaction):
    embed = discord.Embed(color=0xff8800, description="Недостаточно прав!")
    embed.set_author(name=interaction.user.name,
                     icon_url=interaction.user.display_avatar)
    return embed


def txt_embed(interaction, text):
    embed = discord.Embed(color=0xff8800, description=text)
    embed.set_author(name=interaction.user.name,
                     icon_url=interaction.user.display_avatar)
    return embed


client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)


async def checkRPOff():
    for category in data["rp_off"]:
        try:
            for member_ in data["rp_off"][category]:
                if data["rp_off"][category][member_] != None:
                    if data["rp_off"][category][member_] < time.time():
                        del data["rp_off"][category][member_]
                        dumpJson(data)
        except Exception as e:
            logging.error(e)


async def reactionCheck(guild, channel):
    async for message in channel.history(limit=5):
        try:
            if message != None:
                reactions = message.reactions
                if not client.get_emoji("\u2795") in reactions:
                    await message.add_reaction("\u2795")
                if not client.get_emoji("\u2796") in reactions:
                    await message.add_reaction("\u2796")
            if channel.id != data["suggestion_channel"]:
                channel = guild.get_channel(data["suggestion_channel"])
        except Exception as e:
            logging.error(e)


async def asyncCheck():
    guild = client.get_guild(876384198846476288)
    channel = guild.get_channel(data["suggestion_channel"])
    while True:
        await reactionCheck(guild, channel)
        await checkRPOff()
        await asyncio.sleep(5)


@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} запустился!')
    await asyncCheck()


@tree.command(name="clear-logs", description="Очистить логи.")
async def clear_logs(interaction: discord.Interaction):
    if interaction.user.id != 648125700003332107:
        return

    dirPath = 'logs'
    for f in os.listdir(dirPath):
        os.remove(os.path.join(dirPath, f))

    await interaction.response.send_message(
        embed=txt_embed(interaction, "логи почищены"))


@tree.command(name="edit-role-color",
              description="Изменить цвет кастомной роли.")
async def edit_role_color(interaction: discord.Interaction, color: str):
    user = interaction.user

    f = open('custom_roles.json', 'r', encoding='UTF-8')
    data = json.load(f)
    f.close()
  
    if not str(user.id) in data.keys():
        await interaction.response.send_message(
            embed=txt_embed(interaction, "У вас нет кастомной роли."))
        return

    try:
        role = interaction.guild.get_role(data[str(user.id)])
        color_ = int(color, 16)
        await role.edit(color=color_)
    except:
        await interaction.response.send_message(
            embed=txt_embed(interaction, "Ошибка."))
        return

    await interaction.response.send_message(embed=txt_embed(
        interaction,
        f"Цвет роли <@&{role.id}> был изменён на #{color}."))


@tree.command(name="edit-role-name",
              description="Изменить название кастомной роли.")
async def edit_role_name(interaction: discord.Interaction, new_name: str):
    user = interaction.user

    f = open('custom_roles.json', 'r', encoding='UTF-8')
    data = json.load(f)
    f.close()

    if not str(user.id) in data.keys():
        await interaction.response.send_message(
            embed=txt_embed(interaction, "У вас нет кастомной роли."))
        return

    try:
        role = interaction.guild.get_role(data[str(user.id)])
        await role.edit(name=new_name)
    except:
        await interaction.response.send_message(
            embed=txt_embed(interaction, "Ошибка."))
        return

    await interaction.response.send_message(embed=txt_embed(
        interaction,
        f"Название кастомной роли было изменено на <@&{role.id}>."))


@tree.command(name="add-custom-role", description="Добавить кастомную роль.")
async def add_custom_role(interaction: discord.Interaction,
                          member: discord.Member, role: discord.Role):
    user = interaction.user
    if not user.top_role.permissions.administrator:
        await interaction.response.send_message(embed=no_rights(interaction))
        return

    f = open('custom_roles.json', 'r', encoding='UTF-8')
    data = json.load(f)
    f.close()

    data[str(member.id)] = role.id

    try:
        f = open(f'custom_roles.json', 'w', encoding='UTF-8')
        json.dump(data, f)
        f.close()
    except:
        await interaction.response.send_message(embed=txt_embed(interaction, "Ошибка."))
        return

    await interaction.response.send_message(embed=txt_embed(
        interaction,
        f"Кастомная роль <@&{role.id}> была установлена для <@{member.id}>."))


@tree.command(name="russian-roulette",
              description="Сыграть в русскую рулетку.")
async def russian_roulette(interaction: discord.Interaction):
    if random.randint(1, 6) != 1:
        await interaction.response.send_message("_щёлк_")
        return
    member = interaction.user
    guild = interaction.guild
    try:
        await member.timeout(timedelta(seconds=30), reason="Русская рулетка")
    except:
        embed = discord.Embed(color=0xff8800, description="Ошибка.")
        embed.set_author(name=interaction.user.name,
                         icon_url=interaction.user.display_avatar)
        await interaction.response.send_message(embed=embed)

@tree.command(name="avatar", description="Показать аватар.")
async def avatar(interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user
    embed = discord.Embed(color=0xff8800)
    embed.set_image(url=member.display_avatar)
    await interaction.response.send_message(embed=embed)


@tree.command(name="user", description="Информация о каком-либо пользователе.")
async def user_(interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user
    embed = discord.Embed(color=0xff8800)
    embed.set_author(
        name=
        f"Информация о {member.nick if member.nick != None else member.name}",
        icon_url=interaction.user.display_avatar)
    embed.set_thumbnail(url=member.display_avatar)
    embed.set_footer(text=f"Id: {member.id}")
    embed.add_field(
        name="Имя пользователя:",
        value=
        f"{member.nick if member.nick != None else member.name} ({member.name})",
        inline=False)
    embed.add_field(name="Высшая роль:",
                    value=f"<@&{member.top_role.id}>",
                    inline=False)
    embed.add_field(name="Присоединился к серверу:",
                    value=f"<t:{round(member.joined_at.timestamp())}>",
                    inline=False)
    embed.add_field(name="Регистрация аккаунта:",
                    value=f"<t:{round(member.created_at.timestamp())}>",
                    inline=False)
    await interaction.response.send_message(embed=embed)


@tree.command(name="serverinfo", description="Информация о сервере.")
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(color=0xff8800)
    embed.set_author(name=f"Информация о сервере {guild.name}",
                     icon_url=guild.icon)
    embed.set_thumbnail(url=guild.icon)
    embed.set_footer(text=f"server id: {guild.id}")
    people_count = 0
    for member in guild.members:
        if not member.bot:
            people_count += 1
    text1 = f"""
    Всего: {guild.member_count}
    Людей: {people_count}
    Ботов: {guild.member_count - people_count}
    """
    embed.add_field(name="участники:", value=text1, inline=False)

    text2 = f"""
    Всего: {len(guild.voice_channels) + len(guild.text_channels)}
    Текстовых: {len(guild.text_channels)}
    Голосовых: {len(guild.voice_channels)}
    """
    embed.add_field(name="Каналы:", value=text2, inline=False)
    embed.add_field(name="Владелец:",
                    value=f"<@{guild.owner_id}>",
                    inline=False)
    embed.add_field(name="Дата создания:",
                    value=f"<t:{round(guild.created_at.timestamp())}>",
                    inline=False)
    await interaction.response.send_message(embed=embed)


def parsTimeStr(time):
    time_ = 0
    if time[len(time) - 1].lower() == 'm':
        try:
            time_ = int(time[:len(time) - 1]) * 60
            if time_ < 0:
                return -1
        except:
            return -1
    elif time[len(time) - 1].lower() == 'h':
        try:
            time_ = int(time[:len(time) - 1]) * 3600
            if time_ < 0:
                return -1
        except:
            return -1
    return time_

"""
@tree.command(name="hug-off",
              description="Выключить команду /hug для использования на себе.")
async def hug_off(interaction, time_: str = "0m"):
    global data
    time_ = parsTimeStr(time_)
    if time_ == -1:
        embed = txt_embed(interaction, "Ошибка! Указано некорректное время")
        await interaction.response.send_message(embed=embed)
        return
    data["rp_off"]["hug"][str(
        interaction.user.id)] = time.time() + time_ if time_ != 0 else None
    dumpJson(data)
    if time_ != 0:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!hug` до <t:{round(time.time() + time_)}>"
        )
    else:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!hug` до неопределённого времени")
    await interaction.response.send_message(embed=embed)


@tree.command(name="hug-on",
              description="Включить команду /hug для использования на себе.")
async def hug_on(interaction: discord.Interaction):
    global data
    author = interaction.user
    if str(author.id) in data["rp_off"]["hug"]:
        del data["rp_off"]["hug"][str(author.id)]
        dumpJson(data)
        embed = txt_embed(interaction, "Вы разблокировали команду `t!hug`")
        await interaction.response.send_message(embed=embed)
        return
    embed = txt_embed(interaction, "Команда `t!hug` не заблокирована")
    await interaction.response.send_message(embed=embed)


@tree.command(name="kiss-off",
              description="Выключить команду /kiss для использования на себе.")
async def kiss_off(interaction, time_: str = "0m"):
    global data
    time_ = parsTimeStr(time_)
    if time_ == -1:
        embed = txt_embed(interaction, "Ошибка! Указано некорректное время")
        await interaction.response.send_message(embed=embed)
        return
    data["rp_off"]["kiss"][str(
        interaction.user.id)] = time.time() + time_ if time_ != 0 else None
    dumpJson(data)
    if time_ != 0:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!kiss` до <t:{round(time.time() + time_)}>"
        )
    else:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!kiss` до неопределённого времени")
    await interaction.response.send_message(embed=embed)


@tree.command(name="kiss-on",
              description="Включить команду /kiss для использования на себе.")
async def kiss_on(interaction: discord.Interaction):
    global data
    author = interaction.user
    if str(author.id) in data["rp_off"]["kiss"]:
        del data["rp_off"]["kiss"][str(author.id)]
        dumpJson(data)
        embed = txt_embed(interaction, "Вы разблокировали команду `t!kiss`")
        await interaction.response.send_message(embed=embed)
        return
    embed = txt_embed(interaction, "Команда `t!kiss` не заблокирована")
    await interaction.response.send_message(embed=embed)


@tree.command(name="eat-off",
              description="Выключить команду /eat для использования на себе.")
async def eat_off(interaction, time_: str = "0m"):
    global data
    time_ = parsTimeStr(time_)
    if time_ == -1:
        embed = txt_embed(interaction, "Ошибка! Указано некорректное время")
        await interaction.response.send_message(embed=embed)
        return
    data["rp_off"]["eat"][str(
        interaction.user.id)] = time.time() + time_ if time_ != 0 else None
    dumpJson(data)
    if time_ != 0:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!eat` до <t:{round(time.time() + time_)}>"
        )
    else:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!eat` до неопределённого времени")
    await interaction.response.send_message(embed=embed)


@tree.command(name="eat-on",
              description="Включить команду /eat для использования на себе.")
async def eat_on(interaction: discord.Interaction):
    global data
    author = interaction.user
    if str(author.id) in data["rp_off"]["eat"]:
        del data["rp_off"]["eat"][str(author.id)]
        dumpJson(data)
        embed = txt_embed(interaction, "Вы разблокировали команду `t!eat`")
        await interaction.response.send_message(embed=embed)
        return
    embed = txt_embed(interaction, "Команда `t!eat` не заблокирована")
    await interaction.response.send_message(embed=embed)


@tree.command(name="catch-off",
              description="Выключить команду /catch для использования на себе."
              )
async def catch_off(interaction, time_: str = "0m"):
    global data
    time_ = parsTimeStr(time_)
    if time_ == -1:
        embed = txt_embed(interaction, "Ошибка! Указано некорректное время")
        await interaction.response.send_message(embed=embed)
        return
    data["rp_off"]["catch"][str(
        interaction.user.id)] = time.time() + time_ if time_ != 0 else None
    dumpJson(data)
    if time_ != 0:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!catch` до <t:{round(time.time() + time_)}>"
        )
    else:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!catch` до неопределённого времени")
    await interaction.response.send_message(embed=embed)


@tree.command(name="catch-on",
              description="Включить команду /catch для использования на себе.")
async def catch_on(interaction: discord.Interaction):
    global data
    author = interaction.user
    if str(author.id) in data["rp_off"]["catch"]:
        del data["rp_off"]["catch"][str(author.id)]
        dumpJson(data)
        embed = txt_embed(interaction, "Вы разблокировали команду `t!catch`")
        await interaction.response.send_message(embed=embed)
        return
    embed = txt_embed(interaction, "Команда `t!catch` не заблокирована")
    await interaction.response.send_message(embed=embed)


@tree.command(name="pat-off",
              description="Выключить команду /pat для использования на себе.")
async def pat_off(interaction, time_: str = "0m"):
    global data
    time_ = parsTimeStr(time_)
    if time_ == -1:
        embed = txt_embed(interaction, "Ошибка! Указано некорректное время")
        await interaction.response.send_message(embed=embed)
        return
    data["rp_off"]["pat"][str(
        interaction.user.id)] = time.time() + time_ if time_ != 0 else None
    dumpJson(data)
    if time_ != 0:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!pat` до <t:{round(time.time() + time_)}>"
        )
    else:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!pat` до неопределённого времени")
    await interaction.response.send_message(embed=embed)


@tree.command(name="pat-on",
              description="Включить команду /pat для использования на себе.")
async def pat_on(interaction: discord.Interaction):
    global data
    author = interaction.user
    if str(author.id) in data["rp_off"]["pat"]:
        del data["rp_off"]["pat"][str(author.id)]
        dumpJson(data)
        embed = txt_embed(interaction, "Вы разблокировали команду `t!pat`")
        await interaction.response.send_message(embed=embed)
        return
    embed = txt_embed(interaction, "Команда `t!pat` не заблокирована")
    await interaction.response.send_message(embed=embed)


@tree.command(
    name="revive-off",
    description="Выключить команду /revive для использования на себе.")
async def revive_off(interaction, time_: str = "0m"):
    global data
    time_ = parsTimeStr(time_)
    if time_ == -1:
        embed = txt_embed(interaction, "Ошибка! Указано некорректное время")
        await interaction.response.send_message(embed=embed)
        return
    data["rp_off"]["revive"][str(
        interaction.user.id)] = time.time() + time_ if time_ != 0 else None
    dumpJson(data)
    if time_ != 0:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!revive` до <t:{round(time.time() + time_)}>"
        )
    else:
        embed = txt_embed(
            interaction,
            f"Вы заблокировали команду `t!revive` до неопределённого времени")
    await interaction.response.send_message(embed=embed)


@tree.command(name="revive-on",
              description="Включить команду /revive для использования на себе."
              )
async def revive_on(interaction: discord.Interaction):
    global data
    author = interaction.user
    if str(author.id) in data["rp_off"]["revive"]:
        del data["rp_off"]["revive"][str(author.id)]
        dumpJson(data)
        embed = txt_embed(interaction, "Вы разблокировали команду `t!revive`")
        await interaction.response.send_message(embed=embed)
        return
    embed = txt_embed(interaction, "Команда `t!revive` не заблокирована")
    await interaction.response.send_message(embed=embed)


@tree.command(name="hug", description="Обнять кого-нибудь.")
async def hug(interaction: discord.Interaction, member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["hug"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["hug"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    if member == None or member == author:
        embed = discord.Embed(
            color=0xff8800,
            description=f'<@{author.id}> {RP["hug"]["self use text"]}')
        url = random.choice(RP["hug"]["self use image"])
        embed.set_image(url=url)
        embed.set_thumbnail(url=RP["hug"]["self use emote"])
        await interaction.response.send_message(embed=embed)
        logging.info(f'The t!hug command was used with the url [{url}]')
        return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["hug"]["text"])} <@{member.id}>')
    url = random.choice(RP["hug"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=random.choice(RP["hug"]["emote"]))
    logging.info(f'The t!hug command was used with the url [{url}]')
    await interaction.response.send_message(embed=embed)

@tree.command(name="hugall", description="Обнять всех!")
async def hugall(interaction: discord.Interaction):
    author = interaction.user
    embed = discord.Embed(
        color=0xff8800,
        description=f'<@{author.id}> {random.choice(RP["hugall"]["text"])}')
    url = random.choice(RP["hugall"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=random.choice(RP["hugall"]["emote"]))
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!hugall command was used with the url [{url}]')


@tree.command(name="kiss", description="Поцеловать кого-нибудь.")
async def kiss(interaction: discord.Interaction,
               member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["kiss"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["kiss"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    if member == None or member == author:
        embed = discord.Embed(
            color=0xff8800,
            description=
            f'<@{author.id}> {random.choice(RP["kiss"]["self use text"])}')
        url = random.choice(RP["kiss"]["self use image"])
        embed.set_image(url=url)
        embed.set_thumbnail(url=RP["kiss"]["self use emote"])
        await interaction.response.send_message(embed=embed)
        logging.info(f'The t!kiss command was used with the url [{url}]')
        return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["kiss"]["text"])} <@{member.id}>')
    url = random.choice(RP["kiss"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=RP["kiss"]["emote"])
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!kiss command was used with the url [{url}]')


@tree.command(name="eat", description="Съесть кого-нибудь.")
async def eat(interaction: discord.Interaction, member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["eat"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["eat"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    if member == None or member == author:
        embed = discord.Embed(
            color=0xff8800,
            description=
            f'<@{author.id}> {random.choice(RP["eat"]["self use text"])}')
        url = random.choice(RP["eat"]["self use image"])
        embed.set_image(url=url)
        embed.set_thumbnail(url=RP["eat"]["self use emote"])
        await interaction.response.send_message(embed=embed)
        logging.info(f'The t!eat command was used with the url [{url}]')
        return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["eat"]["text"])} <@{member.id}>')
    url = random.choice(RP["eat"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=RP["eat"]["emote"])
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!eat command was used with the url [{url}]')


@tree.command(name="catch", description="Поймать кого-нибудь.")
async def catch(interaction: discord.Interaction,
                member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["catch"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["catch"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    if random.randint(1, 10) == 1:
        embed = discord.Embed(
            color=0xff8800,
            description=
            f'<@{author.id}> {random.choice(RP["catch"]["fail text"])}')
        url = random.choice(RP["catch"]["self use image"])
        embed.set_image(url=url)
        embed.set_thumbnail(url=RP["catch"]["fail emote"])
        await interaction.response.send_message(embed=embed)
        logging.info(f'The t!catch command was used with the url [{url}]')
        return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["catch"]["text"])} <@{member.id}>')
    url = random.choice(RP["catch"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=RP["catch"]["emote"])
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!catch command was used with the url [{url}]')


@tree.command(name="pat", description="Погладить кого-нибудь.")
async def pat(interaction: discord.Interaction, member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["pat"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["pat"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["pat"]["text"])} <@{member.id}>')
    url = random.choice(RP["pat"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=RP["pat"]["emote"])
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!pat command was used with the url [{url}]')


@tree.command(name="kill", description="Убить кого-нибудь :/")
async def kill(interaction: discord.Interaction,
               member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["kill"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["kill"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    if member == None or member == author:
        embed = discord.Embed(
            color=0xff8800,
            description=
            f'<@{author.id}> {random.choice(RP["kill"]["self use text"])}')
        url = random.choice(RP["kill"]["self use image"])
        embed.set_image(url=url)
        embed.set_thumbnail(url=RP["kill"]["self use emote"])
        await interaction.response.send_message(embed=embed)
        logging.info(f'The t!kill command was used with the url [{url}]')
        return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["kill"]["text"])} <@{member.id}>')
    url = random.choice(RP["kill"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=random.choice(RP["kill"]["emote"]))
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!kill command was used with the url [{url}]')


@tree.command(name="revive", description="Оживить кого-нибудь.")
async def revive(interaction: discord.Interaction,
                 member: discord.Member = None):
    author = interaction.user
    if str(author.id) in data["rp_off"]["revive"]:
        embed = txt_embed(interaction,
                          "Данная команда не может быть использована вами")
        await interaction.response.send_message(embed=embed)
        return
    if member != None:
        if str(member.id) in data["rp_off"]["revive"]:
            embed = txt_embed(
                interaction,
                "Данная команда не может быть использована вами на этом участнике"
            )
            await interaction.response.send_message(embed=embed)
            return
    embed = discord.Embed(
        color=0xff8800,
        description=
        f'<@{author.id}> {random.choice(RP["revive"]["text"])} <@{member.id}>')
    url = random.choice(RP["revive"]["image"])
    embed.set_image(url=url)
    embed.set_thumbnail(url=RP["revive"]["emote"])
    await interaction.response.send_message(embed=embed)
    logging.info(f'The t!revive command was used with the url [{url}]')
"""

keep_alive()

client.run(TOKEN)
