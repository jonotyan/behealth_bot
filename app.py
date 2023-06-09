from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from aiogram import executor
from loader import dp
import handlers


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    # await on_startup_notify(dispatcher) #off


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
