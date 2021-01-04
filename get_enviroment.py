import json
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')
SERVER_NAME = os.getenv('SERVER_NAME')
MEMES_CHANNEL = os.getenv('MEMES_CHANNEL')
RANDOM_CHANNEL = os.getenv('RANDOM_CHANNEL')
ORGANIZER_CHANNEL = os.getenv('ORGANIZER_CHANNEL')
UNIVERSITY_EMAIL = os.getenv('UNIVERSITY_EMAIL')
DROPBOX_KEY = os.getenv('DROPBOX_KEY')
with open('files/parrots.json', 'r') as fp:
    PARROTS = json.load(fp)
