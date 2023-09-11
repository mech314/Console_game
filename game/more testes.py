import Locations

width = 26
hight = 3

print("-" * width)
for x in range(0, hight-1):
    if x == 1:
        print("-", " " * 7, Locations.loc_0_0.coordinates, " " * 7, "-")
    print("-" + " " * (width-2) + "-")

print("-" * width)