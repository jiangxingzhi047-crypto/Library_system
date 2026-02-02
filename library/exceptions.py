class LibraryError(Exception):
    """图书馆系统的基础异常"""
    pass


class BookNotFoundError(LibraryError):
    pass


class ReaderNotFoundError(LibraryError):
    pass


class BookAlreadyBorrowedError(LibraryError):
    pass


class BorrowLimitExceededError(LibraryError):
    pass
