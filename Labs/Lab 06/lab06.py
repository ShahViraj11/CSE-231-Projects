fi_open = open("scores.txt")
li_of_li = []
print("{:21s}{:6s}{:6s}{:6s}{:6s}{:>9s}".format("Name","Exam1","Exam2","Exam3","Exam4","Mean"))
sum_marks_one_stud = 0
first_name_list = []
sum_marks_all_stud_1 = 0
sum_marks_all_stud_2 = 0
sum_marks_all_stud_3 = 0
sum_marks_all_stud_4 = 0
for line in fi_open:
    line_list = line.split()
    line_list[0], line_list[1] = line_list[1], line_list[0][0:len(line_list[0]) - 1]
    li_of_li.append(line_list)
    sum_marks_all_stud_1 += int(line_list[2])
    sum_marks_all_stud_2 += int(line_list[3])
    sum_marks_all_stud_3 += int(line_list[4])
    sum_marks_all_stud_4 += int(line_list[5])
    sum_marks_one_stud = int(line_list[2]) + int(line_list[3]) + int(line_list[4]) + int(line_list[5])
    line_list.append(str(sum_marks_one_stud / 4))
    first_name_list.append(line_list[1]+" "+line_list[0])
first_name_list.sort()
li_of_li_sorted = []
for word in first_name_list:
    for li in li_of_li:
        if word == li[1]+" "+li[0]:
            li_of_li_sorted.append(tuple(li))
            break
for li in li_of_li_sorted:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(li[1]+", "+li[0],int(li[2]),int(li[3]),int(li[4]),int(li[5]),float(li[6])))
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",sum_marks_all_stud_1/5,sum_marks_all_stud_2/5,sum_marks_all_stud_3/5,sum_marks_all_stud_4/5))
