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

    if user_message in ('who made you', 'who made you?', 'Who created you', 'Who created you?'):
        return 'Sandun Induranga Created me.'

    if user_message in ('java 8 doc', 'java 8 documentation'):
        return "https://docs.oracle.com/javase/8/docs/api/index.html"

    if user_message in ('java 11 doc', 'java 11 documentation'):
        return "https://docs.oracle.com/javase/8/docs/api/index.html"

    if user_message in ('java 17 doc', 'java 17 documentation'):
        return "https://docs.oracle.com/javase/8/docs/api/index.html"

    if user_message in ('java 18 doc', 'java 18 documentation'):
        return "https://docs.oracle.com/javase/8/docs/api/index.html"

    return "Command Not Found"
