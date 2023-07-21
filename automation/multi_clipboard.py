import sys
from click import command
import clipboard
import json
import pprint

SAVED_DATA = "clipboard.json"


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data loaded tp the clipboard")
        else:
            print("Key doent exist")
    elif command == "list":
        pprint.pprint(data)
    elif command == "delete":
        key = input("Enter a key: ")
        if key in data:
            del data[key]
            save_items(SAVED_DATA, data)
            print("Key deleted")
        else:
            print("Key doent exist")
    else:
        print("Unknown command")

else:
    print("Please insert exactly one command (save,load,list,delete)")
