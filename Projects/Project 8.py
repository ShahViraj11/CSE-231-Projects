###############################################################################
#
#   Viraj's CSE 231 Project 8
#
#   Purpose: This assignment focuses on the design, implementation, and testing of a
#             python program that uses lists,tuples, dictonaries, sets and file management.
#
#   Algorithm:
#   define functions:
#      open_file()
#      read_names()
#      read_movies()
#      read_friends()
#      create_friends_dict()
#      find_common_friends()
#      find_max_friends()
#      find_max_common_friends()
#      find_second_friends()
#      find_max_second_friends()
#           main()
#           merges all the functions according to the respective input
#
############################################################################

MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''


def open_file(s):
    """
    This function prompts the user to input a file name to open and keeps prompting until a
    correct name is entered. The parameter, s, is a string to incorporate into your prompt so
    you are prompting the user for a particular type of file ("names","friends").

    Parameters: string
    Returns: a file pointer
    """
    x = input("\nInput a {} file: ".format(s))  # asking for file input
    while True:
        try:
            file_pointer = open(x, "r", encoding="windows-1252")  # opening the file
            break
        except:
            print('\nError: No such file; please try again.')  # printing out error if file name is invalid
            x = ""
            x = input("\nInput a {} file: ".format(s))  # formatting the input to ask for specific file
    return file_pointer


def read_names(fp):
    """
    This function reads the Names.txt file using file pointer, fp.Because order
    matters you must create the list with the names in the same order that they appear in the
    file (which basically means simply read it in order). The names are unique.

    Parameter: file pointer
    Returns: list of strings
    """
    file_data = fp.read()
    file_data = file_data.split("\n")

    list_list = []
    final = []
    for line in file_data[0:]:
        if line != '':
            final.append(line)

    return final


def read_friends(fp, name_lst):
    """
    This function reads the Friends.csv file using file pointer, fp. The file has no header.
    Each line is a list of indices (ints) of names.That is, line 0, the first line of the
    file corresponds to the name at index 0 of names_lst, and so on.

    Parameter: file pointer, list of strings
    Returns: list of lists of strings
    """
    file_data = fp.read()
    file_data = file_data.split("\n")

    list_list = []
    final = []
    for line in file_data[0:]:
        if line != '':
            a = line.split(",")
            l = []
            for i in a:
                if i != " " and i != "":
                    l.append(name_lst[int(i)])
            final.append(l)
    return final


def create_friends_dict(names_lst, friends_lst):
    """
    This function takes the two lists created in the read_names function and the
    read_friends function and builds a dictionary. Build a dictionary with name as the
    key and a list of friends as the value.

    Parameter: list of strings, list of lists of strings
    Returns: dictionary
    """
    example_dict = {}
    for i in names_lst:
        for j in friends_lst:
            if names_lst.index(i) == friends_lst.index(j):
                example_dict[i] = j

    return example_dict


def find_common_friends(name1, name2, friends_dict):
    """
    This function takes two names (strings) and the friends_dict (returned by the
    create_friends_dict) and returns a set of friends that the two names have in
    common.

    Parameter: string, string, dictionary
    Returns: set of strings
    """
    L1 = friends_dict[name1]
    L2 = friends_dict[name2]
    empty_list = []
    for i in L1:
        for j in L2:
            if i == j:
                empty_list.append(i)
    empty_list = set(empty_list)
    return empty_list


def find_max_friends(names_lst, friends_lst):
    """
    This function takes a list of names and the corresponding list of friends and determines
    who has the most friends. It returns a list of those with the most friends and how many
    friends they have.

    Parameter: list of strings, list of list of strings
    Returns: list of strings, int
    """
    example_lst = []
    example_lst2 = []
    for i in friends_lst:
        example_lst.append(len(i))
    max_len = max(example_lst)
    for j in range(len(example_lst)):
        if example_lst[j] == max_len:
            k = names_lst[j]
            example_lst2.append(k)

    return sorted(example_lst2), max_len


