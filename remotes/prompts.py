def whats_hot_prompt(tweets_data, context):

    template = """
        Analyze the following posts and text


        {tweets}
        {text}
    """

    return template.format(tweets=tweets_data, text=context)


  