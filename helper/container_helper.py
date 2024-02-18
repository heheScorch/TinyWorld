# -*- coding: utf-8 -*-


def is_list_intersect(list1, list2):
	for elem in list1:
		if elem in list2:
			return True
	return False
