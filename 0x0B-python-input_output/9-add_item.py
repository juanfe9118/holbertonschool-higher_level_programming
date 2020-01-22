#!/usr/bin/python3
"""Load, add, save module"""


from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
for a in range(1, len(argv)):
    my_list.append(argv[a])
save_to_json_file(my_list, filename)
