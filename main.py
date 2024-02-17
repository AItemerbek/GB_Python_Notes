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


switch = {
    'menu': view_menu,
    'read': view_note,
    'notes': view_all_notes
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