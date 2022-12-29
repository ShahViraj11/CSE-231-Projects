###############################################################################
#
#   Viraj's CSE 231 Project 7
#
#   Purpose: This assignment focuses on the design, implementation, and testing of a
#             python program that uses lists and tuples.
#
#   Algorithm:
#   define functions:
#      open_file()
#      read_reviews()
#      read_movies()
#      year_movies()
#      genre_movies()
#      gen_users()
#      occ_users()
#      highest_rated_by_movie()
#      highest_rated_by_reviewer()
#           main()
#           merges all the functions according to the respective inpu
#
############################################################################
GENRES = ['Unknown', 'Action', 'Adventure', 'Animation', "Children's",
          'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''


def open_file(s):
    """
    This function prompts for a file name input and returns the corresponding
    file pointer if the file name is valid; else will return an error message.
    returns: file pointer
    """
    x = input("\nInput {} filename: ".format(s))  # asking for file input
    while True:
        try:
            file_pointer = open(x, "r", encoding="windows-1252")  # opening the file
            break
        except:
            print('\nError: No such file; please try again.')  # printing out error if file name is invalid
            x = ""
            x = input("Input {} filename: ".format(s))  # formatting the input to ask for specific file
    return file_pointer


def read_reviews(N, fp):
    """
        This function prompts for a file name input and returns the corresponding
        file pointer if the file name is valid; else will return an error message.
        returns: file pointer
        """
    example_1 = []  # example list declaration
    for i in range(N + 1):  # N being the length defining the range
        example_1.append([])

    for line in fp:
        t = line.split('\t')
        example_1[int(t[0])].append((int(t[1]), int(t[2])))  # appending the file until required input
    for i in example_1:
        i.sort()  # sorting the list

    return example_1


def read_users(fp):
    """
        This function prompts for a file name input and returns the corresponding
        file pointer if the file name is valid; else will return an error message.
        returns: file pointer
        """
    file_data = fp.read()  # reading the file
    file_data = file_data.split("\n")

    tup_list = []  # declaring lists
    master_list = []

    for line in file_data[0:]:  # running for loop for lines since index 0
        if line == "":
            break
        else:
            x = line.split("|")  # splitting the lines by "|" as asked
            x[0] = int(x[0])
            x[1] = int(x[1])
            x[2] = str(x[2])
            x[3] = str(x[3])
            x = [x[1], x[2], x[3]]
            tup_list.append(tuple(x))  # appending the list as required
    tup_list.insert(0, [])

    return tup_list


def read_movies(fp):
    """
       This function reads movies file. It breaks in case of an empty string
       reads the lines in the files from index 0 while looking at all data types at
       different indices. Appends the list accordingly and returns a master list.
        """
    file_data = fp.read()
    file_data = file_data.split("\n")

    list_list = []
    master_list = [[]]

    for line in file_data[0:]:
        if line == "":
            break
        else:
            x = line.split("|")
            del x[3]
            x[0] = int(x[0])
            x[1] = str(x[1])
            x[2] = str(x[2])
            x[3] = str(x[3])
            temp_list = x[4:]
            genre_list = []
            for count, i in enumerate(temp_list):
                if int(i) == 1:
                    genre_list.append(GENRES[count])

            x = (x[1], x[2], genre_list)

            for i in list_list:
                master_list.append(i)
            master_list.append(x)

    return master_list


def year_movies(year, L_movies):
    """
        This function checks for the movies in a specific year. This function filters the main movie list
         to find movies for a specific year and returns their specific movie ids by
         also sorting them.
        """
    return_lists = []
    for count, i in enumerate(L_movies):
        if not i:
            pass
        else:
            if i[1][-4:] != '':
                if int(i[1][-4:]) == int(year):
                    return_lists.append(count)
    return_lists.sort()
    return return_lists


def genre_movies(genre, L_movies):
    """
        This function filters the main movie list to find movies for a specific genre and
        returns their ids as a list.Movies having multiple genres only those are counted where
        the movie has particular genre as asked.
        """
    return_list2 = []
    for count, i in enumerate(L_movies):
        if not i:
            pass
        else:
            if i[2] != '':
                if genre in str(i[2]):
                    return_list2.append(count)
    return_list2.sort()
    return return_list2


def gen_users(gender, L_users, L_reviews):
    """
        This function filters the main reviews list to find reviews for a specific
        gender of users and returns them as a list of lists. It finds users in
        L_users and maps their IDs onto the the review file to see their reviews
        """
    return_list3 = []
    for i in range(len(L_users)):
        if len(L_users[i]) == 0:
            continue
        elif L_users[i][1] == gender:
            return_list3.append(L_reviews[i])
    return return_list3


def occ_users(occupation, L_users, L_reviews):
    """
        This function filters the main reviews list to find records for a specific
        occupational group of users and returns them as a list of lists of tuples.
        It finds users in L_users and maps their IDs onto the the review file
        to see their reviews
        """
    return_list3 = []
    for i in range(len(L_users)):
        if len(L_users[i]) == 0:
            continue
        elif L_users[i][2] == occupation:
            return_list3.append(L_reviews[i])
    return return_list3


def highest_rated_by_movie(L_in, L_reviews, N_movies):
    """
            This function calculates the average rating for the reviews in L_reviews list of the
            movies in L_in list and returns a list of the highest average rated movies and the highest
            average.
            Returns: master_list(list), maximum value of average list
            """
    ratings, movie_counter, average_list = [0] * len(L_in), [0] * len(L_in), [0] * len(L_in)
    for level1 in L_reviews:
        for level2 in level1:
            if level2[0] in L_in:
                ratings[L_in.index(level2[0])] += level2[1]
                movie_counter[L_in.index(level2[0])] += 1

    for count, i in enumerate(average_list): average_list[count] = ratings[count] / movie_counter[count]
    average_list = [round(i, 2) for i in average_list]
    list1 = [count for count, i in enumerate(average_list) if i == max(average_list)]
    master_list = [L_in[i] for i in list1]
    return master_list, max(average_list)


def highest_rated_by_reviewer(L_in, N):
    """
            This function calculates the average rating for movies by a specific group of users (L_in)
            and returns a list of the highest average rated movies and the highest average.
            After that the function proceeds just as the highest_rated_by_movie function.
            Returns: movie_list (list) and maximum value of average list (float)
            """

    movie_list, master_list = [], []
    for level1 in L_in:
        for movies in level1:
            if movies[0] not in movie_list:
                movie_list.append(movies[0])

    ratings, movie_counter, average_list = [0] * len(movie_list), [0] * len(movie_list), [0] * len(movie_list)
    movie_list.sort()
    for level1 in L_in:
        for movies in level1:
            index = movie_list.index(movies[0])
            ratings[index] += movies[1]
            movie_counter[index] += 1

    for count, i in enumerate(average_list): average_list[count] = ratings[count] / movie_counter[count]
    average_list = [round(i, 2) for i in average_list]
    list1 = [count for count, i in enumerate(average_list) if i == max(average_list)]

    return [i for count, i in enumerate(movie_list) if count in list1], max(average_list)


def main():
    new_1 = open_file('users')  # calling open file function for users file
    new_2 = open_file('reviews')  # calling open file function for reviews file
    new_3 = open_file('movies')  # calling open file function for movies file
    main_list1 = read_users(new_1)  # calling read_users function for reading file opened by open function
    fp = len(main_list1)  # fp  is length of content in users.txt
    main_list2 = read_reviews(fp, new_2)  # calling read_reviews function with respective parameters
    main_list3 = read_movies(new_3)  # calling read_movies function with parameter as file movies.txt
    ac = len(main_list3)
    print(MENU)

    while True:  # running the code until user enters 5 as value of x
        x = input('\nSelect an option (1-5): ')  # asking for input from user
        try:
            x = int(x)
            if x not in range(1,6):# converting it into integer
                print("\nError: not a valid option.")
                continue
        except:
            print("\nError: not a valid option.")  # if input not being in required range
            continue

        if x == 1:  # if input is 1
            while True:
                year_in = input('\nInput a year: ')
                try:
                    year_in = int(year_in)
                except:
                    print("\nError in year.")
                    continue
                if year_in not in range(1930, 1998):  # year being in predefined range
                    print("\nError in year.")  # printing out error if not in range
                    continue
                fun_call1 = year_movies(year_in, main_list3)
                movie_ID_list, highest_rate = highest_rated_by_movie(fun_call1, main_list2, ac)
                print('\nAvg max rating for the year is:', highest_rate)
                for ID in movie_ID_list:
                    print(main_list3[ID][0])
                break

        elif x == 2:  # if input is 2

            print('\nValid Genres are: ', GENRES)  # printing out all valid genres
            while True:
                genre_inp = input('Input a genre: ')
                try:
                    genre_inp = genre_inp.split("-")
                    genre_inp[1] = genre_inp[1].lower()
                    genre_inp = genre_inp[0] + "-" + genre_inp[1]
                except:
                    genre_inp = str(genre_inp[0])
                example2 = [gen.upper() for gen in GENRES]
                if (genre_inp.upper() not in example2) or genre_inp.isdigit() == True:
                    print("\nError in genre.")  # printing error if genre isn't in range
                    continue
                else:  # if condition is satisfied then calling required functions
                    fun_call3 = genre_movies(genre_inp.capitalize(),
                                             main_list3)  # calling genre movies function with respective parameters
                    movie_ID_list, highest_rate = highest_rated_by_movie(fun_call3, main_list2,
                                                                         ac)
                    print('\nAvg max rating for the Genre is:',
                          highest_rate)
                    for ID in movie_ID_list:
                        print(main_list3[ID][0])
                    break
                # printing out maximum average rating

        elif x == 3:  # if input is 3
            while True:
                gender_inp = str(input('\nInput a gender (M,F): '))
                gender_inp = gender_inp.upper()
                if gender_inp != 'F' and gender_inp != 'M':  # if gender input not being Male or Female
                    print("\nError in gender.") # prompting for input again
                    continue
                else:
                    fun_call5 = gen_users(gender_inp, main_list1,
                                          main_list2)  # calling gender users function with respective parameters
                    Mov_id, maximum_rate = highest_rated_by_reviewer(fun_call5,
                                                                     ac)  # calling reviewer function with respective parameters
                    print('\nAvg max rating for the Gender is:', maximum_rate)
                    for ID in Mov_id:
                        print(main_list3[ID][0])
                    break


        elif x == 4:  # if input is 4
            print('\nValid Occupatipns are: ', OCCUPATIONS)
            while True:
                occ_inp = input('Input an occupation: ')
                ac = occ_inp.lower()
                if ac not in OCCUPATIONS:  # converting input into lower case
                    print("\nError in occupation.")
                    continue
                else:
                    fun_call6 = occ_users(ac, main_list1,
                                          main_list2)  # calling occupation users function with respective parameters
                    Mov_id, maximum_rate = highest_rated_by_reviewer(fun_call6,
                                                                     ac)  # calling reviewer function with respective
                    print('\nAvg max rating for the occupation is:', maximum_rate)
                    for ID in Mov_id:
                        print(main_list3[ID][0])
                    break
                # parameters


        elif x == 5:  # if input is 5
            break  # quit the program


if __name__ == "__main__":
    main()