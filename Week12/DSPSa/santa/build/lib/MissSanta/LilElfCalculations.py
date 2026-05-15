import random
def helloSanta():
    """Greets Santa
    Parameters:
        None
    Returns:
        None    
    """

    print("Hello Santa")


def helloElfName(name):
    """Greets a little elf by its own name
    Parameters:
        name (string): a name of an elf
    Returns:
        None    
    """
    print(f"Hello lil elf {name}!")


def countStock(wrappedGifts, gifts):
    """Calculates the amount of gifts left to wrap!
    Parameters:
        wrappedGifts (int): an amount of gifts that have been wrapped
        gifts (int): total amount of gifts to be wrapped
    Returns:
        string: message that explains how many gifts need to be wrapped    
    """
    GiftsToWrap = gifts - wrappedGifts
    return f"The darned elves still have to wrap {GiftsToWrap} gifts!!!"


def KidsReceivedCoal(coalAmount):
    """Generates a random amount of kids that have received the punishment of coal for Christmas
    Parameters:
        coalAmount (int): an maximum amount of coal that can be given to kids
    Returns:
        string: message that explains how many kids were punished and what the maximum amount would've been.   
    """
    coalKids = random.randin(0,coalAmount)
    return f"{coalKids} have been punished this year. The possible max was {coalAmount}"