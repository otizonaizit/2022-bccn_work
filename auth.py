import getpass
import json
import os

pwdb_file = "./pwdb.json"

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
            pwdb = add_user(pwdb, username, password)

    return status

def get_pwdb_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "pwdb.json")

def read_pwdb():
    path = get_pwdb_path()
    with open(path, 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb

def write_pwdb(pwdb):
    path = get_pwdb_path()
    with open(path, 'wt') as pwdb_file:
        json.dump(pwdb, pwdb_file)

def add_user(pwdb, username, password):
    pwdb[username] = password
    write_pwdb(pwdb)
    return pwdb

def init_pwdb():
    write_pwdb({})

def check_pwdb():
    if not (os.path.exists(get_pwdb_path())):
        init_pwdb()

if __name__ == "__main__":
    check_pwdb()

    username, password = get_credentials()

    pwdb = read_pwdb()
    status = authenticate(username, password, pwdb) 

    if status:
        print("success")
    else:
        print("failed")
