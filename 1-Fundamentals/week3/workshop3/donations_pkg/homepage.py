def show_homepage():

    print("          === DonateMe Homepage ====")
    print("|-----------------------------------------|")
    print("| 1.    Login     | 2.    Register        |")
    print("|------------------------------------------|")
    print("| 3.    Donate    | 4.    Show Donations. |-")
    print("------------------5.  Exit----------------")

    print("|-----------------------------------------|")


def show_donate(username):
    donation_amnt = float(input("Enter amount to donate:"))
    #donation_amnt = float(donation_amnt)
    #donation = donation_amnt
    donation = f'{username} donated ${donation_amnt}'
    #donation = "%s donated %.2f"%(username, donation_amnt)
    #donation = "{} donated {}".format(username, donation_amnt)
    print("Thank you for your donation")
    return donation


def show_donations(donations):
    print("\n----------All------------")
    if donations == []:
        print("Currently, there are no donations")
    for i in donations:
        print(donations)
        if i not in donations:
            donations.append(i)
            print(donations)
