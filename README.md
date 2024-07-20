# DiscordRoomBalancer
Balancer of the number of people on the discord voice channel

## How to use

1. Make config.json
2. Run `python3 main.py`

## config.json

```json
{
    "token": "YOUR_BOT_TOKEN",
    "entrance_id": VOICE_CHANNEL_ID,
    "target_ids": [VOICE_CHANNEL_ID, VOICE_CHANNEL_ID, ...],
    "special_roles": ["ROLE_NAME", "ROLE_NAME", ...]
}
```

- entrance_id: 入口となるチャンネルID
- target_ids: 飛ばす先のチャンネルID
- special_roles: ロール内で人数を均等にする場合に、そのロール名を指定する
