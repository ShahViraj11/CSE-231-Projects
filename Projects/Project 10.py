###############################################################################
#
#   Viraj's CSE 231 Project 10
#
#   Purpose: This assignment focuses on the design, implementation, and testing of a
#             python program that uses classes and builds understanding about classes
#             by performing tasks similar to a card game.
#
#   Algorithm:
#   define functions:
#      initialize()
#      display()
#      stock_to_waste()
#      waste_to_tableau()
#      waste_to_foundation()
#      tableau_to_foundation()
#      check_win()
#      parse_option()
#          main()
#           merges all the functions according to the respective input
#
############################################################################
from cards import Card, Deck

MENU = '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''


def initialize():
    '''
    This function builds the required lists for the function.

    Parameters: None
    Returns: tableau, stock, foundation, waste

    '''
    foundation = [[], [], [], []]
    tableau = [[], [], [], [], [], [], []]
    stock = Deck()
    stock.shuffle()
    for a in range(len(tableau)):
        for b in tableau[a:]:
            temp_card = stock.deal()
            temp_card.flip_card()
            b.append(temp_card)
        tableau[a][a].flip_card()

    li = [stock.deal()]
    waste = li

    return tableau, stock, foundation, waste


def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty", "empty", "empty", "empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1]
    if len(stock):
        stock_top_card = "XX"  # stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock", "waste", "foundation"))
    print("\t\t\t\t     ", end='')
    for i in range(4):
        print(" {:5d} ".format(i + 1), end='')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end="")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end="")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end='')
    for i in range(7):
        print(" {:5d} ".format(i + 1), end='')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ", end='')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end='')
            except IndexError:
                print(" {:5s} ".format(''), end='')
        print()
    print()


def stock_to_waste(stock, waste):
    '''
    This functions checks if the card that is being transfered from
    stock to waste is actually valid move or not. If possible then
    it returns true else it returns false

    Parameters: stock, waste
    Returns: True/False


    '''
    if stock.is_empty():
        return False
    else:
        waste.append(stock.deal())
        return True


def waste_to_tableau(waste, tableau, t_num):
    '''
    This functions checks if the card that is being transfered from
    waste to tableau is actually valid move or not. If possible then
    it returns true else it returns false.

    Parameters: waste, tableau, t_num
    Returns: True/False
    '''
    if len(tableau[t_num]) == 0:
        if waste[-1].rank() == 13:
            tableau[t_num].append(waste.pop())
            return True
        else:
            return False

    else:
        if waste[-1].suit() in [1, 4]:
            if tableau[t_num][-1].suit() in [2, 3]:
                if waste[-1].rank() + 1 == tableau[t_num][-1].rank():
                    tableau[t_num].append(waste.pop())
                    return True
                else:
                    return False
            else:
                return False
        elif waste[-1].suit() in [2, 3]:
            if tableau[t_num][-1].suit() in [1, 4]:
                if waste[-1].rank() + 1 == tableau[t_num][-1].rank():
                    tableau[t_num].append(waste.pop())
                    return True
                else:
                    return False
            else:
                return False


def waste_to_foundation(waste, foundation, f_num):
    '''
    This functions checks if the card that is being transfered from
    waste to foundation is actually valid move or not. If possible then
    it returns true else it returns false.

    Parameters: waste, foundation, f_num
    Returns: True/False
    '''
    if len(foundation[f_num]) == 0:
        if waste[-1].rank() == 1:
            foundation[f_num].append(waste.pop())
            return True
        else:
            return False
    elif foundation[f_num][-1].rank() + 1 == waste[-1].rank() and foundation[f_num][-1].suit() == waste[-1].suit():
        foundation[f_num].append(waste.pop())
        return True
    else:
        return False


def tableau_to_foundation(tableau, foundation, t_num, f_num):
    '''
    This functions checks if the card that is being transfered from
    tableau to foundation is actually valid move or not. If possible then
    it returns true else it returns false.

    Parameters: tableau, foundation, t_num , f_num
    Returns: True/False
    '''
    if len(foundation[f_num]) == 0:
        if tableau[t_num][-1].rank() == 1:
            foundation[f_num].append(tableau[t_num].pop())
            if len(tableau[t_num]) != 0:
                if tableau[t_num][-1].is_face_up():
                    return True
                else:
                    tableau[t_num][-1].flip_card()
                    return True
            return True
        else:
            return False
    else:
        if tableau[t_num][-1].suit() == foundation[f_num][-1].suit():
            if tableau[t_num][-1].rank() - 1 == foundation[f_num][-1].rank():
                foundation[f_num].append(tableau[t_num].pop())
                if len(tableau[t_num]) != 0:
                    if tableau[t_num][-1].is_face_up():
                        return True
                    else:
                        tableau[t_num][-1].flip_card()
                        return True
        else:
            return False


