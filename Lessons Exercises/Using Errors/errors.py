INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


class InvalidPasswordError(ValueError):
    pass


def validate_password(username, password):
    if password == username or password in INVALID_PASSWORDS:
        raise InvalidPasswordError
    else:
        return True


def create_account(username, password):
    return (username, password)


def main(username, password):

    try:
        validate_password(username, password)
    except InvalidPasswordError:
        print("Oh no!")
    else:
        account = create_account(username, password)


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!
