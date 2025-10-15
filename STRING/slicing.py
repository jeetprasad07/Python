# slicing of the string,,,

name = "jeetprasad"
"""
    J E E T P R A S A D
    0 1 2 3 4 5 6 7 8 9
"""

print(name[1:4]) # "eet" last idx will not included

print(name[:4]) # equal to [0:4] "jeet"

print(name[1:]) # eetprasad

print(name[3:8]) # "tpras"

print(name[2:7]) # "etpra"

# Nagative index......
 
str = "APPLE"
"""
    A  P  P  L  E
   -5 -4 -3 -2 -1
"""

print(str[-3:-1]) # "PL"