inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):  # function to store snowfall inches
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches  # variable to add inches to total increasing it by value of inches
    print("Total snowfall inches:", total_inches)


print_total_snowfall(inches_snow)
# user input of inches
thurs_inches = input("How many inches of snow fell on Thursday?")
inches_snow["Thursday"] = int(thurs_inches)
print_total_snowfall(inches_snow)
