#!/usr/bin/env python3

import sys

lines = []
for line in sys.stdin:
    line = line.strip().split()
    lines.append(line)

########## EDIT HERE ##########
#combiner for mapper.py and reducer.py
#sort by quality and service

lines.sort(key=lambda x: (int(x[2]), int(x[3])))
skyline = []

for id_a, city_a, quality_a, service_a, price_a in lines:
    #just combine
    skyline.append((id_a, city_a, quality_a, service_a, price_a))
########## EDIT HERE ##########

for point in skyline:
    print("{0} {1} {2} {3} {4}".format(point[0], point[1], point[2], point[3], point[4]))