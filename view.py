from notes import *


def split_string(text, max_length):
    words = text.split()
    result = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += " " + word if current_line else word
        else:
            result.append(current_line)
            current_line = word
    if current_line:
        result.append(current_line)
    return result


def show_note(filename: str, index: str):
    ds = read_note_from_file(filename)
    if index not in ds:
        print()
        print(f'Заметки с идентфикатором {index} не существует ')
        return
    print('╒═══════════╤══════════════════════════════════════╤═════════════════════╤═════════════════════╕')
    print('│ № записи  │ Имя заметки                          │ Создана             │ Изменена            │')
    print('├───────────┼──────────────────────────────────────┼─────────────────────┼─────────────────────┤')
    print('│ ', end='')
    print("{0:<10}".format(index), end='│ ')
    print("{0:<37}".format(ds[index][name]), end='│ ')
    print("{0:<20}".format(ds[index][time_create][:19:]), end='│ ')
    print("{0:<20}".format(ds[index][time_changed][:19:]), end='│ ')
    print()
    print('├───────────┴──────────────────────────────────────┴─────────────────────┴─────────────────────┤')
    max_line = 93
    text = split_string(ds[index][body], max_line)
    for i in range(len(text)):
        print('│ ', end='')
        print("{0:<93}".format(text[i]), end='│ ')
        print()
    print('╘══════════════════════════════════════════════════════════════════════════════════════════════╛')
    print()


def show_notes_list(ds: dict):
    print('Список заметок')
    print('╒═══════════╤══════════════════════════════════════╤═════════════════════╤═════════════════════╕')
    print('│ № записи  │ Имя заметки                          │ Создана             │ Изменена            │')
    print('├───────────┼──────────────────────────────────────┼─────────────────────┼─────────────────────┤')
    for k in ds.keys():
        print('│ ', end='')
        print("{0:<10}".format(k), end='│ ')
        print("{0:<37}".format(ds[k][name]), end='│ ')
        print("{0:<20}".format(ds[k][time_create][:19:]), end='│ ')
        print("{0:<20}".format(ds[k][time_changed][:19:]), end='│ ')
        print()
    print('╘══════════════════════════════════════════════════════════════════════════════════════════════╛')

