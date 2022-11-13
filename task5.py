import random
def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей

    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ''.join([symbols])
    a = random.sample(password, 8)
    b = (''.join(map(str, a)))
    return b

print(get_random_password())
