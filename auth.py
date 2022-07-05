import getpass
import json

def get_credentials():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    return username, password

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if password == pwdb[username]:
            status = True
    else:
        ans = input(f"Would you like to add a new user with this name {username}? (y/n)")
        if ans == "y":
            pwdb = add_user(pwdb, username, password, "pwdb.json")

    return status

def read_pwdb(path):
    with open(path, 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb

def write_pwdb(pwdb, path):
    with open(path, 'wt') as pwdb_file:
        json.dump(pwdb, pwdb_file)

def add_user(pwdb, username, password):
    pwdb[username] = password
    write_pwdb(pwdb, 'pwdb.json')
    return pwdb


if __name__ == "__main__":
    username, password = get_credentials()
    # pwdb = {"moritz": "123"}
    # pwdb = {}
    # write_pwdb(pwdb, 'pwdb.json')
    pwdb = read_pwdb('pwdb.json')
    status = authenticate(username, password, pwdb)

    if status:
        print("success")
    else:
        username, password = get_credentials()
        status = authenticate(username, password, pwdb)
        print(status)
