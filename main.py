from notes import *
from view import *
from messages import *

filename = 'test.json'


def view_menu():
    print(menu)


def view_note():
    index: str = input(note_index)
    show_note(filename, index)


def view_all_notes():
    data = read_note_from_file(filename)
    show_notes_list(data)


def add_note():
    new_note = create_notes()
    print(need_to_save)
    answer = input(choice)
    if answer == '1':
        print_note_to_file(filename, new_note)
        new_note_name = new_note[name]
        print(f'Запись {new_note_name} успешно сохранена ')


def delete_note():
    index: str = input(note_index)
    print(need_to_read_before)
    answer = input(choice)
    if answer == '1':
        show_note(filename, index)
    print(need_delete)
    answer = input(choice)
    if answer == '1':
        erase_note(filename, index)


def edit_note():
    index: str = input(note_index)
    print(need_to_read_before)
    answer = input(choice)
    if answer == '1':
        show_note(filename, index)
    print(need_adit)
    answer = input(choice)
    if answer == '1':
        change_note(filename, index)


switch = {
    'menu': view_menu,
    'read': view_note,
    'notes': view_all_notes,
    'add': add_note,
    'del': delete_note,
    'edit': edit_note
}


def main():
    print(wellcome)
    while True:
        key = input(command)
        if key == 'exit':
            break
        if key not in switch:
            continue
        switch[key]()


if __name__ == '__main__':
    main()
