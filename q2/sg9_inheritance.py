#Parent class
class Publication:
    def __init__(self, title, author):
        self.__self = self
        self.__author = author
    #Setter
    @title.setter #Makes functions look like attributes
    def set_title(self, title):
        self._title = title
    #Getter
    @property #Makes functions look like attributes
    def get_title(self):
        return self._title 
    #Setter
    @author.setter #Makes functions look like attributes
    def set_author(self, author):
           self._author = author
    #Getter
    @property #Makes functions look like attributes
    def get_author(self):
        return self._author
    
    def display_info(self):
        print("Title:", self._title)
        print("Author:", self._author)
    
#Child class
class Book(Publication):
        def __init__(self, title, author, pages):
            super().__init__(title,author)
            self.__pages = pages
    
    @pages.setter #Makes functions look like attributes
    def set_pages(self, pages):
        if pages <= 0:
            self.__pages = pages
        else:
            print("The number of pages can not be negative")
    
    @property #Makes functions look like attributes
    def get_pages(self):
        return self.__pages

#Child class
class Magazine(Publication):
    def __init__(self, title, author, issue_num):
        super().__init__(title,author)
    self.__issue_num = issue_num

    @issue_num.setter #Makes functions look like attributes
    def set_issue_num(self, issue_num):
     self.__issue_num = issue_num

    @property #Makes functions look like attributes
    def get_issue_num(self):
        return self.__issue_num #Returns the magazine's issue number

#Objects
p1 = Publication("Journal of Science", "Maria Santos")
b1 = Book("The Alchemist", "Paulo Coelho", 208)
m1 = Magazine("Smithsonian", "Smithsonian Institution", 1)

#Printing Info
#Display Publication Info
print("Publication:")
p1.display_info

#Display Book Info
print("Book:")
b1.display_info()
print("Number of pages:", b1.pages)

#Display Magazine Info
print("Magazine:")
m1.display_info()
print("Issue number:", m1.issue_num)
