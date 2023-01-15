import Constants as key
from telegram.ext import *
import responses as res

"""
* @author : Sandun Induranga
* @since : 0.1.0
"""

print("Bot Started..!")


def start_bot(update, ctx):
    update.message.reply_text('Type Something to get started..!')


def help_bot(update, ctx):
    update.message.reply_text('If you need help! Please contact Sandun..!')


def chat(update, ctx):
    text = str(update.message.text).lower()
    response = res.bot_responses(text)

    update.message.reply_text(response)


def error(update, ctx):
    print(ctx.error)
