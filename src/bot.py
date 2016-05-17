"""
Intricate Chat Bot for Twitch.tv with Whispers

By Shane Engelman <me@5h4n3.com>

Contributions from dustinbcox and theepicsnail
"""

import sys
from threading import Thread

import src.lib.rive as rive
from src.config.config import config
from src.lib.irc import IRC
from src.models.model import Channel, Message, User, Command

reload(sys)
sys.setdefaultencoding("utf8")

BOT_USER = config["username"].lstrip("#")
SUPERUSER = config["superuser"].lstrip("#")
TEST_USER = config["test_user"].lstrip("#")
EXTRA_CHANNEL = "lorenzotherobot".lstrip("#")

NICKNAME = config["username"].lstrip("#")
PASSWORD = config["oauth_password"]


class Bot(object):

    def __init__(self):
        self.IRC = IRC(config)
        self.nickname = NICKNAME
        self.password = PASSWORD
        self.config = config
        self.run()

    def whisper(self, username, message):
        message = str(message.lstrip("!"))
        resp = rive.Conversation(self).run(username.strip(), message)
        if resp:
            resp = resp[:350]
            print "!->", resp
            self.IRC.send_whisper(username, str(resp))
            return

    def run(self):

        def get_incoming_data(kind):
            while True:
                data = self.IRC.nextMessage(kind)
                if kind == "whisper":
                    message = self.IRC.check_for_whisper(data)
                if not message:
                    continue
                if message:
                    if kind == "whisper":
                        data = self.IRC.get_whisper(data)
                    message_dict = data
                    message = message_dict.get('message')
                    username = message_dict.get('username')
                    print "->*", username, message
                    if message and kind == "whisper":
                        Thread(target=self.whisper, args=(
                            username, message)).start()
                continue

        Thread(target=get_incoming_data, args=("whisper",)).start()
