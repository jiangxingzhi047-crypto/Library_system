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
