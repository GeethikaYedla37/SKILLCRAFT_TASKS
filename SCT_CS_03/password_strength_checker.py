import re

def check_strength(password):
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
    # Check for uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    # Check for lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1
    # Check for special characters
    if re.search(r"[@#$%^&+=!]", password):
        score += 1

    # Return strength level
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength = check_strength(pwd)
    print("Password strength:", strength)
