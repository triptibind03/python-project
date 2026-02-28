def check_password(password):
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False

    if len(password) <8:
        print("Password is weak, enter strong password")
        return
        
    for ch in password:
        if ch.isupper():
            has_upper=True
        elif ch.islower():
            has_lower=True
        elif ch.isdigit():
            has_digit=True
        elif ch in "@#$%^&*!":
            has_special = True
        
    if has_upper and has_lower and has_digit and has_special :
        print("Your password is strong")
    elif not has_upper:
        print("Enter upper letter")
    elif not has_lower:
        print("Enter a lower letter")
    elif not has_digit:
        print("enter a digit")
    elif not has_special:
        print("Enter Special Characters")
    else:
        print("Enter a strong password")
           

pwd=input("Enter your password: ")
check_password(pwd)
        
