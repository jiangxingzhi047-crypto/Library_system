from book import Book
from reader import Reader
from library import Library


def main():
    library = Library()

    # 添加书籍
    library.add_book(Book("Python 入门", "Guido"))
    library.add_book(Book("算法导论", "CLRS"))

    # 添加读者
    alice = Reader("Alice", 1)
    bob = Reader("Bob", 2)

    library.add_reader(alice)
    library.add_reader(bob)

    # 借书
    library.borrow_book(1, "Python 入门")
    library.borrow_book(2, "算法导论")

    # 统计
    print("已借出书籍：")
    for book in library.borrowed_books():
        print(f"{book.title} -> {book.borrower.name}")

    print("\n有未还书的读者：")
    for reader in library.readers_with_unreturned_books():
        print(reader.name)


if __name__ == "__main__":
    main()
