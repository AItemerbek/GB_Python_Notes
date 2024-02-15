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


def print_note_to_file(filename: str, data: dict):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print()


def print_note(data: dict):
    print(f"Название заметки: {data['name']} ")
    print(f"{data['body']}")


def read_note(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


new_note = create_notes()

print_note(new_note)
print_note_to_file('new.json', new_note)
note = read_note('new.json')
print(note)
