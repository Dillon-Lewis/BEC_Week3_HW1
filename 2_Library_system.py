#Task 1

# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

#1. Add a new book to the files
    #.append
    #

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def main():
    while True:
        main = input('''
Book List

1. Add a book
2. View book list
3. Quit
''')
        if main == '1':
            add()  # Add a book
        elif main == '2':
            number = 1               
            for i in library:                    
                    print(f'Book {number}:', i[0], "by", i[1], )    
                    number += 1   # View list
        elif main == '3':
             break
        else:
            print('enter correct number')
            continue

def add():
        T1 = input("What is the Title of the book?\n").title()      
        for title, author in library:
             if T1 in title:
                  print("Provide a book we dont already have!")
                  return
             
        A1 = input('Who is the author of the book?\n') 
        new_book = (T1, A1)
        library.append(new_book)

        
                              
main()