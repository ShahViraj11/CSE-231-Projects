import math

print("\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)")

num_str = input("\nWould you like to continue (A/B)? \n")

while num_str == "A":

    ask_code = input("\nCustomer code (BD, D, W): \n")
    while ask_code != "BD" and ask_code != "D" and ask_code != "W":
        print("\n\t*** Invalid customer code. Try again. ***")
        ask_code = input("\nCustomer code (BD, D, W): \n")
    No_days = int(input("\nNumber of days: \n"))
    Odometer_start = int(input("Odometer reading at the start: \n"))
    Odometer_end = int(input("Odometer reading at the end:   \n"))
    miles = float(Odometer_end - Odometer_start) / 10
    amt_due = 0
    if miles < 0:
        miles = float((Odometer_end + 1000000) - Odometer_start) / 10

    if ask_code == "BD":
        amt_due = float(40 * No_days + 0.25 * miles)
    elif ask_code == "D":
        if miles <= 100:
            amt_due = float(60.0 * No_days)
        else:
            amt_due = float(No_days * (60 + 0.25 * ((miles / No_days) - 100)))
    elif ask_code == "W":
        weeks = math.ceil(No_days / 7)
        mpw = miles / weeks

        if mpw <= 900:
            amt_due = float(190 * weeks)
        elif 900 < mpw <= 1500:
            amt_due = float(weeks*(190 + 100))
        else:
            amt_due = float(190 * weeks + 200 * weeks + 0.25 * (miles - 1500 * weeks))

    print("\nCustomer summary:")
    print("\tclassification code:", ask_code)
    print("\trental period (days):", No_days)
    print("\todometer reading at start:", Odometer_start)
    print("\todometer reading at end:  ", Odometer_end)
    print("\tnumber of miles driven: ", miles)
    print("\tamount due: $", amt_due)

    num_str = input("\nWould you like to continue (A/B)? \n")
if num_str == "B":
    print("Thank you for your loyalty.")