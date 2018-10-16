#!/usr/bin/python3
""" adds all arguments to a Python list, and save the list to a file """


if __name__ == "__main__":
    save = __import__('7-save_to_json_file').save_to_json_file
    load = __import__('8-load_from_json_file').load_from_json_file
    from sys import argv
    import json
    try:
        f = open("add_item.json", 'r')
        l = json.loads(f.readline())
        l.extend([e for e in argv[1:]])
    except FileNotFoundError:
        l = [e for e in argv[1:]]
    finally:
        f = open("add_item.json", 'w')
        f.write(json.dumps(l))
        f.close()
