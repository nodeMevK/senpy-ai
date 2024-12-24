def whats_hot_prompt(tweets_data, context):

    template = """
        Analyze the following posts and text

        {tweets}
        {text}


    """

    return template.format(tweets=tweets_data, text=context)


def respond_to_tweet(tweets_data, context):
    template = """
        Analyze the following posts and text

        {tweets}
        {text}


    """

    return template.format(tweets=tweets_data, text=context)

def respond_aggresively_to_tweet():
    template = """
        Analyze the following posts and text

        {tweets}
        {text}


    """

    return template.format(tweets=tweets_data, text=context)


