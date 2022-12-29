###########################################################
#  CSE 231 #5
#
#  asking for input from a menu and defined functions and printing outputs respectively
#    input should be from the list else it will ask again
#    each function has their own way of inputs
#    while loops until the input holds true for the algorithm
#       the function will not stop until the user enters the code x to exit
#       if an invalid input is entered then it is prompted by the function
#       user is offered by the program to enter another input by showing the menu again
#       the program will not breakdown if an unexpected input is given
#    closing message is to thank user for using the program
###########################################################
import math

EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''


def factorial(N):  # defining the factorial function
    N_int = int(N)
    fact = 1
    if N_int < 0:  # program returns none if the input isn't as expected
        return None
    if N_int == 1 or N_int == 0:
        return 1
    else:  # if not then it calculates the value
        while N_int > 1:
            fact = fact * N_int
            N_int = N_int - 1
    return fact


def e():  # defining the e function
    add = 0
    i = 0
    while 1 / math.factorial(i) >= EPSILON:  # using epsilon as defined above
        add += 1 / math.factorial(i)  # using factorial function
        i += 1
        ac = round(add, 10)
    return ac


def pi():  # defining the pi function
    add = 0
    n = 0
    while 1 / (2 * n + 1) >= EPSILON:  # using epsilon as defined above
        add += ((-1) ** n) / (2 * n + 1)
        n += 1
    ab = round(add, 10)  # rounding output to 10 digits
    return 4 * ab


def sinh(x):  # defining the hyperbolic sine function
    try:
        x_flt = float(x)
    except:
        return None
    add = 0
    n = 0
    while math.fabs((x_flt ** (2 * n + 1)) / math.factorial(2 * n + 1)) > EPSILON:  # using epsilon as defined above
        add += (x_flt ** (2 * n + 1)) / math.factorial(2 * n + 1)  # using factorial function
        n += 1
    ae = round(add, 10)
    return ae


def main():  # main function
    print(MENU)
    inp_option = input("\nChoose an option: ")
    while True:  # initiating while statement
        if inp_option.upper() == 'F':
            print("\nFactorial")
            num = input("Input non-negative integer N: ")
            if num.isalpha():  # checking if function is alphabet
                print("\nInvalid N.")
                inp_option = input("\nChoose an option: ")
                continue
            elif int(num) < 0:  # checking if function is non-negative
                print("\nInvalid N.")
                inp_option = input("\nChoose an option: ")
                continue
            else:  # if not then function should calculate the factorial
                fact = factorial(num)  # calling factorial function
                print("\nCalculated:", fact)
                print("Math:", math.factorial(int(num)))
                print("Diff: 0")
                inp_option = input("\nChoose an option: ")
        elif inp_option.upper() == 'E':
            print("\ne")
            a = e()  # calling e function
            print("Calculated:", round(a, 10))  # rounding answer to 10 digits
            print("Math:", round(math.e, 10))  # using math function
            print("Diff: {:.10f}".format(round(math.e, 10) - round(a, 10)))
            inp_option = input("\nChoose an option: ")
            continue
        elif inp_option.upper() == 'P':
            print("\npi")
            b = pi()  # calling pi function
            print("Calculated:", b)
            print("Math:", round(math.pi, 10))
            print("Diff: {:.10f}".format(round(math.pi, 10) - b))
            inp_option = input("\nChoose an option: ")
            continue
        elif inp_option.upper() == 'S':
            print("\nsinh")
            inp_x = input("X in radians: ")
            try:  # using try and except to check if input is a float
                inp_x = float(inp_x)
            except:
                if inp_x.isalpha() == True or inp_x.isalnum() == True:
                    print("\nInvalid X.")
                    inp_option = input("\nChoose an option: ")
                    continue

            c = sinh(inp_x)  # calling sine function
            if c is not None:  # if the input is desired then output will be calculated
                print("\nCalculated:", c)
                print("Math:", round(math.sinh(inp_x), 10))
                print("Diff: {:.10f}".format(round(math.sinh(inp_x), 10) - c))
            inp_option = input("\nChoose an option: ")
            continue

        elif inp_option.upper() == 'M':
            print(MENU)  # printing menu if asked
            inp_option = input("\nChoose an option: ")
            continue
        elif inp_option.upper() == 'X':  # if user wants to exit the program
            print("\nThank you for playing.")
            break
        elif inp_option.upper() != 'F' or inp_option.upper() != "X" or inp_option.upper() == 'S' or inp_option.upper() == 'P' or inp_option.upper() == 'E' or inp_option.upper() == 'M':  # if input isn't the options available from the options
            print("\nInvalid option:", (inp_option).upper())
            print(MENU)
            inp_option = input("\nChoose an option: ")

            continue  # loop will continue to exicute entil user exters X


# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == '__main__':
    main()
