import math
print("Hello, world! This is Python 3!")
def leap_year(year):
    leap = False
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        leap = True
    return leap


def rotate(s, n):
     Rfirst = s[0: len(s) - n]
     Rsecond = s[len(s) - n:]
     return Rsecond + Rfirst

def float_check(x):

    return (x.count('.') == 1 or x.count('.') < 1) and x.replace('.', '').isdigit()

def digit_count(n):
    odd_count = 0
    even_count = 0
    zero_count = 0
    z = str(math.floor(n))
    for i in z:
        if int(i) == 0:
            zero_count = zero_count + 1
        elif int(i) % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return even_count, odd_count, zero_count
