def get_an_idea_prompt(tweets_data, context):

    template = """
        {tweets}
        {text}
    """

    return template.format(tweets=tweets_data, text=context)


  