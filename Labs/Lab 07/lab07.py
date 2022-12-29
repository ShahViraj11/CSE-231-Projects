
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    reader = csv.reader(fp)
    next(reader, None)
    next(reader, None)
    next(reader, None)
    next(reader, None)
    li_of_state_data = []
    for line in reader:
        if line[0] != '':
            li_of_state_data.append(line)
    return li_of_state_data

def get_totals(L):
    US_total = 0
    states_total = 0
    for index, line in enumerate(L):
        index_one = ""
        if index != 0:
            index_one = line[1]
            if "<" in index_one:
                index_one = index_one[1:]
            states_total += int("".join(index_one.split(",")))
        else:
            US_total = int("".join(line[1].split(",")))
    return US_total, states_total

def get_industry_counts(L):
    """Docstring"""
    arg, bus, con, lh, man = 0, 0, 0, 0, 0
    for i in L[1:]:
        if i[9] not in INDUSTRIES:
            continue
        else:
            if i[9] == 'Agriculture':
                arg += 1
            elif i[9] == 'Business services':
                bus += 1
            elif i[9] == 'Construction':
                con += 1
            elif i[9] == 'Leisure/hospitality':
                lh += 1
            else:
                man += 1
    lst = [['Agriculture', arg], ['Business services', bus], ['Construction',
                                                              con],
           ['Leisure/hospitality', lh], ['Manufacturing', man]]
    return sorted(lst, key=itemgetter(1), reverse=True)

def get_largest_states (L):
    li_of_largest_states = []
    US_percent = float(L[0][2][:3])
    for line in L:
        if float(line [2][:3]) > US_percent:
            li_of_largest_states.append(line[0])
    return li_of_largest_states

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()
