import datetime

d1 = {"Yakusoku no Neverland": "Kaiu Shirai", "The Little Prince": "Antoine de Saint-Exupéry", "Naruto":
      "Masashi Kishimoto", "KonoSuba": "Natsume Akatsuki", "Avengers": "Stan Lee", "Harry Potter":
      "J.K. Rowling", "Carrie": "Stephen King", "Gone with the Wind": "Margaret Mitchell",
      "Noli Me Tangere": "Dr. Jose Rizal", "El Filibusterismo": "Dr.Jose Rizal"}  # Author
d2 = {"Yakusoku no Neverland": "August 1, 2016", "The Little Prince": "April 6, 1943", "Naruto": "September 21, 1999",
      "KonoSuba": "September 9, 2014", "Avengers": "September 1963", "Harry Potter":
      "June 26, 1997 - July 21, 2007", "Carrie": "April 5,1974", "Gone with the Wind": "June 30, 1936",
      "Noli Me Tangere": "1887", "El Filibusterismo": "1891"}  # Published Date
d3 = {"Yakusoku no Neverland": 1, "The Little Prince": 10, "Naruto": 7, "KonoSuba": 1, "Avengers": 3,
      "Harry Potter": 7, "Carrie": 2, "Gone with the Wind": 3, "Noli Me Tangere": 6,
      "El Filibusterismo": 6}  # Numbers of Available Books
d4 = {"Yakusoku no Neverland": "Anime", "The Little Prince": "Children's Book", "Naruto": "Anime",
      "KonoSuba": "Anime", "Avengers": "Comics", "Harry Potter": "Fantasy Fiction", "Carrie":
      "Horror Fiction", "Gone with the Wind": "Romance", "Noli Me Tangere": "Novel", "El Filibusterismo": "Novel"}

print("\n\033[1mWelcome To Library\033[0m")
print("How can we help you? \n")
print("Please choose from the following commands below: ")
print("֎ DISPLAY Book details(display), \n֎ ADD New Book(add), \n֎ CHANGE Book details(change)")
print("֎ BORROW Book(borrow), \n֎ RETURN Book(return), \n֎ DELETE a Book(delete) ")
print("or EXIT program(quit) \n")

Datenow = datetime.date.today().strftime("%B-%d-%Y")


def repetition():
    return int(input("Please specify how many repetitions for this action: "))


def main():
    while True:
        x = str(input("Please input the course of action to do: "))
        if x == "display":
            q = int(input("how many: "))
            for _ in range(0, q):
                # input for the key
                i = str(input("Please specify the book title: "))
                # display output
                print(f"\033[1mBook Title:\033[0m ֎{i}֎ \n"
                      f"\033[1mBook Author:\033[0m © {d1[i]} \n"
                      f"\033[1mBook Publishing Date:\033[0m {d2[i]} \n"
                      f"\033[1mBook Location:\033[0m {d4[i]} Section \n"
                      f"\033[1mBook Cop(y/ies) Remaining:\033[0m {d3[i]} \n")
        elif x == "add":
            q = repetition()
            for _ in range(0, q):
                print("Add new Book. Please specify the necessary information on the queries to follow: ")
                a = str(input("Book title: "))
                b = str(input("Book author: "))
                c = str(input("Published date(MM/DD/YYYY): "))
                loc = str(input("In what shelf should the book be stored?: "))
                d = int(input("How many cop(y/ies) of this book will be available?: "))
                e = {a: b}
                f = {a: c}
                g = {a: d}
                h = {a: loc}
                # add into dictionary
                d1.update(e)
                d2.update(f)
                d3.update(g)
                d4.update(h)
                for key in e:
                    print(f"The book '{key}' by {e[key]} is now added to the library.")
        elif x == "change":
            q = repetition()
            print("Please enter 'B' for Book Title, 'A' for Author, 'D' for Date, "
                  "\n'S' for specifying the location, and 'N' for number of books.\n")
            for _ in range(0, q):
                q = str(input("What would you like to change? "))
                if q == "B":
                    c = str(input("Please specify the name of the book you want to change the title: "))
                    # to check if input is in dictionary
                    d1[c] = d1[c]
                    d = str(input("Please specify the new title of the book: "))
                    d1[d] = d1.pop(c)
                    d2[d] = d2.pop(c)
                    d3[d] = d3.pop(c)
                    d4[d] = d4.pop(c)
                    print(f"The name of the book '{c}' has been changed to '{d}'.")
                elif q == "A":
                    c = str(input("Please specify the Book you want to change the author: "))
                    # to check if input is in dictionary
                    d1[c] = d1[c]
                    # change the value of the specific key
                    d1[c] = str(input("Book author: "))
                    print("{} author is {}".format(c, d1[c]))
                elif q == "D":
                    c = str(input("Please specify the Book you want to change the date: "))
                    # to check if input is in dictionary
                    d2[c] = d2[c]
                    # change the value of the specific key
                    d2[c] = str(input("New time: "))
                    print("The book '{}' publishing date is changed to {}.".format(c, d2[c]))
                elif q == "N":
                    c = str(input("Please specify the Book you want to change the quantity of available books: "))
                    # to check if input is in dictionary
                    d3[c] = d3[c]
                    # change the value of the specific key
                    d3[c] = int(input("Number of books: "))
                    print("The book '{}' now has {} available cop(y/ies) in the library.".format(c, d3[c]))
                elif q == "S":
                    c = str(input("Please specify the book you want to change: "))
                    # to check if input is in dictionary
                    d4[c] = d4[c]
                    # input the location directly into the dictionary.
                    loc = str(input("Please specify the location of the book (e.g. Horror): "))
                    d4[c] = loc
                    print(f"The book '{c}' is now located at {loc} section.")
                else:
                    print("Book not found. Please try again!")
        elif x == "borrow":
            q = repetition()
            for _ in range(0, q):
                e = str(input("Input the book you want to borrow: "))
                d3[e] = d3[e]
                if d3[e] > 0:
                    d3[e] -= 1
                    print(f"The book '{e}' is borrowed at this library on {Datenow}.")
                else:
                    print(f"No more remaining cop(y/ies) for '{e}' book available.")
        elif x == "return":
            q = repetition()
            for _ in range(0, q):
                e = str(input("Please specify the book you want to return: "))
                d3[e] = d3[e]
                d3[e] += 1
                print(f"The book '{e}' has just been returned to this library on {Datenow}.")
        elif x == "delete":
            print("Delete a book")
            q = repetition()
            for _ in range(0, q):
                d = str(input("Input the book you want to delete: "))
                # to check if input is in dictionary
                d1[d] = d1[d]
                # delete a key:value pair
                d1.pop(d)
                d2.pop(d)
                d3.pop(d)
                print("The book '{}' is deleted from the library.".format(d))
        elif x == "quit":
            print("Thank You!")
            # close the program
            exit()
        else:
            print("Please select from course of actions above.")


while True:
    try:
        main()
    except KeyError:
        print("Book currently not available. Please try again!")
    except ValueError:
        print("Wrong input. Please check your inputs and retry.")
