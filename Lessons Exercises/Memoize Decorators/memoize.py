import functools


def memoize(function):
    function._cache = dict()
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        arg = (args, tuple(kwargs.items()))
        if arg not in function._cache:
            function._cache[arg] = function(*args, **kwargs)
        return function._cache[arg]
    return wrapper

