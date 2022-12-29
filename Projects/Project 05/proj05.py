###########################################################
#  Viraj Shah's CSE 231 #5
#
#  The project detects if the planet habitable or not.
#    the input for the maximum distance from earth is prompted.
#    the distance should be entered in light years.
#    if wrong input is entered then the user is prompted again for input.
#    the five functions defined before main are called to get required output
#    the output is rounded of up to two decimal points.
#    entire discription of planet is printed with the defined functions.
#    after showing data for one input the file is closed.
#    the program does not contain a closing message.
###########################################################
import math

# Constants
PI = math.pi
EARTH_MASS = 5.972E+24  # kg
EARTH_RADIUS = 6.371E+6  # meters
SOLAR_RADIUS = 6.975E+8  # radius of star in meters
AU = 1.496E+11  # distance earth to sun in meters
PARSEC_LY = 3.262


def open_file(): #function to open the files provided
    file_pointer = input("Input data to open: ")
    while True:
        try:
            file_pointer = open(file_pointer + '.csv')
            break
        except:
            print("\nError: file not found.  Please try again.")
            file_pointer = ""
            file_pointer = input("Enter a file name: ")
    return file_pointer


def make_float(s): #function to make the input float
    try:
        s = float(s)
        return s
    except ValueError:
        return -1


def get_density(mass, radius): #function to calculate density
    if mass < 0 or radius < 0 or mass == 0:
        return -1
    else:
        new_mass = mass * EARTH_MASS
        new_radius = radius * EARTH_RADIUS
        Vol_m = 4 * PI * (new_radius ** 3) / 3
        Density = new_mass / Vol_m
    return Density


def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound): #function to calculate temperature
    star_radius = star_radius * SOLAR_RADIUS
    axis = axis * AU
    planet_temp = star_temp * math.sqrt(abs(star_radius) / (2 * abs(axis))) * (1 - albedo) ** 0.25
    if axis < 0 or star_temp < 0 or star_radius < 0 or albedo < 0 or low_bound < 0 or upp_bound < 0:
        return False
    elif low_bound < planet_temp < upp_bound:
        return True
    else:
        return False


def get_dist_range(): #function to calculate maximum distance
    p = input("\nEnter maximum distance from Earth (light years): ")
    try:
        if float(p) <= 0:
            print("\nError: Distance needs to be greater than 0.")
            return get_dist_range()
        else:
            p = float(p)
            return p
    except ValueError:
        if p != float():
            print("\nError: Distance needs to be a float.")
            return get_dist_range()


global closestr #assignment of some global functions
closestr = ""

global closest_distr
closest_distr = ""

global closest_distg
closest_distg = ""


def main(): #main function
    print('''Welcome to program that finds nearby exoplanets '''
          '''in circumstellar habitable zone.''')
    fp = open_file() #calling function to open file
    z = get_dist_range() #calling function to get maximum distance
    newz = z / PARSEC_LY #conversion
    bound = 1000000000 
    bound1 = 10000000000000000
    low_bound = 200 #setting boundaries as laid in the pdf
    upp_bound = 350
    albedo = 0.5
    fp.readline() #reading files line by line
    max_star, max_planet = -1, -1
    total_mass, count, count2, count3, count4 = 0, 0, 0, 0, 0
    for line in fp:
        init_dist = line[114:]
        init_dist = make_float(init_dist)

        if 0 < init_dist < newz: #setting boundary for distance
            planet_radius, planet_mass = line[78:85], line[86:96]
            star_temp, star_radius = line[97:105], line[106:113]
            planet_axis, planet_name = line[66:77], line[:25]
            planet_radius = make_float(planet_radius) #calling float function
            planet_mass = make_float(planet_mass)
            star_temp = make_float(star_temp) #calling float function
            star_radius = make_float(star_radius)
            planet_axis = make_float(planet_axis) #calling float function
            if max_star < int(line[50:57]): #using min-max algorithm
                max_star = int(line[50:57])
            if max_planet < int(line[58:65]):
                max_planet = int(line[58:65])
            if planet_mass != -1:
                count = count + 1
                total_mass = total_mass + planet_mass #calculating planet's mass
                x = total_mass / count
            planet_density = get_density(planet_mass, planet_radius) #calling density function
            if temp_in_range(planet_axis, star_temp, star_radius, albedo, low_bound, upp_bound): #calling temperature function
                count2 += 1
                if 0 < planet_mass < 10 or 0 < planet_radius < 1.5 or planet_density > 2000: #finding if planet is gaseous or rocky
                    count3 += 1
                    if init_dist < bound: #checking for the nearest rocky planet
                        bound = init_dist
                        global closestr
                        closestr = line[:25]
                        global closest_distr
                        closest_distr = round(float(line[114:]) * PARSEC_LY, 2)
                else:
                    count4 += 1
                    if init_dist < bound1: #checking for the nearest gaseous planet
                        bound1 = init_dist
                        closestg = line[:25]
                        global closest_distg
                        closest_distg = round(float(line[114:]) * PARSEC_LY, 2)
        else:
            continue
            #using print statements to get  desired output
    print("\nNumber of stars in systems with the most stars: {}.".format(max_star))
    print("Number of planets in systems with the most planets: {}.".format(max_planet))
    print("Average mass of the planets: {} Earth masses.".format(round(x, 2)))
    print("Number of planets in circumstellar habitable zone: {}.".format(count2))
    if count3 == 0:
        print("No rocky planet in circumstellar habitable zone.")
    else:
        print("Closest rocky planet in the circumstellar habitable zone {} is {} light years away.".format(closestr.strip(),
                                                                                                           closest_distr))
    if count4 == 0:
        print("No gaseous planet in circumstellar habitable zone.")
    else:
        print(
            "Closest gaseous planet in the circumstellar habitable zone {} is {} light years away.".format(closestg.strip(),
                                                                                                               closest_distg))
    fp.close()


if __name__ == "__main__":
    main()