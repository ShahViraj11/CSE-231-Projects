import string


def build_word_index(input_file):
    word_map = dict()
    line_no = 0

    for line in input_file:
        line_no += 1
        # YOUR COMMENT
        word_lst = line.strip().split()

        # YOUR COMMENT
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]

        for word in word_lst:

            if word != "":
                if word not in word_map:
                    word_map[word] = {line_no}
                else:
                    word_map[word].add(line_no)

    return word_map


def print_word_index(word_map):
    index_lst = sorted(list(word_map.items()))

    for word, line_set in index_lst:
        line_lst = sorted(list(line_set))
        line_str = str(line_lst[0])
        for line_no in line_lst[1:]:
            line_str += ", {}".format(line_no)
        print("{:14s}:".format(word), line_str)

    ## Alternative way to create the line_str
    ## line_str = ",".join([str(i) for i in line_lst])


def main():
    filename = 'document1.txt'  # input( "Name of file to be processed: " )

    try:
        file = open(filename, "r")

        index = build_word_index(file)

        print_word_index(index)

        file.close()

    except IOError:

        print("Halting -- unable to open", filename)


main()