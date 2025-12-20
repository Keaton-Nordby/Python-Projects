# simple password manager that allows you to view and add passwords
# includes simple "encryption"

master_pwd = input("What is your master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(user, passw)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")
        

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press (q) to quit? ")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid code")
        continue
