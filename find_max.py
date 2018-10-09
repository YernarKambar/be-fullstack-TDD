def get_max(a, b):
    """
        return max number among a and b
    """
    if a>b: return a
    else: return b

def get_max_without_arguments():
    """
        raise TypeError exception with message
        The raise statement allows the programmer to force a specified exception to occur
    """
    raise TypeError('Error cause no arguments')

def get_max_with_one_argument(a):
    """
        return that value
    """
    return a;

def get_max_with_many_arguments(*args):
    """
        return highest number among args
    """
    result = args[0]
    for num in args:
        if (num > result):
            result = num
    return result

def get_max_with_one_or_more_arguments(first, *args):
    """
        return highest number among first + args
    """
    result = first
    for num in args:
        if (num > result):
            result = num
    return result

def get_max_bounded(*args, low, high):
    pass


def make_max(*, low, high):
    def inner(first, *args):
        pass

    return inner
