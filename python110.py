class Book:
    def __init__(self,tittle, auther,pages):
        self.tittle = tittle
        self.auther = auther
        self.pages = pages



    def __str__(self):
        return f" ' {self.tittle}' by {self.auther}"



    def __repr__(self):
        return f"Book(tittle ='{self.tittle}', auther='{self.auther}', pages={self.pages})"


    def __len__(self):
        return self.pages


b1 = Book("Python 100 days", "Code with harry" , 350)
print("print output:",b1)
print("Repr output:", repr(b1))
print("Total pages (len):",len(b1))

