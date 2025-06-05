import re

def check_password_strength(password):
    strength = 0
    remarks = ''

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks += "Include at least one uppercase letter.\n"

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks += "Include at least one lowercase letter.\n"

    # Digit check
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks += "Include at least one digit.\n"

    # Special character check
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        remarks += "Include at least one special character (@$!%*?&).\n"

    # Display result
    print("\nPassword Strength: ", end="")
    if strength == 5:
        print("Very Strong ✅")
    elif 3 <= strength < 5:
        print("Moderate ⚠️")
    else:
        print("Weak ❌")

    if remarks:
        print("\nSuggestions:")
        print(remarks)

# Example usage
user_password = input("Enter your password: ")
check_password_strength(user_password)
