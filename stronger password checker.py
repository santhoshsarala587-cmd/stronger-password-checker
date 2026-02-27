print("Stronger Password Checker")

password = input("Enter your password: ")

score = 0
suggestions = ""


if len(password) >= 8:
    score += 1
else:
    suggestions += "Add minimum 8 characters\n"

has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True

if has_upper:
    score += 1
else:
    suggestions += "Add at least one uppercase letter\n"

has_lower = False
for ch in password:
    if ch.islower():
        has_lower = True

if has_lower:
    score += 1
else:
    suggestions += "Add at least one lowercase letter\n"


has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True

if has_digit:
    score += 1
else:
    suggestions += "Add at least one number\n"

special = "!@#$%^&*"
has_special = False
for ch in password:
    if ch in special:
        has_special = True

if has_special:
    score += 1
else:
    suggestions += "Add at least one special character (!@#$%^&*)\n"

print("\nPassword Score:", score, "/ 5")

if score == 5:
    print("Password Strength: Very Strong 💪")
elif score == 4:
    print("Password Strength: Strong 👍")
elif score == 3:
    print("Password Strength: Medium 😐")
elif score == 2:
    print("Password Strength: Weak ⚠️")
else:
    print("Password Strength: Very Weak ❌")

if score < 5:
    print("\nSuggestions to make the password stronger:")
    print(suggestions)