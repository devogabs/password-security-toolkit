from password_checker import check_password_strength


if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")

    result = check_password_strength(password)

    print(f"Password Strength Score: {result['score']}/{result['max_score']}")
    if result['feedback']:
        print("Feedback:")
        for item in result['feedback']:
            print(f"- {item}") 