###########################################################

#  Computer Project #3

#

#  The program basically displays entire discription of triangle

#    asks user if he wants to process a triangle

#    if yes then enter the sides of the triangle

#    program does not stop until user enters no

#       3 sides of the triangle are entered

#       area, perimeter, angles in radians and degrees, type of triangle

#       asks if user wants to process another triangle

#       asks for second input

#    counts the number of triangles

###########################################################
import math

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
count = 0
print()
s = input("Do you wish to process a triangle (Y or N)?  "  # asking the user if he wants to proceed
          )
if s == 'N' or s == 'n':
    print("\nNumber of valid triangles:", count)
    quit()

while s == 'Y' or s == 'y':  # if the user enters yes then he is asked to enter the length of each sides
    A = input("\nEnter length of side AB: ")
    a = float(A)
    B = input("\nEnter length of side BC: ")
    b = float(B)
    C = input("\nEnter length of side CA: ")
    c = float(C)
    if a + b == c or b + c == a or c + a == b:  # if he enters the sides which make a degenrate or invalid triangle he is asked to enter it again if he wants to
        print("\n\n  Degenerate Triangle")
        s = input("\nDo you wish to process another triangle? (Y or N) ")

        if s == "N" or s == "n":
            print("\nNumber of valid triangles:", count)
            quit()
        else:
            continue
    elif a + b < c or b + c < a or c + a < b:
        print("\n\n  Not a Triangle")
        s = input("\nDo you wish to process another triangle? (Y or N) ")
        if s == "N" or s == "n":
            print("\nNumber of valid triangles:", count)
            quit()
        else:
            continue
    elif a + b > c or b + c > a or c + a > b:  # if the gives sides are valid then entire description of triangle is shown
        print("\n\n  Valid Triangle")
        count += 1
        print("\n  Triangle sides:")
        print("    Length of side AB:", a)
        print("    Length of side BC:", b)
        print("    Length of side CA:", c)
        alpha = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # using cosine rules measuring the angles
        betta = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
        gamma = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
        x = alpha * 180 / math.pi  # converting them into degrees and asigning them new variables
        y = betta * 180 / math.pi
        z = gamma * 180 / math.pi
        print('\n  Degree measure of interior angles:')  #
        print("    Angle A:", round(y, 1))
        print("    Angle B:", round(z, 1))
        print("    Angle C:", round(x, 1))
        print("\n  Radian measure of interior angles:")
        print("    Angle A:", round(betta, 1))
        print("    Angle B:", round(gamma, 1))
        print("    Angle C:", round(alpha, 1))
        print("\n  Perimeter and Area of triangle:")
        print("    Perimeter of triangle:", a + b + c)  # calculating perimeter
        s = float((a + b + c) / 2)
        print("    Area of triangle:", round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 1))  # calculating area
        print("\n  Types of triangle:")
        if a == b == c:  # checking the type of triangle
            print("    Isosceles Triangle")
            print("    Equilateral Triangle")
            print("    Oblique Triangle")
        elif a == b != c or b == c != a or c == a != b:
            if a == math.sqrt(b ** 2 + c ** 2) or b == math.sqrt(a ** 2 + c ** 2) or c == math.sqrt(
                    b ** 2 + a ** 2):
                print("    Isosceles Triangle")
                print("    Right Triangle")
            elif x > 90 or y > 90 or z > 90:
                print("    Isosceles Triangle")
                print("    Oblique Triangle")
                print("    Obtuse Triangle")
            elif x < 90 or y < 90 or z < 90:
                print("    Isosceles Triangle")
                print("    Oblique Triangle")

        elif a != b != c:
            if a == math.sqrt(b ** 2 + c ** 2) or b == math.sqrt(a ** 2 + c ** 2) or c == math.sqrt(
                    b ** 2 + a ** 2):  # using pythagorean theorem to check if it is a right triangle
                print("    Scalene Triangle")
                print("    Right Triangle")
            elif x > 90 or y > 90 or z > 90:
                print("    Scalene Triangle")
                print("    Oblique Triangle")
                print("    Obtuse Triangle")
        s = input(
            "\nDo you wish to process another triangle? (Y or N) ")  # asking the user if he wants to process another triangle
print("\nNumber of valid triangles:", count)
