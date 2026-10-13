#!/usr/bin/env python3
for number in range(99):
    print("{:d} = {:#x}".format(number, number), end="\n" if number == 98 else "\n")
