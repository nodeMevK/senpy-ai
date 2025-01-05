def whats_hot_prompt(tweets_data, context, personality):

    template = """
        Analyze the following {posts} and text. 

        Using the information, render a concise internal monologue about the current posts
        and their relevance to update your priors.

        Focus on trends, metas, key themes, and potential areas of interest. 

        Try to find the next meta brewing. 

        Most importantly, focus on the posts that were given to you. 

        External content:
        {text}

        Also, stay true to your lore and character

        Character:
        {personality}


    """

    return template.format(psots=tweets_data, text=context)


def respond_to_tweet(tweets_data, context, personality):
    template = """
        Analyze the following posts and text

        {tweets}
        {text}


    """

    return template.format(tweets=tweets_data, text=context)

def respond_aggresively_to_tweet(tweets_data, context, personality):
    template = """
        Analyze the following posts and text

        {tweets}
        {text}


    """

    return template.format(tweets=tweets_data, text=context)


