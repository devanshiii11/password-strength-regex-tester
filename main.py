import re

def validate_password(pwd):
    if len(pwd) < 8:
        return False, "Length less than 8"

    if not re.search(r"\d", pwd):
        return False, "No number present"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        return False, "No special character present"

    return True, "Strong password"


passwords = ["abc", "123456", "Pass@123", "Admin"]

print("Password Strength Report\n")

for pwd in passwords:
    status, reason = validate_password(pwd)
    if status:
        print(f"{pwd} → PASS ({reason})")
    else:
        print(f"{pwd} → FAIL ({reason})")
