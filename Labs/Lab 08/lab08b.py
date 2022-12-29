from operator import itemgetter

def read_file(fp):
    key_list = []
    value_list = []
    header = fp.readline()
    for line in fp:
        line = line.strip()
        temp = line.split()

        key_list.append(temp[0])
        value_list.append(int(temp[1]))
    result_dict_convertible = []
    for ind in range(len(key_list)):
        result_dict_convertible.append(tuple([key_list[ind],value_list[ind]]))
    return dict(result_dict_convertible)

def integrate_dict(d1,d2):
    d_res = {}
    for name,score in d1.items():
        if name in d_res:
            d_res[name] += score
        else:
            d_res[name] = score
    for name,score in d2.items():
        if name in d_res:
            d_res[name] += score
        else:
            d_res[name] = score

        
    return d_res
def print_res(d_res):
    a = sorted(d_res.items())
    print("{:10s} {:<10s}".format('Name','Total'))
    for ch in a:
        print('{:10s} {:<10d}'.format(ch[0],ch[1]))



fi_op1 = open("data1.txt")
dict_1 = read_file(fi_op1)

fi_op2 = open("data2.txt")
dict_2 = read_file(fi_op2)

res = integrate_dict(dict_1,dict_2)
print_res(res)




