from view import *
import messages

filename = 'test.json'


def view_menu():
    print(messages.menu)


def view_note():
    index: str = input(messages.note_index)
    show_note(filename, index)


def view_all_notes():
    data = read_note_from_file(filename)
    show_notes_list(data)


def add_note():
    new_note = create_notes()
    print(messages.need_to_save)
    answer = input(messages.choice)
    if answer == '1':
        print_note_to_file(filename, new_note)
        new_note_name = new_note[name]
        print(f'Запись {new_note_name} успешно сохранена ')


def delete_note():
    index: str = input(messages.note_index)
    print(messages.need_to_read_before)
    answer = input(messages.choice)
    if answer == '1':
        show_note(filename, index)
    print(messages.need_delete)
    answer = input(messages.choice)
    if answer == '1':
        erase_note(filename, index)


def edit_note():
    index: str = input(messages.note_index)
    print(messages.need_to_read_before)
    answer = input(messages.choice)
    if answer == '1':
        show_note(filename, index)
    print(messages.need_adit)
    answer = input(messages.choice)
    if answer == '1':
        change_note(filename, index)


def notes_filter():
    start = input(messages.input_start_date)
    if check_date_format(start):
        end = input(messages.input_end_date)
        if check_date_format(end):
            ds = date_notes_select(filename, start, end)
            show_notes_list(ds)
        else:
            print(messages.date_format_error)
    else:
        print(messages.date_format_error)


switch = {
    'menu': view_menu,
    'read': view_note,
    'notes': view_all_notes,
    'add': add_note,
    'del': delete_note,
    'edit': edit_note,
    'filter': notes_filter
}


def main():
    print(messages.wellcome)
    while True:
        key = input(messages.command)
        if key == 'exit':
            break
        if key not in switch:
            continue
        switch[key]()


if __name__ == '__main__':
    main()
