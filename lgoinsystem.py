def login():
    attempts =  3
    while attempts>0:
        if input("User: ")=="tripti" and input("pass: ")=="tripti":
                 print("logged innn")
                 return
        else:
            attempts-=1
            print("wronggg left attempts: ", attempts)
    print("Locked foreverrr")
login()

