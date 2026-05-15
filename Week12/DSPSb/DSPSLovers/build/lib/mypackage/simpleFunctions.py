def helloworld():
    """Print hello world
    Parameters:
        none
    Returns:
        none
    """
    print("Hello world")


def helloname(name):
    """Print hello followed by a given name
    Parameters:
        name (string): a name
    Returns:
        none
    """
    print(f"Hello, {name}")


def sum(x,y):
    """Calculates the sum between 2 given numbers
    Parameters:
        x (int): a number
        y (int): a number
    Returns:
        int: sum of x and y
    """
    return x + y


def average(x,y):
    """Calculates the average between 2 given numbers
    Parameters:
        x (int): a number
        y (int): a number
    Returns:
        float: average of x and y
    """
    return (x + y) / 2


def power(x,y):
    """Calculates one number to the power of the other
    Parameters:
        x (int): a number
        y (int): a number
    Returns:
        int: x to the power of y
    """
    return x ** y