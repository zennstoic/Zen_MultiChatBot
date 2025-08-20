from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from src.utils.logger import setup_logger

logger = setup_logger("TelegramClient")

class TelegramClient:
    def __init__(self, config, storage):
        self.token = config["token"]
        self.chat_ids = config.get("chat_ids", [])
        self.storage = storage
        self.bot = Bot(token=self.token)
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def start(self):
        self.dispatcher.add_handler(CommandHandler("help", self.help))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.message))
        logger.info("Telegram client started")
        self.updater.start_polling()

    def help(self, update: Update, context: CallbackContext):
        msg = "Hi! I'm ZenBot 😎\nCommands:\n/help\n/stats\n/notify"
        update.message.reply_text(msg)

    def message(self, update: Update, context: CallbackContext):
        user_id = update.message.from_user.id
        text = update.message.text
        self.storage.log_message("telegram", user_id, text)
        update.message.reply_text(f"Received: {text}")

    def send_message(self, user_id, message):
        try:
            self.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            logger.error(f"Failed to send message to {user_id}: {e}")
