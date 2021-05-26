"""Generate an infinite stream of successively larger random lists."""
from helper import random_list


def generate_cases():
    index = 0
    while True:
        yield random_list(index)
        index = index + 1


if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)
