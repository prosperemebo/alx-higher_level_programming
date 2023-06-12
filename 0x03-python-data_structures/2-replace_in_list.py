#!/usr/bin/python3
# Replaces item in list at index

def replace_in_list(my_list, idx, element):
	if (idx < 0 or idx >= len(my_list)):
		return my_list
	else:
		my_list[idx] = element
		return my_list