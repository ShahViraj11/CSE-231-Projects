import math

Rods = float(input("Input rods: \n"))
print(f'You input {Rods} rods.')
A = Rods * 5.0292
B = Rods * 16.5
C = Rods * 0.00312500776
D = Rods / 40
Time = Rods * 0.06048402116
print("\nConversions")
print("Meters:", round(A, 3))
print("Feet:", round(B, 3))
print("Miles:", round(C, 3))
print("Furlongs:", round(D, 3))
print(f'Minutes to walk {Rods} rods: {round(Time, 3)}')
