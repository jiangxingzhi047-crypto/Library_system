from book import Book
from reader import Reader


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.readers: dict[int, Reader] = {}

    # -------- 注册相关 --------
    def add_book(self, book: Book):
        self.books[book.title] = book

    def add_reader(self, reader: Reader):
        self.readers[reader.reader_id] = reader

    # -------- 借还逻辑 --------
    def borrow_book(self, reader_id: int, book_title: str) -> bool:
        if reader_id not in self.readers:
            raise ValueError("读者不存在")
        if book_title not in self.books:
            raise ValueError("图书不存在")

        reader = self.readers[reader_id]
        book = self.books[book_title]

        if not reader.can_borrow():
            raise RuntimeError("超过最大借阅数量")

        if not book.borrow(reader):
            return False

        reader.add_book(book)
        return True

    def return_book(self, reader_id: int, book_title: str) -> bool:
        reader = self.readers.get(reader_id)
        book = self.books.get(book_title)

        if not reader or not book:
            raise ValueError("读者或图书不存在")

        book.return_book()
        reader.remove_book(book_title)
        return True

    # -------- 统计功能 --------
    def borrowed_books(self):
        return [book for book in self.books.values() if book.is_borrowed]

    def readers_with_unreturned_books(self):
        return [reader for reader in self.readers.values() if reader.has_unreturned_books()]
