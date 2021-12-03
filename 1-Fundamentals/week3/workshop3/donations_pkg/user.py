def login(database, username, password):
    if username in database.keys() and password == database[username]:
        print("welcome", username)
        return username

    elif username in database.keys() and password != database[username]:
        print("The password you entered is incorerect")
        return ""
    else:
        print("User does not exist in the database")
        return ""

def register(database, username):
    if username in database.keys():
        print("Username already registered")
        return""
    else:
        print("Username has been registered")
        return username
