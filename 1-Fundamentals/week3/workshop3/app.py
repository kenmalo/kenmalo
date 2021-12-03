from donations_pkg import homepage
from donations_pkg.user import login
from donations_pkg.user import register
#from donations_pkg.homepage import show_donate
#from donations_pkg.homepage import show_donations
database = {"admin": "password123"}
donations = []
authorized_user = ""
homepage.show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("logged in as:", authorized_user)
option = input("Choose an option: ")
while True:
    if option == "1":
        username = input("Enter username:")
        password = input("Enter password:")
        authorized_user = login(database, username, password)
        option = input("Choose an option: ")

    elif option == "2":
        username = input("Enter username:")
        password = input("Enter password:")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
            print(database)
            option = input("Choose an option: ")

    elif option == "3":
        authorized_user == ""
        donation = homepage.show_donate(authorized_user)
        donations.append(donation)
        option = input("Choose an option: ")

    elif option == "4":
        homepage.show_donations(donations)
        break
    if option == "5":
        print("Goodbye")
        exit()
