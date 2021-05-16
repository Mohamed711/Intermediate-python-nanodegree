import functools

import helper


def check_types(severity=1):
    """ Check the function input arguments types """

    if severity == 0:
        return lambda function: function

    def severity_error(msg):
        if severity == 1:
            print(msg)
        elif severity == 2:
            raise TypeError(msg)

    def checker(function):
        func_arguments = function.__annotations__
        if not func_arguments:
            return function

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            passed_args = dict(helper.bind_args(function, *args, **kwargs))
            for argument_name, argument_val in passed_args.items():
                if argument_name not in func_arguments:
                    continue

                if type(passed_args[argument_name]) is not func_arguments[argument_name]:
                    severity_error("Argument Error")

            func_return = function(*args, **kwargs)
            if 'return' in func_arguments and type(func_return) is not func_arguments["return"]:
                severity_error("Argument Error")

            return func_return
        return wrapper
    return checker
