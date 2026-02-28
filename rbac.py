def login(username, password):
    if username=="admin" and password=="admin123":
        return "admin"
    elif username=="editor" and password=="editor123":
        return "editor"
    elif username=="user" and password=="user123":
        return "user"
    else:
        print("Invalid credentials")

username=input("Username: ")
password=input("Password: ")

def rbac(role):
    if role=="admin":
        print("You are admin! ")
    elif role=="editor":
        print("You are editor! ")  
    elif role=="user":
        print("You are user! ")
    else: 
        print("no role assigned")

role=login(username, password)
if role:
    rbac(role)
    print("You are logged in as: ", role)
else: 
    print("Login failed!")
