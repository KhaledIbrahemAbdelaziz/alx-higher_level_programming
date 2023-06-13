#!/usr/bin/python3
"""Define the add_item function"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    try:
        l = load_from_json_file(filename)
    except:
        l = []
    for i in sys.argv[1:]:
        l.append(i)
    save_to_json_file(l, filename)
