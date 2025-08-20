from src.config import load_config
from src.utils.logger import setup_logger
from src.utils.storage import Storage
from src.platforms.telegram_client import TelegramClient
from src.platforms.discord_client import start_discord
from src.platforms.twitter_client import TwitterClient
import threading

logger = setup_logger()
config = load_config()
storage = Storage(config["database_path"])

# Initialize platforms
telegram_client = TelegramClient(config["telegram"], storage)
twitter_client = TwitterClient(config["twitter"], storage)

# Start Discord in separate thread
discord_thread = threading.Thread(target=start_discord, args=(config["discord"], storage))
discord_thread.start()

# Start Telegram
telegram_client.start()
