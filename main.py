from decouple import config

api_id = config("API_ID")
api_hash = config("API_HASH")


from telethon import TelegramClient, events



client = TelegramClient("userbot_session", api_id, api_hash)


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        await event.reply("hello")


client.start()
client.run_until_disconnected()
