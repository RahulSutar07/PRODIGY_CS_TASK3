import re

def evaluate_password(password):
    strength_score = 0
    suggestions = []

    # Check for minimum length
    if len(password) >= 8:
        strength_score += 1
    else:
        suggestions.append("Ensure the password is at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    # Check for numeric characters
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        suggestions.append("Include at least one numeric digit.")

    # Check for special symbols
    if re.search(r'[@#$%^&+=]', password):
        strength_score += 1
    else:
        suggestions.append("Add at least one special character (@#$%^&+=).")

    # Determine password strength
    if strength_score == 5:
        password_quality = "Strong"
    elif strength_score == 4:
        password_quality = "Medium"
    else:
        password_quality = "Weak"

    return password_quality, suggestions

while True:
    user_input = input("Enter a password: ")
    password_quality, suggestions = evaluate_password(user_input)
    print(f"Password Strength: {password_quality}")
    
    for suggestion in suggestions:
        print(suggestion)
    
    if password_quality == "Strong":
        break
    else:
        print("\nTry again to improve your password.")
