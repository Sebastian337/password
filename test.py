MAX_LENGTH = 12
MAX_SCORE = 10
SCORE_CHECK = 2


def is_very_long(password):
    return len(password) > MAX_LENGTH


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_symbols(password):
    return any(not (char.isdigit() or char.isalpha()) for char in password)


def main():
    checks = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]
    
    password = input("Введите пароль: ")
    score = sum(SCORE_CHECK for check in checks if check(password))
    print(f"Рейтинг пароля: {min(score, MAX_SCORE)}")


if __name__ == "__main__":
    main()