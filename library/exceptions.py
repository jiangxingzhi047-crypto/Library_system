class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
    pass


class ReaderNotFoundError(LibraryError):
    pass


class BookAlreadyBorrowedError(LibraryError):
    pass


class BorrowLimitExceededError(LibraryError):
    pass
