import json
import dotenv
import os
dotenv.load_dotenv()

github_token = os.getenv('github_token')
print(github_token)

class Config:
    def __init__(self):
        self.load_config()

    def load_config(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.github_token = github_token
            self.notification_settings = config.get('notification_settings')
            self.subscriptions_file = config.get('subscriptions_file')
            self.update_interval = config.get('update_interval', 24 * 60 * 60)
