def get_credentials():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    return username, password

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if password == pwdb[username]:
            status = True
    return status



if __name__ == "__main__":
    username, password = get_credentials()

    pwdb = {"lisa":"asd"}
    status = authenticate(username, password, pwdb)

    if status:
        print("success")
    else:
        print("failed")
