import tweepy
from src.utils.logger import setup_logger

logger = setup_logger("TwitterClient")

class TwitterClient:
    def __init__(self, config, storage):
        auth = tweepy.OAuth1UserHandler(
            config["api_key"], config["api_secret"], 
            config["access_token"], config["access_token_secret"]
        )
        self.api = tweepy.API(auth)
        self.storage = storage

    def send_dm(self, user_id, text):
        try:
            self.api.send_direct_message(recipient_id=user_id, text=text)
        except Exception as e:
            logger.error(f"Twitter DM failed to {user_id}: {e}")

    def post_tweet(self, text):
        try:
            self.api.update_status(text)
        except Exception as e:
            logger.error(f"Failed to post tweet: {e}")
