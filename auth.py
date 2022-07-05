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

def read_pwdb(filename):
    with open(filename, 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb

def write_pwdb(filename, pwdb):
    with open(filename, 'wt') as pwdb_file:
        json.dump(pwdb, pwdb_file)

if __name__ == "__main__":
    username, password = get_credentials()

    #pwdb = {"lisa":"asd"}
    #write_pwdb('pwdb.json', pwdb)
    pwdb = read_pwdb('pwdb.json')
    status = authenticate(username, password, pwdb)

    if status:
        print("success")
    else:
        print("failed")
