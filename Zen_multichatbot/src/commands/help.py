def help_command(platform_client, user_id):
    message = "Hi! I'm ZenBot 😎\nAvailable commands:\n/help - Show this\n/stats - Show stats\n/notify - Receive updates"
    platform_client.send_message(user_id, message)
