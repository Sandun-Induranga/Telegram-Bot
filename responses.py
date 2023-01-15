"""
* @author : Sandun Induranga
* @since : 0.1.0
"""


def bot_responses(message):
    user_message = str(message).lower()

    if user_message in ("hello", "hi"):
        return 'Hey! How are you?'

    if user_message in ('who are you', 'who are you?', 'what is this'):
        return 'I\'m a bot who created by Sandun Induranga'
