from decouple import config
from telethon import TelegramClient, events
from datetime import datetime, timedelta, timezone

from gemini_reply import PROMPT, generate_reply

api_id = config("API_ID")
api_hash = config("API_HASH")



client = TelegramClient("userbot_session", api_id, api_hash)

REPLY_WINDOW_MINUTES = 5
NOT_TO_MESSAGE = [777000]


async def get_last_messages(chat_id, limit=10):
    msgs = []
    async for m in client.iter_messages(chat_id, limit=limit):
        msgs.append(m)
    
    return list(reversed(msgs))


async def reply_to_recent_messages():
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=REPLY_WINDOW_MINUTES)

    async for dialog in client.iter_dialogs():
        if not dialog.is_user or dialog.entity.id in NOT_TO_MESSAGE:
            continue
        print(dialog.message.date, cutoff, dialog.name)
        if dialog.message.date < cutoff:
                break
        async for msg in client.iter_messages(dialog.id):
            print("->", msg.date, cutoff, dialog.name)
            if msg.date < cutoff:
                break
                        
            if msg.out:
                continue

            async for newer in client.iter_messages(dialog.id, min_id=msg.id):
                if newer.out:
                    break
            else:
                last_messages = await get_last_messages(dialog.id, limit=20)
                context = ""
                # print(f"\nContext for {dialog.name}:")
                for c in last_messages[:-1]:
                    if c.sender_id==458835871:
                        context+=f"{dialog.name}: {c.text}\n"
                    else:
                        context+=f"Yididya: {c.text}\n"
                
                
                reply_text = generate_reply(PROMPT.format(context,last_messages[-1].text ))
                print(reply_text)
                await msg.reply(reply_text)

       




async def main():
    await client.start()
    print("Fetching recent messages")
    await reply_to_recent_messages()
    print("Done")


with client:
    client.loop.run_until_complete(main())

