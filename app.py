from utils.functions import *

menu_text = '''Welcome to Book List Keeper v.1.0!
- Press r to view the books on your Read Later list
- Press f to view the books on your Finished list
- Press a to add a book
- Press d to remove a book
- Press q to quit
- Your choice: '''

menu_dict = {
    'r': view_read_later_list,
    'f': view_finished_list,
    'a': add_book,
    'd': remove_book
}

menu_choices = ['r', 'f', 'a', 'd']

menu_input = ''


def menu():
    global menu_input

    menu_input = input(menu_text)

    if menu_input in menu_choices:
        menu_dict[menu_input]()

    elif menu_input == 'q':
        pass

    else:
        print('')
        print('Please enter a valid input.')
        print('')


startup_csv()

while menu_input != 'q':
    menu()

write_to_csv('books.txt')

print('')
print('Application closed.')