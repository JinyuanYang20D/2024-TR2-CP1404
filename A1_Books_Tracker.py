"""..."""

from book import Book

"""
Name: Jinyuan Yang
Date started: 1/07/2024
GitHub URL: https://github.com/JinyuanYang20D/CP1404Practicals
"""

import csv
import random

books = open("books.csv", "r")
print(books.read())
books_list = [
    Book(**{"title": "Developing the Leader Within You", "author": "John Maxwell", "number of pages": "225", "completed": False}),
    Book(**{"title": "The 360 Degree Leader", "author": "John Maxwell", "number of pages": "369", "completed": True}),
    Book(**{"title": "In Search of Lost Time", "author": "Marcel Proust", "number of pages": "93", "completed": False}),
    Book(**{"title": "Starting Out with Python", "author": "Tony Gaddis", "number of pages": "744", "completed": True}),
]


def main():
    """Main function of the program"""
    uncompleted = [
        Book(**{"title": "Developing the Leader Within You", "author": "John Maxwell", "number of pages": "225", "completed": False}),
        Book(**{"title": "In Search of Lost Time", "author": "Marcel Proust", "number of pages": "93", "completed": False})
    ]
    print("Books to read 1.0 - by <Jinyuan Yang>")
    print("4 books loaded.")
    print("Menu:")
    print("D - Display books")
    print("A - Add new book")
    print("C - Complete a book")
    print("Q - Quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            list = list_books()
        elif choice == "A":
            add = add_book()
        elif choice == "C":
            complete = complete_book()
        else:
            save = save_books()
        print("Menu:")
        print("D - Display books")
        print("A - Add new book")
        print("C - Complete a book")
        print("Q - Quit")
        choice = input(">>> ").upper()
    print("6 books saved to books.csv")
    print("So many books to read, so little time :)")


def list_books():
    """List all books"""
    max_title_length = max(len(book.title) for book in books_list)
    max_author_length = max(len(book.author) for book in books_list)
    for book in books_list:
        title = book.title
        author = book.author
        completed = book.is_completed
        uncompleted = "*" if not completed else ""
        print(f"{title:{max_title_length}} | {author:{max_author_length}} | {uncompleted}")
    print("Menu:")
    print("D - Display books")
    print("A - Add new book")
    print("C - Complete a book")
    print("Q - Quit")
    choice = input(">>> ").upper()
    return choice


def add_book():
    """Add a new book"""
    title = input("Title: ")
    author = input("Author: ")
    page_number = input("Number of pages: ")
    while not title:
        title = input("Input can not be blank: ")
    while not author:
        author = input("Input can not be blank: ")
    while not page_number.isdigit():
        page_number = input("Invalid input - please enter a valid number: ")
    books_list.append(Book(**{'title': title, 'author': author, 'number of pages': int(page_number), 'completed': False}))
    print(f"{title} by {author} ( {page_number} pages) added.")
    print("Menu:")
    print("D - Display books")
    print("A - Add new book")
    print("C - Complete a book")
    print("Q - Quit")
    choice = input(">>> ").upper()
    return choice


def complete_book():
    """Mark a book as completed"""
    if len(uncompleted) > 0:
        print("List of all books:")
        for book in books_list:
            print("-", book)
        while True:
            chosen_book = input("Choose a book to mark as completed: ")
            if chosen_book not in books_list:
                print("Invalid book. Please choose a book from the list.")
            elif chosen_book not in uncompleted:
                print("This book has already been completed. Please choose an uncompleted book.")
            else:
                break
        uncompleted.remove(chosen_book)
        print(chosen_book, "has been marked as completed.")
    else:
        print("No uncompleted books.")
    print("Menu:")
    print("D - Display books")
    print("A - Add new book")
    print("C - Complete a book")
    print("Q - Quit")
    choice = input(">>> ").upper()
    return choice

def save_books():
    """Save books to books.csv"""
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Number of pages', 'Completed'])
        for book in books_list:
            writer.writerow([book['title'], book['author'], book['number of pages'], book['completed']])
    print(f'{len(books_list)} books saved to books.csv')
    while True:
        choice = input('Enter a book or "quit" to exit: ')
        if choice == 'quit':
            save_books()
            break
        else:
            books_list.append({'title': choice, 'author': 0, 'number of pages': 0, 'completed': False})
            print(f'{choice} added to books.csv')

main()
