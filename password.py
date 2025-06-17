def main():
    max_length = 12
    max_score = 10
    score_check = 2

    def is_very_long(password):
        return len(password) > max_length

    def has_digit(password):
        return any(char.isdigit() for char in password)

    def has_lower_letters(password):
        return any(char.islower() for char in password)

    def has_upper_letters(password):
        return any(char.isupper() for char in password)

    def has_symbols(password):
        return any(not (char.isdigit() or char.isalpha()) for char in password)

    checks = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]
    
    password = input("Введите пароль: ")
    score = sum(score_check for check in checks if check(password))
    print(f"Рейтинг пароля: {min(score, max_score)}")


if __name__ == "__main__":
    main()
