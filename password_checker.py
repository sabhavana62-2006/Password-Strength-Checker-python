import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        print("✔ Length is good")
        score += 1
    else:
        print("✘ Password should be at least 8 characters")

    if any(char.isupper() for char in password):
        print("✔ Contains Uppercase Letter")
        score += 1
    else:
        print("✘ Add an Uppercase Letter")

    if any(char.islower() for char in password):
        print("✔ Contains Lowercase Letter")
        score += 1
    else:
        print("✘ Add a Lowercase Letter")

    if any(char.isdigit() for char in password):
        print("✔ Contains Number")
        score += 1
    else:
        print("✘ Add a Number")

    if any(char in string.punctuation for char in password):
        print("✔ Contains Special Character")
        score += 1
    else:
        print("✘ Add a Special Character")

    print("\nScore:", score, "/5")

    if score == 5:
        print("Password Strength: STRONG 💪")
    elif score >= 3:
        print("Password Strength: MEDIUM 👍")
    else:
        print("Password Strength: WEAK ❌")