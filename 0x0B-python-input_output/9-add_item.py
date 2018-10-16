#!/usr/bin/python3
""" adds all arguments to a Python list, and save the list to a file """


if __name__ == "__main__":
    save = __import__('7-save_to_json_file').save_to_json_file
    load = __import__('8-load_from_json_file').load_from_json_file
    from sys import argv
    import json
    try:
        l = load("add_item.json")
        l.extend([e for e in argv[1:]])
    except FileNotFoundError:
        l = [e for e in argv[1:]]
    finally:
        save(l, "add_item.json")
