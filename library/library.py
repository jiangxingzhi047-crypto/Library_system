from .exceptions import *


def borrow_book(self, reader_id, book_title):
    if reader_id not in self.readers:
        raise ReaderNotFoundError()

    if book_title not in self.books:
        raise BookNotFoundError()

    reader = self.readers[reader_id]
    book = self.books[book_title]

    if not reader.can_borrow():
        raise BorrowLimitExceededError()

    if book.is_borrowed:
        raise BookAlreadyBorrowedError()

    book.borrow(reader)
    reader.add_book(book)
