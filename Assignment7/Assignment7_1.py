class BookStore:
    NoOfBooks=0
    def __init__(self, nameValue, authorValue):
        self.Name=nameValue
        self.Author=authorValue
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
    
    def Display(self):
        print("{} by {} No of Books : {}".format(self.Name, self.Author, BookStore.NoOfBooks))

def main():
    print("Enter Book Name")
    name=input()
    print("Enter Author")
    author=input()
    Obj1=BookStore(name, author)
    Obj1.Display()

    print("Enter Book Name")
    name=input()
    print("Enter Author")
    author=input()
    Obj2=BookStore(name, author)
    Obj2.Display()

if __name__=="__main__":
    main()