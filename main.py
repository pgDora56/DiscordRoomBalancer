import json
import discord
import random
import asyncio
import time

lock = asyncio.Lock()

# config.jsonの読み込み
with open("config.json", "r") as f:
    conf = json.load(f)
client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")
    channel = await get_join_channel()
    print(channel)

    channel = client.get_channel(conf["entrance_id"])
    target_members = []
    for member in channel.voice_states:
        user = await channel.guild.fetch_member(member)
        if not user.bot:
            target_members.append(user)
    
    random.shuffle(target_members)

    channel_idx = 0
    for member in target_members:
        await member.move_to(client.get_channel(conf["target_ids"][channel_idx]))
        channel_idx = (channel_idx + 1) % len(conf["target_ids"])



@client.event
async def on_voice_state_update(member, before, after):
    # Voiceの状況が変わったときに呼び出される
    if after.channel == None or after.channel.id != conf["entrance_id"]:
        return  # なにもしない
    await move_person(member)


async def move_person(member):
    # LOCK
    async with lock:
        # 人数が少ないチャンネルを探す
        cid = await get_join_channel()

        if cid == -1:
            return
        
        channel = client.get_channel(cid)
        await member.move_to(channel)


async def get_join_channel() -> int:
    msize = 417417417 
    cid = []
    for tid in conf["target_ids"]:
        channel = client.get_channel(tid)
        cnt = 0
        for member in channel.voice_states:
            user = await channel.guild.fetch_member(member)
            if not user.bot:
                cnt += 1
        if cnt < msize:
            msize = cnt
            cid = [tid]
        elif cnt == msize:
            cid.append(tid)

    if len(cid) == 0:
        return -1
    print("cid: ", cid) 
    return random.choice(cid)



token = conf["token"]
client.run(token)