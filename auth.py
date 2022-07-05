import json

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

def read_pwdb(path):
    with open(path, 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb

def write_pwdb(pwdb, path):
    with open(path, 'wt') as pwdb_file:
        json.dump(pwdb, pwdb_file)


if __name__ == "__main__":
    username, password = get_credentials()

    pwdb = {"lisa":"asd"}
    status = authenticate(username, password, pwdb)
    write_pwdb(pwdb, "pwdb.json")
    if status:
        print("success")
    else:
        print("failed")
