###############################################################################
#
#   Viraj's CSE 231 Project 9
#
#   Purpose: This assignment focuses on the design, implementation, and testing of a
#             python program that uses csv file management lists,tuples, dictonaries
#             sets and file management.
#
#   Algorithm:
#   define functions:
#      open_file()
#      read_file()
#      add_prices()
#      get_max_price_of_company()
#      find_max_company_price()
#      get_avg_price_of_company()
#      display_list()
#          main()
#           merges all the functions according to the respective input
#
############################################################################
import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"


def open_file():
    """
        This function prompts the user to input a file name to open and keeps prompting until a
        correct name is entered. The parameter, s, is a string to incorporate into your prompt so
        you are prompting the user for a particular type of file ("prices","securities").

        Parameters: None
        Returns: two file pointer
        """
    while True:
        f1 = input("\nEnter the price's filename: ")
        try:
            fp1 = open(f1, "r")
            break
        except:
            print("\nFile not found. Please try again.")
            continue
    while True:
        f2 = input("\nEnter the security's filename: ")
        try:
            fp2 = open(f2, "r")
            break
        except:
            print("\nFile not found. Please try again.")
            continue
    return fp1, fp2


def read_file(securities_fp):
    """
        This function takes the security’s file pointer that has the names of the companies and their codes. It has a header line that you need to skip. It creates a set of all the company’s names. And it also creates a master dictionary where the key is the company code (column 1), and the value is a list with 6 things.

        Parameters:  A file pointer
        Returns:  set, dictionary
        """
    lines = csv.reader(securities_fp)
    templist = []
    master_dict = {}
    row_first = True
    for row in lines:
        if row_first:
            row_first = False
        else:
            master_dict[row[0]] = [row[1], row[3], row[4], row[5], row[6], []]
            templist.append(row[1])

    return set(templist), master_dict


def add_prices(master_dictionary, prices_file_pointer):
    """
    This function does not return anything, but it changes the master dictionary while reading the prices file.The company symbol (column 2) is used to index into the master dictionary so you can append the price list to that list (originally empty) at index 5 of the master dictionary entry.

        Parameters: dictionary, file pointer
        Returns: None
        """
    csv_reader = csv.reader(prices_file_pointer)
    next(csv_reader)
    for row in csv_reader:
        if row[1] in master_dictionary.keys():
            (master_dictionary[row[1]])[5].append([row[0], float(row[2]), float(row[3]), float(row[4]), float(row[5])])
    return master_dictionary


def get_max_price_of_company(master_dictionary, company_symbol):
    """
    This function takes the master dictionary and a company symbol, and it gets
    the max high price and the date of the max price. In the case of multiple entries
    of the same maximum price the date as a string is compared.

    Parameters: None
    Returns: two file pointer
        """
    list_a = []
    try:
        for i in master_dictionary[company_symbol][5]:
            tup_a = (i[4], i[0])
            list_a.append(tup_a)

        new_list_a = max(list_a)
        return new_list_a
    except:
        return (None, None)


def find_max_company_price(master_dictionary):
    """
        This function takes the master dictionary and finds the company with the highest high price. The function
         get_max_price_of_company is used to find each company's high.

        Parameters: dictionary
        Returns: (string, float)
        """
    example_dict = {}
    for i in master_dictionary:
        fun_call2 = get_max_price_of_company(master_dictionary, i)
        if fun_call2[1] != None:
            example_dict[fun_call2[0]] = i
    abc = list(example_dict.keys())
    max_price = max(abc)
    return example_dict[max_price], max_price


def get_avg_price_of_company(master_dictionary, company_symbol):
    '''
    This function uses the master dictionary and company symbol to
    find the average high price for the company. Round the average
    to two decimal places. If the company does not exist or there is
    no price data for the company, return 0.0.

    Parameters: dictionary, string
    Returns : float

    '''

    list_a = []
    if company_symbol in master_dictionary and master_dictionary[company_symbol][5] != []:

        for i in master_dictionary[company_symbol][5]:
            list_a.append(i[4])
        n_c = len(list_a)
        s_c = sum(list_a)
        return round(s_c / n_c, 2)
    else:
        return 0.0


def display_list(lst):
    """
        This function does not return anything, but it takes a list of strings and displays
        that list in three columns, each column is 35 characters wide. The correct
        format can be seen in strings.txt. Print items from left to right, and top down.
        Add a new line character “\n” when done printing all elements of the list.

        Parameters: list of strings
        Returns: None
        Display: prints the list in three columns going from left to right and top down.
        """
    z = 3
    x = "{:^35s}"
    for i in lst:
        if z == 1:
            z = 3
            print("{:^35s}\n".format(i), end="")

        else:
            print("{:^35s}".format(i), end="")
            z -= 1


def main():
    print(WELCOME)
    x1, x2 = open_file()  # calling the open file function
    a1, b1 = read_file(x2)  # calling the read_file function
    add_prices(b1, x1)  # calling the add prices function

    while True:
        print(MENU)  # printing to menu to diplay the options
        x = int(input("\nOption: "))  # asking for input option
        if x in range(1, 6):  # if the input is not in the desired range
            if x == 1:  # if the input is option 1
                print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
                a1 = list(a1)  # converting the set into list
                z = sorted(a1)  # sorting the list
                display_list(z)  # calling the display function
                print()
                print()

            elif x == 2:  # if the input is option 2
                print("\ncompanies' symbols:")
                b11 = list(b1.keys())  # making list of keys in the master dictonary
                z1 = sorted(b11)
                display_list(z1)  # calling the display function
                print()
                print()

            elif x == 3:  # if the input is option 3
                while True:  # while the condition being true
                    sym = input("\nEnter company symbol for max price: ")
                    if sym not in b1:  # if the input not being in the master dictonary
                        print("\nError: not a company symbol. Please try again.")
                        continue  # printing the error and asking for input again
                    else:
                        break

                fun_call1 = get_max_price_of_company(b1, sym)  # calling the function to print max price of company
                if fun_call1 == (None, None):  # if the tuple is empty
                    print("\nThere were no prices.")  # prompt that there is no prices
                else:
                    print(  # else printing the desired output
                        "\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(fun_call1[0], fun_call1[1]))
            elif x == 4:  # if the input is option 4
                fun_call3 = find_max_company_price(b1)  # calling the max compnay price function
                print(  # printing out the desired output
                    "\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(fun_call3[0],
                                                                                                          fun_call3[1]))
            elif x == 5:  # if the input is option 5
                while True:  # while the condition being true
                    avg_sym = input("\nEnter company symbol for average price: ")
                    if avg_sym not in b1:  # if th input not being in master dictonary
                        print("\nError: not a company symbol. Please try again.")
                        continue  # reprompting for the input again
                    else:
                        break
                fun_call4 = get_avg_price_of_company(b1, avg_sym)  # calling the averge price function
                if fun_call4 == 0.0:
                    print("\nThere were no prices.")
                else:
                    print(
                        "\nThe average stock price was ${:.2f}.\n".format(fun_call4))  # printing out the desired output




        else:  # incase the input is 6 then the program will end
            break


if __name__ == "__main__":
    main()
