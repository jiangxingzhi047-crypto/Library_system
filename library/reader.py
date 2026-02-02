from book import Book

class Reader:
  MAX_BORROW_LIMIT = 3

  def __init__(self,name:str,reader_id:int):
    self.name = name
    self.reader_id = reader_id
    self.borrowed_books:dict[str,Book] = {}

  def can_borrow(self,book:Book):
    self.borrowed_books[book.title] = book

  def remove_book(self,book_title:str):
    if book_title not in self.borrowed_books:
      raise KeyError("该读者未借阅此书")
    del self.borrowed_books[book_title]

  def has_unreturned_books(self) ->bool:
    return bool(self.borrowed_books)
    
