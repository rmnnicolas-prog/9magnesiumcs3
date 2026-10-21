class Publication:
def __init__(self, title, author):
    self.__self = self
    self.__author = author

def set_title(self, title):
    self._title = title

@property
def get_title(self):
    return self._title

def set_author(self, author):
       self._author = author
  
@property
def get_author(self):
    return self.__author

class Book(Publication):
    def __init__(self, title, author, number_of_pages)
