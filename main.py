import Constants as key
from telegram.ext import *
import responses as res

"""
* @author : Sandun Induranga
* @since : 0.1.0
"""

print("Bot Started..!")


def start_command(update, ctx):
    update.message.reply_text('Type Something to get started..!')
