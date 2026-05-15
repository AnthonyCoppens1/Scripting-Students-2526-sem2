from difflib import SequenceMatcher

def calculateTrueLove(name1, name2):
    """Calculates the true love percentage between 2 given names
    Parameters:
        name1 (string): a name
        name2 (string): a name
    Returns:
        int: the percentage
    """

    result = round(SequenceMatcher(None, name1, name2).ratio() * 100, 0)
    return f"{result}% match!"



def crappyLove(name1, name2):
    """Calculates the crappy love percentage between 2 given names
    Parameters:
        name1 (string): a name
        name2 (string): a name
    Returns:
        int: the percentage
    """
    result = abs(len(name1) - len(name2))

    if result <= 2:
        return "90% match"
    elif result <= 5:
        return "70% match"
    elif result <= 8:
        return "50% match"
    else:
        return "Don't even try % match"