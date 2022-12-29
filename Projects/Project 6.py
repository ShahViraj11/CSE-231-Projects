###############################################################################
#
#   CSE 231 #6
#
#   Purpose: to visualize the filtered data from the given two files
#
#   Algorithm:
#       import libraries
#           csv
#           itemgetter from operator
#       declare global variables
#           REGIME
#           MENU
#       define funtions
#           open_file()
#               returns a file pointer if correct file is inputted
#           read_file()
#               takes in a file pointer, reads the file and returns a list of
#               data
#           get_characters_by_criterion()
#               takes the value from the readfile and based on the given
#               value of particular criterion it filters out the data
#           get_characters_by_criteria()
#               takes the data from the previous function and filters data
#               one by one by element, weapon and rarity
#           get_region_list()
#               it retrives the data from the master list, filters out the
#               duplicate data and returns the sorted list
#               have changed their regimes several times over the course of
#               decades
#           main()
#               merges all the functions
#
###############################################################################
import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "
ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"


def open_file():
    """
    This function prompts for a file name input and returns the corresponding
    file pointer if the file name is valid; else will return an error message.
    returns: file pointer
    """
    file_pointer = input("Enter file name: ")
    while True:
        try:
            file_pointer = open(file_pointer)
            break
        except:
            print("\nError opening file. Please try again.")
            file_pointer = ""
            file_pointer = input("Enter file name: ")
    return file_pointer


def read_file(fp):
    """
    This function takes in a file pointer, reads through the file and returns a
    a list of data
    fp: file pointer
    returns: country_names (list), list_of_regime_lists (list)
    """

    file_data = fp.read()
    file_data = file_data.split("\n")

    tup_list = []

    for line in file_data[1:]:
        if line == "":
            break
        else:
            x = line.split(",")
            x[0] = str(x[0])
            x[1] = int(x[1])
            x[2] = str(x[2])
            x[3] = str(x[3])
            x[4] = str(x[4])
            x = [x[0], x[2], x[3], x[1], x[4]]
            if x[4] == "":
                x[4] = None

            tup_list.append(tuple(x))

    return tup_list


def get_characters_by_criterion(list_of_tuples, criteria, value):
    """

    value:  If the criteria value isn't 3 then the input is string else int
    Returns:  list of tuples
    displays: nothing

        """

    return_list = []

    for character in list_of_tuples:
        if value == str(value):
            if character[criteria] == None:
                pass

            else:
                if character[criteria] == value.capitalize():
                    return_list.append(character)
        elif criteria == 3:
            if character[criteria] != int(value):
                pass

            else:
                return_list.append(character)

    return return_list


def get_characters_by_criteria(master_list, element, weapon, rarity):
    """
    value:  From the previous function it filters the data one by one
            with the data types being list of tuples, string, string, int
    Returns:  list of tuples
    displays: nothing
    """
    new_element = get_characters_by_criterion(master_list, 1, element)
    new_weapon = get_characters_by_criterion(new_element, 2, weapon)
    new_rarity = get_characters_by_criterion(new_weapon, 3, rarity)
    return new_rarity


def get_region_list(master_list):
    """

    value:  It takes the value in list of tuples as master list
    Returns:  sorted list of strings
    displays: nothing

        """

    temp_list = []
    temp_list2 = []
    for i in master_list:
        temp_list.append(i[4])
        for i in temp_list:
            if i != None:
                if i not in temp_list2:
                    temp_list2.append(i)
                    temp_list2.sort()

    return temp_list2


def sort_characters(list_of_tuples):
    """

        value: It takes the criteria in list of tuples and order of
        sorting is decreasing rarity and alphabetically by name.
        Returns:  sorted list of tuples
        displays: nothing

            """
    sorted_list = list(list_of_tuples)
    sorted_list.sort(key=len, reverse=True)
    sorted_list.sort(key=itemgetter(3), reverse=True)
    return sorted_list


def display_characters(list_of_tuples):
    """

   value:  It takes the parameter in list of tuples, displays character along with their information using formats
   Returns:  nothing
   displays: character of attributes

       """

    if list_of_tuples:
        print(HEADER_FORMAT.format("Character", "Element", "Weapon", "Rarity", "Region"))
        for j in list_of_tuples:
            if j[4] == None:
                print(ROW_FORMAT.format(j[0], j[1], j[2], j[3], 'N/A'))

            else:
                print(ROW_FORMAT.format(j[0], j[1], j[2], j[3], j[4]))

    else:
        print("\nNothing to print.")


def get_option():
    """

   value:   asks for the input in given range and calls function accordingly
   Returns:  int
   displays: menu and error message

       """

    a = int(input(MENU))
    if a in range(1, 5):
        return a
    else:
        print(INVALID_INPUT)


def main():
    c = open_file()  # calling the open_file function
    main_list = read_file(c)  # reading the file

    while True:  # as long as the input is not 4
        ac = get_option()  # getting option from user
        if ac == 1:  # if the option input is 1
            print("\nRegions:")
            reg_list = get_region_list(main_list)  # calling region list function
            for count, region in enumerate(reg_list):  # going through list
                if region == '':
                    continue  # if empty then continue
                else:
                    if count != (len(reg_list) - 1):  # printing data as asked
                        print(region, end=", ")  # seprating it by comma
                    else:
                        print(region)  # printing out the region of option
        elif ac == 2:  # if the option input is 2
            while True:  # while the condition being true
                crit_input = int(input(CRITERIA_INPUT))  # asking for input
                if crit_input in range(1, 5):  # while input being in range
                    val_input = input(VALUE_INPUT).capitalize()  # to make input devoid of string variations
                    if crit_input != 3:  # checking if input is not 3
                        output = sort_characters(get_characters_by_criterion(main_list, crit_input, val_input))
                        display_characters(output)  # calling display and sort functions
                        break
                    else:
                        if val_input.isdigit():  # checking if input is a digit
                            val_input = int(val_input)  # if so, converting it into integer
                            output = sort_characters(get_characters_by_criterion(main_list, crit_input, val_input))
                            display_characters(output)  # calling display and sort functions
                            break
                        else:

                            print(INVALID_INPUT)  # if above case fails then input is invalid
                            continue  # asking for input again
                else:
                    print(INVALID_INPUT)  # if above all case fail then input is invalid
                    continue  # asking for input again
        elif ac == 3:  # if the option input is 3
            ele_input = input(ELEMENT_INPUT)  # asking for element
            weap_input = input(WEAPON_INPUT)  # asking for weapon
            rar_input = input(RARITY_INPUT)  # asking for rarity
            rar_int = 0  # declaring new integer
            while True:  # while the conditions being true

                try:  # checking if input is integer for rarity
                    rar_int = int(rar_input)
                    output = get_characters_by_criteria(main_list, ele_input, weap_input, rar_int)
                    display_characters(sort_characters(output))  # if condition is true then calling
                    # display and criteria functions
                    break
                except:
                    print(INVALID_INPUT)  # if condition is not true then printing invalid input
                    rar_input = input(RARITY_INPUT)  # asking for input again
                    continue  # rerunning the loop
        elif ac == 4:  # if the option input is 4
            break  # code breaks and the program is exited


if __name__ == "__main__":
    main()

