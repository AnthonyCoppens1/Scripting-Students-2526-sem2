from difflib import SequenceMatcher

def ChristmasLove(name1, name2):
    """Calculates the love percentage between 2 possibly happy people (hopefully they stay together)
    Parameters:
        name1 (string): the name of the first person in love
        name2 (string): the name of the second person in love
    Returns:
        int: the given love percentage between 2 people that have been provided
    """

    love = round(SequenceMatcher(None, name1, name2).ratio() * 100, 0)
    return f"{name1} and {name2} have a match % of {love}% <3 !"


def badLove(name1, name2):
    """Calculates the love percentage between 2 possibly happy people (hopefully they stay together)
    Parameters:
        name1 (string): the name of the first person in love
        name2 (string): the name of the second person in love
    Returns:
        int: the given love percentage between 2 people that have been provided
    """

    length = len(name1) - len(name2)
    if length < 2:
        return "100% match"
    elif length < 5:
        return "50% match"
    else:
        return "0% match"