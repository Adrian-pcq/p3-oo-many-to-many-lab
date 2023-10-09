class Author:
    
    
    def __init__(self,name):
        self.name = name
        self.contracts_list = []
    
    def contracts(self):
        return self.contracts_list
    
    def books(self):
        books_list = []
        for contract in self.contracts_list:
            books_list.append(contract.book)
        return books_list 

    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        list_royalties = []
        for contract in self.contracts_list:
           list_royalties.append(contract.royalties)
        total = sum(list_royalties)
        return total




class Book:

    all = []
    author_list = []

    def __init__(self,title):
        self.title = title
        self.contracts_list = []
        self.all.append(self)

    def books(self):
        return self.all
    
    def contracts(self):
        return self.contracts_list

    def authors(self):
        for contract in self.contracts_list:
           self.author_list.append(contract.author)
        return self.author_list    




class Contract:

    all=[]

    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception("author must to be an instance of Author!")
        
        if isinstance(book,Book):
            self.book = book
        else:
            raise Exception("book must to be an istance of Book!")
        
        if type(date)==str:
            self.date = date
        else:
            raise Exception("Try again!")
        
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception("Try again!")
        self.all.append(self)  
        author.contracts_list.append(self)
        book.contracts_list.append(self)
              
    @classmethod
    def contracts_by_date(cls,date):
        contracts = []
        for contract in cls.all:
            if contract.date == date:
                contracts.append(contract)   
        return contracts        
                 