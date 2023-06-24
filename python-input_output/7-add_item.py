#!/usr/bin/python3
""" script that adds all arguments to a Python list,
and then save them to a file"""


from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

fname = "add_item.json"

try:
    content = load_from_json_file(fname)
except FileNotFoundError:
    content = []

save_to_json_file(content + argv[1:], fname)
