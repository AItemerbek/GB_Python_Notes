import datetime
import json


def create_notes():
    note_name = input('Input note name: ')
    note_body = input('Input your notes: ')
    note = dict()
    note['name'] = note_name
    note['body'] = note_body
    note['timeCreate'] = datetime.datetime.now().isoformat()
    note['timeChanged'] = datetime.datetime.now().isoformat()
    return note


def print_dict_to_file(filename: str, new_data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)
    print()


print(create_notes())
print_dict_to_file('notes.json', create_notes())