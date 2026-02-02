class Book:
  def __init__(self,title:str,author:str):
    self.title = title
    self.author = author
    self.is_borrowed = False
    self.borrower = None

  def borrow(self,reader) ->bool:
    if self.is_borrowed:
      return False
    self.is_borrowed = True
    self.borrower = reader
    return True

  def return_book(self) -> bool:
    if not self.is_borrowed :
      return False
    self.is_borrowed = False
    self.borrower = None
    return True


  def to_dict(self) -> dict:
    return {
      "title": self.title,
        "author": self.author,
        "is_borrowed": self.is_borrowed,
        "borrower_id": self.borrower.reader_id if self.borrower else None
      }