def find_max_common_friends(friends_dict):
    """
    This function takes the friends dictionary and finds which pairs of people have the most
    friends in common. It returns a list of those pairs with the most common friends and how
    many friends they have. Each pair is represented as a tuple of names.

    Parameter: dictionary
    Returns: list of tuples of strings, int
    """
    example_lst = []
    example_lst2 = []

    for i in friends_dict.keys():  # looking through keys in friends dict
        for j in friends_dict.keys():
            if i != j and {j: i} not in example_lst2:  # if i and j aren't equal
                pairs_dict2 = {}
                pairs_dict = {}
                a = tuple(set(friends_dict[i]))
                pairs_dict2[i] = j
                example_lst2.append(pairs_dict2)
                pairs_dict[a] = tuple(set(friends_dict[j]))
                example_lst.append(pairs_dict)
    example_lst3 = []  # declaring list
    for i in example_lst:
        c = 0
        for j in i:
            for k in j:
                c += i[j].count(k)
        example_lst3.append(c)  # appending the list when k in j
    max_len = max(example_lst3)
    main_list = []
    for i in range(len(example_lst3)):  # going through length of 3rd list
        if example_lst3[i] == max_len:
            main_list.append((example_lst2[i]))  # appending it accordingly
    main_list2 = []
    for i in range(len(main_list)):
        for j in main_list[i]:
            main_list2.append((j, main_list[i][j]))

    return main_list2, max_len


def find_second_friends(friends_dict):
    """
    Here we consider second-order friendships, that is, friends of friends. For each person in
    the network find the friends of their friends, but doesn’t include the person’s first order
    friends or themselves.

    Parameter: dictionary
    Returns: dictionary with key a string and value as a set.
    """

    scndfrnddct = {}
    for person in friends_dict:
        frndlist = friends_dict.get(person)
        second_friend_list = []
        for friend in frndlist:
            second_friend_list.extend(friends_dict[friend])
        for name in second_friend_list:
            if name == person or name in friends_dict[person]:
                second_friend_list.remove(name)
        for name in second_friend_list:
            if name == person or name in friends_dict[person]:
                second_friend_list.remove(name)
        for name in second_friend_list:
            if name == person or name in friends_dict[person]:
                second_friend_list.remove(name)
        final_set = set(second_friend_list)
        if person not in scndfrnddct:
            scndfrnddct[person] = final_set
        second_friend_list = []
    return scndfrnddct


def find_max_second_friends(seconds_dict):
    """
    consider second-order friendships, that is, friends of friends. In the
    previous function you created a dictionary of such friendships. Now similar to finding
    max friends you will find max second-order friends.

    Parameter: dictionary
    Returns: list of strings, int
    """
    example_list = []
    names_list = list(seconds_dict.keys())
    final_list = []
    for x in seconds_dict:
        example_list.append(len(seconds_dict[x]))
    max_frnds = max(example_list)
    for i, num in enumerate(example_list):
        if num == max_frnds:
            final_list.append(names_list[i])

    return final_list, max_frnds


def main():
    print("\nFriend Network\n")
    fp = open_file("names")  # calling open file function
    names_lst = read_names(fp)  # calling read names function
    fp = open_file("friends")
    friends_lst = read_friends(fp, names_lst)  # calling the read_friends function to read that file
    friends_dict = create_friends_dict(names_lst, friends_lst)  # calling the creat_friends_dict function

    print(MENU)  # printing out the menu
    choice = input("\nChoose an option: ")  # asking for choice from user
    while choice not in "12345":  # if choice not in range
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")  # asking for input again

    while choice != '5':

        if choice == "1":  # if choice being option 1
            max_friends, max_val = find_max_friends(names_lst, friends_lst)  # calling max_friends function
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")  # printing out the values returned by the respective function
            for name in max_friends:
                print(name)

        elif choice == "2":
            max_names, max_val = find_max_common_friends(
                friends_dict)  # calling the function that finds maximum common friends
            print("\nThe maximum number of commmon friends:", max_val)
            print(
                "Pairs of non-friends with the most friends in common:")  # printing out the values returned by the respective function
            for name in max_names:
                print(name)  # printing out the name of respective function

        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(
                seconds_dict)  # calling out the function that fins maximum second friends
            print("\nThe maximum number of second-order friends:", max_val)
            print(
                "People with the most second_order friends:")  # printing out the values returned by the respective function
            for name in max_seconds:
                print(name)  # printing out the name of respective function

        elif choice == "4":
            x = input("\nEnter a name: ")
            while True:
                if x not in list(friends_dict.keys()):  # if name not being in list of keys of dictionary
                    print("\nThe name {} is not in the list.".format(x))
                    x = input("\nEnter a name: ")  # prompting for input again from user
                    continue  # starting the loop again
                else:
                    print("\nFriends of {}:".format(x))
                    for name in friends_dict[x]:  # if name being in list of keys of dictonary
                        print(name)
                    break  # breaking out of the loop





        else:
            print("Shouldn't get here.")  # in case of wierd inputs

        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")  # reporting that input is an error choice
            choice = input("Choose an option: ")  # prompting for input again


if __name__ == "__main__":
    main()
