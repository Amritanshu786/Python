class bookx:
    def __init__(self,pages):
        self.pages - pages
    def __add__(self,other):
        return self.pages + other.pages
    def __gt__(self,other):
        return self.pages>other.pages


class booky:
    def __init__(self,pages):
        self.pages = pages


b1= bookx(100)
b2 = booky(200)
print("Total number of pages ", b1+b2)
