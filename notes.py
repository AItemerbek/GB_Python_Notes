import datetime
import json
import os
import lorem

notesfile = 'notes.json'
name = 'name'
body = 'body'
time_create = 'time_create'
time_changed = 'time_changed'


def create_notes():
    note_name = input('Input note name: ')
    note_body = input('Input your notes: ')
    note = dict()
    note[name] = note_name
    note[body] = note_body
    note[time_create] = datetime.datetime.now().isoformat()
    note[time_changed] = datetime.datetime.now().isoformat()
    return note


def print_note_to_file(filename: str, data: dict):
    notes = dict()
    if file_exist(filename):
        notes = read_note_from_file(filename)
        notes[count_notes(filename) + 1] = data
    else:
        notes[1] = data
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


def print_all_notes_to_file(filename: str, data: dict):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_note_from_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def file_exist(filename: str):
    return os.path.isfile(filename)


def count_notes(filename: str):
    if not file_exist(filename):
        return 0
    data = read_note_from_file(filename)
    return len(data)


def show_all_notes(filename: str):
    if count_notes(filename) == 0:
        print('База заметок пуста или не существует')
        return
    data = read_note_from_file(filename)
    for key in data.keys():
        print(
            f'Идентификатор: {key}, Имя записи: {data[key][name]}, Дата последнего изменения: {data[key][time_changed]}')


def change_note(filename: str, index: str):
    if count_notes(filename) == 0:
        print('База заметок пуста или не существует')
        return
    data = read_note_from_file(filename)
    data[index][body] = input('Введите новый текст заметки: ')
    data[index][time_changed] = datetime.datetime.now().isoformat()

    print_all_notes_to_file(filename, data)
    print(f'Запись № {index}  {data[index][name]} была успешно изменена в {data[index][time_changed]}')


# Support method
def create_random_notes(quantity: int):
    filename = 'test.json'
    ds = dict()
    for i in range(0, quantity):
        ds['name'] = 'note_' + str(i)
        ds['body'] = lorem.lorem
        ds['time_create'] = datetime.datetime.now().isoformat()
        ds['time_changed'] = datetime.datetime.now().isoformat()
        print_note_to_file(filename, ds)


# create_random_notes(10)
show_all_notes('test.json')
change_note('test.json', '2')
