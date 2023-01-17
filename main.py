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
    
    
def main():
    updater = Updater(key.API_KEY, use_context=True)
    dp = updater.dispatcher
    # app = ApplicationBuilder().token(key.API_KEY).build()
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(CommandHandler("help", help_bot))

    dp.add_handler(MessageHandler(Filters.text, chat))
    #
    # dp.add_error_handler(error)
    #
    # updater.start_polling()
    # updater.idle()

    dp.add_handler(CommandHandler("hello", start_bot))

    dp.run_polling()
    dp.idle()


main()
