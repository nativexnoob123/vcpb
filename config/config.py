# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1250763
API_HASH = "11d05c637abdb46e35f51bc73241c75c"

# Get this from @Botfather
TOKEN = "1256310441:AAGztLmdRkkl0JGo-LzgERojAJiwn4ZVfNU"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb+srv://mars:music@cluster0.u0okq.mongodb.net/<dbname>?retryWrites=true&w=majority"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    853393439,
    993911054
]

# The ID of the group where your bot streams
GROUP = -1001366299402

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "da"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 20

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
