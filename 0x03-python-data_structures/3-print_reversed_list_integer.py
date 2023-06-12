#!/usr/bin/python3
# This script prints all items
# in input list in reverse

def print_reversed_list_integer(my_list=[]):
	if my_list:
        	for num in range(len(my_list) - 1, -1, -1):
            		print("{:d}".format(my_list[num]))
