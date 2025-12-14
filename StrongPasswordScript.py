import re


def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  #one uppercase
        return False
    if not re.search(r"[a-z]", password):  #lowercase
        return False
    if not re.search(r"[0-9]", password):  #one digit
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  #one special character
        return False
    return True


# --- Main Script ---
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")

    if check_password_strength(user_password):
        print("Your password is strong!")
    else:
        print("Your password is weak. Make sure it meets the following criteria")
        print("At least 8 characters long")
        print("Contains uppercase and lowercase letters")
        print("Contains at least one number (0-9)")
        print("Contains at least one special character (!, @, #, $, %, etc.)")
