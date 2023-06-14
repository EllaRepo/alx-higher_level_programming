#!/usr/bin/python3
""" This module defines a script that adds all arguments to a Python list,
    and then save them to a file
"""
import os.path
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

f_list = []
filename = "add_item.json"
if os.path.exists(filename):
    f_list = load_from_json_file(filename)

for arg in argv[1:]:
    f_list.append(arg)
save_to_json_file(f_list, filename)
