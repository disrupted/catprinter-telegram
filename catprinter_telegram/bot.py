from __future__ import annotations

from pathlib import Path

from telethon.sync import TelegramClient, events

from catprinter_telegram.config import API_HASH, API_ID, BOT_TOKEN
from catprinter_telegram.printer import print_image


def filter_start(message):
    return message == "/start"


def run():
    bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

    with bot:

        @bot.on(events.NewMessage(incoming=True, pattern=filter_start))
        async def start(event: events.NewMessage.Event):
            await bot.send_message(
                event.sender_id,
                "Let's go! Send me a picture and I will print it for you.",
            )

        @bot.on(events.NewMessage(incoming=True, pattern=lambda m: not filter_start(m)))
        async def message_handler(event: events.NewMessage.Event):
            if not event.photo:
                await event.reply("that's not a photo")
                return

            filepath = await event.message.download_media()
            if not filepath:
                await event.reply("error saving image")
                return

            await event.reply(f"printing {filepath}...")
            try:
                print_image(Path(filepath))
            except Exception as ex:
                await bot.send_message(
                    event.sender_id,
                    "printing failed",
                )

        bot.run_until_disconnected()
