import time

def login():
    correct_user = "tripti"
    correct_pass = "tripti"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print("\n---- LOGIN ----")
        username = input("Username: ")
        password = input("Password: ")

        if username == correct_user and password == correct_pass:
            print("\n✅ Login Successful! Welcome,", username)
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"\n❌ Incorrect credentials! Attempts left: {remaining}")
            time.sleep(1)  # small delay (restriction feel)

    print("\n🚫 Account Locked! Too many failed attempts.")

login()