def tableau_to_tableau(tableau, t_num1, t_num2):
    '''
    This functions checks if the card that is being transfered from
    tableau to tableau is actually valid move or not. If possible then
    it returns true else it returns false.

    Parameters: tableau, t_num1 , t_num2
    Returns: True/False
    '''
    if len(tableau[t_num2]) == 0:
        if tableau[t_num1][-1].rank() == 13:
            tableau[t_num2].append(tableau[t_num1].pop())
            if len(tableau[t_num1]) != 0:
                if tableau[t_num1][-1].is_face_up():
                    return True
                else:
                    tableau[t_num1][-1].flip_card()
                    return True
            return True
        else:
            return False
    else:
        if tableau[t_num1][-1].suit() in [1, 4]:
            if tableau[t_num2][-1].suit() in [2, 3]:
                if tableau[t_num1][-1].rank() + 1 == tableau[t_num2][-1].rank():
                    tableau[t_num2].append(tableau[t_num1].pop())
                    if tableau[t_num1]:
                        if tableau[t_num1][-1].is_face_up():
                            return True
                        else:
                            tableau[t_num1][-1].flip_card()
                            return True
                    return True
                else:
                    return False
            else:
                return False
        elif tableau[t_num1][-1].suit() in [2, 3]:
            if tableau[t_num2][-1].suit() in [1, 4]:
                if tableau[t_num1][-1].rank() + 1 == tableau[t_num2][-1].rank():
                    tableau[t_num2].append(tableau[t_num1].pop())
                    if tableau[t_num1]:
                        tableau[t_num1][-1].flip_card()
                    return True
                else:
                    return False
            else:
                return False


def check_win(stock, waste, foundation, tableau):
    '''
    This functions checks if the user has won the game
    by checking if there is any card left in stock, waste
    and tableau. If user has won then it returns true else false

    Parameters: stock, waste, foundation , tableau
    Returns: True/False
    '''
    counter = 0
    if stock.is_empty() and len(waste) == 0:
        for i in tableau:
            if len(i) == 0:
                counter += 1
        if counter == len(tableau):
            return True
        else:
            return False
    else:
        return False


def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game
        '''
    option_list = in_str.strip().split()

    opt_char = option_list[0][0].upper()

    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]

    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']

    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1]
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str, dest]

    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
            and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT', 'TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT', 'TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            # elif opt_str == 'MFT' and (source < 0 or source > 3):
            # print("Error in Source.")
            # return None
            # source values are valid
            # check for valid destination values
            if (opt_str == 'TT' and (dest < 1 or dest > 7)) \
                    or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str, source, dest]

    print("\nError in option:", in_str)
    return None  # none of the above


def main():
    tableau1, stock1, foundation1, waste1 = initialize()  # calling the initialize function
    print(MENU)  # displaying all the available moves
    display(tableau1, stock1, foundation1, waste1)  # calling the display function
    while True:  # while the condition being true

        inp_1 = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")  # asking for input from the user
        list_1 = parse_option(inp_1)  # calling parse_option function
        if list_1 is None:
            display(tableau1, stock1, foundation1, waste1)
            continue
        else:  # incase if list_1 is not empty
            if len(list_1) == 1:
                if list_1[0].upper() == 'H':
                    print(MENU)  # printing menu if input is H
                elif list_1[0].upper() == 'Q':
                    break  # breaking out of the loop
                elif list_1[0].upper() == 'R':
                    tableau1, stock1, foundation1, waste1 = initialize()  # initializing the game
                    print(MENU)  # displaying all the available moves
                    display(tableau1, stock1, foundation1, waste1)  # calling the display function
                elif list_1[0].upper() == 'SW':
                    var_1 = stock_to_waste(stock1, waste1)  # calling the stock_to_waste function for moving the card
                    if not var_1:
                        print("\nInvalid move!\n")
                    display(tableau1, stock1, foundation1, waste1)  # calling the display function
            elif len(list_1) == 2:  # if the length of list being 2
                if list_1[0].upper() == 'WT':
                    var_2 = waste_to_tableau(waste1, tableau1, int(
                        list_1[1]) - 1)  # moving card from waste to tableau by calling the respective function
                    if not var_2:  # checking if move is valid or not
                        print("\nInvalid move!\n")
                    display(tableau1, stock1, foundation1, waste1)  # calling the display function
                elif list_1[0].upper() == 'WF':
                    var_3 = waste_to_foundation(waste1, foundation1, int(
                        list_1[1]) - 1)  # moving card from waste to foundation by calling the respective function
                    if not var_3:
                        print("\nInvalid move!\n")
                    g_won = check_win(stock1, waste1, foundation1,
                                      tableau1)  # checking if the user won as foundation is invloved
                    if g_won:
                        print("You won!")
                    display(tableau1, stock1, foundation1, waste1)  # calling the display function
            elif len(list_1) == 3:  # if the length of list being 2
                if list_1[0].upper() == 'TT':
                    var_4 = tableau_to_tableau(tableau1, int(list_1[1]) - 1, int(
                        list_1[2]) - 1)  # moving card from tableau to tableau by calling the respective function
                    if not var_4:
                        print("\nInvalid move!\n")
                    display(tableau1, stock1, foundation1, waste1)  # calling the display function
                elif list_1[0].upper() == 'TF':
                    # moving card from tableau to foundation by calling the respective function
                    var_5 = tableau_to_foundation(tableau1, foundation1, int(list_1[1]) - 1, int(list_1[2]) - 1)

                    if var_5 is False and var_5 is not None:  # if the move returns none of if it is invalid
                        print("\nInvalid move!\n")
                    g_won = check_win(stock1, waste1, foundation1,
                                      tableau1)  # checking if the user won as foundation is invloved
                    if g_won:
                        print("You won!")
                    display(tableau1, stock1, foundation1, waste1)  # calling the display function

    pass


if __name__ == '__main__':
    main()

