def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_symbols(password):
    return any(char in "!@#$%^&*()-_=+" for char in password)


checks = [
    is_very_long,
    has_digit,
    has_lower_letters,
    has_upper_letters,
    has_symbols
]


password = input("Введите пароль: ")
score = sum(2 for check in checks if check(password))


print(f"Рейтинг пароля: {min(score, 10)}")
