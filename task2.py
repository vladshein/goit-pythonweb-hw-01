# task2
from typing import List
from abc import ABC, abstractmethod
from logger_config import logger


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title: str = title
        self.author: str = author
        self.year: str = year


# ABC Library interface
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        logger.info(f"Book {book.title} was successfully added")

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info(f"Book {book.title} was successfully removed")
                break

    def show_books(self):
        for book in self.books:
            logger.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )


class LibraryManager:
    def __init__(self, library: Library):
        self.library: Library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        if title == "" or title not in [book.title for book in self.library.books]:
            logger.info(f"Book {title} not found")
            return
        self.library.remove_book(title)

    def show_books(self):
        if len(self.library.books) == 0:
            logger.info("Library is empty.")
            return
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
