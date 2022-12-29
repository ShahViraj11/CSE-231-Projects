num_str = input("Input an integer (0 terminates): \n")
num_int = int(num_str)
even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
positive_count = 0
while num_int != 0:
    if num_int > 0:
        if num_int % 2 != 0:
            odd_count += 1
            odd_sum += num_int
        else:
            even_count += 1
            even_sum += num_int

    if num_int > 0:
        positive_count += 1
    num_str = input("Input an integer (0 terminates): \n")
    num_int = int(num_str)


else:
    print("")
    print("sum of odds:", odd_sum)
    print("sum of evens:", even_sum)
    print("odd count:", odd_count)
    print("even count:", even_count)
    print("total positive int count:", positive_count)


