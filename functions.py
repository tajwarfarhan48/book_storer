user_books = []  # All of the user's books are stored in this list. Each book is stored as '[name, author, yes/no(read status)]'.
counter = 0  # For counting the number of books in a specific portion of the list requested by the user


def startup_csv():  # For starting up the .csv version of the application
    try:
        with open('books.txt', 'r') as file:
            read_from_csv('books.txt')
    except FileNotFoundError:
        with open('books.txt', 'w') as file:
            pass


def read_from_csv(filename):  # Retrieves the user's books from a .csv file. Must be run at the start of the program if the .csv version is used.
    global user_books

    with open(filename, 'r') as file:
        user_books = [line.strip().split(',') for line in file.readlines()[1:]]  # Takes each line in the file, removes the '\n' character, and separates it into a list as described at the top of the program.


def write_to_csv(filename):  # Writes the updated book list to a .csv file. This function must be called at the end of any changes to the user's book list if the .csv version is used.
    global user_books

    with open(filename, 'w') as file:
        for book in user_books:  # This section of the code writes each book in the user's book list to the file specified.
            name = book[0]
            author = book[1]
            status = book[2]
            file.write(f'{name},{author},{status}\n')


def view_list(book_list, filter_word):  # Views a specific portion of the entire list according to the demands of the user.
    global counter

    for book in book_list:  # For filtering the book list such that only the books demanded by the user will be shown
        if book[2] == filter_word:  # Filtering is done using the 'status' property of the book. The filter_word parameter should have either a 'yes' or 'no' value.
            counter += 1
            name = book[0]
            author = book[1]
            print('')
            print(f'''Name: {name}, Author: {author}''')


def view_read_later_list():  # For viewing the 'READ LATER' list
    global counter
    global user_books

    print('')
    print('Your Read Later list: ')

    view_list(user_books, 'no')  # Only filters the books the users hasn't read yet

    print('')
    print(f'There are {counter} book(s) in your reading list.')
    print('')

    counter = 0  # Resets the counter


def view_finished_list():  # For viewing the 'FINISHED' list
    global counter
    global user_books

    print('')
    print('Your Finished list: ')

    view_list(user_books, 'yes')  # Only filters the books the user has finished reading

    print('')
    print(f'You have finished reading {counter} book(s).')
    print('')

    counter = 0  # Resets the counter


def add_book():  # For adding a new book to either the user's 'READ LATER' or 'FINISHED' list
    global user_books

    print('')
    new_book_name = input('Please enter the name of the book you wish to add. Press x to cancel: ')  # Asks the user to enter the name of the new book

    while new_book_name == '':  # This section prevents blank responses
        print('')
        print('You cannot leave this field blank.')
        print('')
        new_book_name = input('Please enter the name of the book you wish to add. Press x to cancel: ')

    if new_book_name == 'x':  # For cancelling the operation
        print('')
        return None

    for book in user_books:  # Checks whether the new book is already in the list
        if book[0] == new_book_name:
            print('')
            print(f'This book is already in your {"Read Later" if book[2] == "no" else "Finished"} list.')
            print('')
            return None

    print('')
    new_book_author = input('Please enter the name of the author. Press x to cancel: ')  # Asks the user for the author

    while new_book_author == '':  # This section prevents blank responses
        print('')
        print('You cannot leave this field blank.')
        print('')
        new_book_author = input('Please enter the name of the author. Press x to cancel: ')

    if new_book_author == 'x':
        print('')
        return None

    print('')
    new_book_status = input('Have you read this book already? Press y for yes and n for no. Press x to cancel: ')  # Asks the user whether they have finished reading the book

    valid_inputs = ['y', 'n', 'x']

    while new_book_status not in valid_inputs:  # This section prevents invalid responses
        print('')
        print('Please enter a valid input.')
        print('')
        new_book_status = input('Have you read this book already? Press y for yes and n for no. Press x to cancel: ')

    if new_book_status == 'x':
        print('')
        return None

    elif new_book_status == 'y':
        new_book = [new_book_name, new_book_author, 'yes']

    else:
        new_book = [new_book_name, new_book_author, 'no']

    user_books.append(new_book)
    write_to_csv('books.txt')   # Saves the changes

    print('')
    print(f'Your book has been successfully added to the {"Read Later" if new_book[2] == "no" else "Finished"} list.')
    print('')


def remove_book():  # For removing a book from the user's list
    global user_books

    print('')
    book_name = input('Please enter the name of the book you wish to remove. Press x to cancel: ')  # Asks the user for the name of the book they wish to remove

    while book_name == '':  # Prevents blank responses
        print('')
        print('You cannot leave this field blank.')
        print('')

    if book_name == 'x':
        print('')
        return None

    for book in user_books:  # Searches for the book and removes it when found
        if book[0] == book_name:
            status = book[2]
            user_books.remove(book)
            write_to_csv('books.txt')  # Saves the changes

            print('')
            print(f'The book has been removed from your {"Read Later" if status == "no" else "Finished"} list.')
            print('')
            return None

    print('')  # This section of the code runs when the book is not in the list.
    print('This book is not in any of your lists.')
    print('')
