def managerScore(_response, context, personality):
    template = """
        Analyze the following agent responses: {response}

        On a scale of 1-10 rate them with 
    """
    return template.format(response=_response)
