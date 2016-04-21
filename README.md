# Setup Bot
A bot with personality

Introducing Setup Bot - a Twitch chat/irc bot written in `Python` (2.6 / 2.7) with **FULL WHISPER SUPPORT** and more features than I care to count at this point. This implementation relies on a highly customized IRC connection library that allows for hot event-driven bot action over multiple sockets at once.

## Installation
### Virtual Environment
I would recommend running this in a virtual environment to keep your dependencies in check. If you'd like to do that, run:

```shell
sudo pip install virtualenv
```

Followed by:

```shell
virtualenv venv
```

This will create an empty virtualenv in your project directory in a folder called "venv." To enable it, run:

```shell
source venv/bin/activate
```

and your console window will be in that virtualenv state. To deactivate, run:

```shell
deactivate
```

### Dependencies
To install all dependencies locally (preferably inside your activated virtualenv), run:

```shell
pip install -r requirements.txt
```

### Further Steps
Make a copy of the example config file:

```shell
cp src/config/config_example.py src/config/config.py
```

Make a copy of the example globals file:

```shell
cp globals_example.py globals.py
```

Create a user that you will use to connect with the database with (you do not want to connect as root for security reasons) - replace "newuser" and "password" with whatever you'd like:

Create your schema from my blank template:

#### Globals and Config Files
Head into `src/config/config.py` and enter the correct channels and cron jobs you'd like to run, then go into `globals.py`. Leave `VARIABLE`, and `CHANNEL_INFO` alone.

## Finally
### To run:

```shell
./serve.py
```

### Whispers
If a user tries to type a message that is currently on a cooldown, the bot will whisper the user directly. It will inform them that they need to chill and how much more time they have until they can use it again. It will also let them know that they can just try to use the command in the whisper message itself. Users can type whatever they want to the bot and it will reply with quite a few responses defined in the `brain` directory using a language called `RiveScript` [https://www.rivescript.com/](https://www.rivescript.com/) . There is also an API for quotes that the bot hits when it gets stumped so it sounds smart. The API is provided by [http://forismatic.com/en/api/](http://forismatic.com/en/api/) . The bot can be whispered by typing

```
/w setup_bot hi
```

into any chatroom on Twitch.
