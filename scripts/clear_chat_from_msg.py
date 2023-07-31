import asyncio

from telethon import TelegramClient

from config import get_settings

settings = get_settings()


CHAT_ID = 1  # id чата, в котором нужно удалить все сообщения


async def main():
    async with TelegramClient(settings.TG_SESSION_NAME, settings.API_ID, settings.API_HASH) as client:
        a = client.iter_messages(CHAT_ID)
        msg_ids = []
        async for i in a:
            msg_ids.append(i.id)
            if len(msg_ids) > 50:
                await client.delete_messages(CHAT_ID, msg_ids)
                msg_ids = []


asyncio.run(main())
