from proj07 import read_reviews
print("opening reviews_small.txt")
fp = open("reviews_small.txt",'r',encoding ="windows-1252")
N = 10
print("N:",N)
instructor = [[], [(2, 3), (3, 3), (6, 1), (9, 5), (10, 2)], [(3, 1), (4, 4), (5, 3), (6, 5), (7, 3), (8, 5)], [(1, 2), (4, 3), (7, 3)], [(10, 5)], [], [(2, 2), (5, 2), (8, 3)], [], [], [(2, 2), (10, 4)], []]
print("Instructor:")
print(instructor)
student = read_reviews(N,fp)
print("Student:")
print(student)
#assert student == instructor