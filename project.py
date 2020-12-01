import datetime

d1 = {"red": "taylor swift", "attack on tale": "francis", "the life of ty": "boss philip"}  # author
d2 = {"red": "June 21,2001", "attack on dolomite": "November 28,2021",
      "the life of ty": "December 1,2001"}  # published date
d3 = {"red": 1, "attack on dolomite": 13, "the life of ty": 200}  # numbers of available books

print("\nWelcome To Library")
print("How can we help you? \n")
print("Pls. choose the following: display book details(display), add new book(add), change details(change)")
print("borrow book(borrow), return book(return), delete a book(delete) or exit program(quit) \n")

Datenow = datetime.date.today().strftime("%B-%d-%Y")


def main():
    while True:
        x = str(input("course of action: "))
        if x == "display":
            # input for the key
            i = str(input("Pls enter Book Title: "))
            # display output
            print(f"{i} by {d1[i]} is published in {d2[i]}, the book has {d3[i]} available")
        elif x == "add":
            print("Add new Booke")
            a = str(input("Book title: "))
            b = str(input("Book author: "))
            c = str(input("Published date(M/D/Y): "))
            d = int(input("how many books available?: "))
            e = {a: b}
            f = {a: c}
            g = {a: d}
            # add into dictionary
            d1.update(e)
            d2.update(f)
            d3.update(g)
            for key in e:
                print(f"{key} by {e[key]} is added to the library")
        elif x == "change":
            print("A for Author,D for Date,N for number of books")
            q = str(input("what would you like to change? "))
            if q == "A":
                c = str(input("Input the Book you want to change the author: "))
                # to check if input is in dictionary
                d1[c] = d1[c]
                # change the value of the specific key
                d1[c] = str(input("Book author: "))
                print("{} author is {}".format(c, d1[c]))
            elif q == "D":
                c = str(input("Input the Book you want to change the date: "))
                # to check if input is in dictionary
                d2[c] = d2[c]
                # change the value of the specific key
                d2[c] = str(input("New time: "))
                print("{} published date is {}".format(c, d2[c]))
            elif q == "N":
                c = str(input("Input the Book you want to change the numbers of available books: "))
                # to check if input is in dictionary
                d3[c] = d3[c]
                # change the value of the specific key
                d3[c] = int(input("Number of books: "))
                print("{} now has {} books available".format(c, d3[c]))
            else:
                print("Book not found pls. try again")
        elif x == "borrow":
            e = str(input("Input the book you want to borrow:"))
            d3[e] = d3[e]
            if d3[e] > 0:
                d3[e] -= 1
                print(f"{e} is borrowed at {Datenow}")
            else:
                print(f"No more {e} available")
        elif x == "return":
            e = str(input("Input the book you want to return:"))
            d3[e] = d3[e]
            d3[e] += 1
            print(f"{e} is returned at {Datenow}")
        elif x == "delete":
            print("Delete a book")
            d = str(input("Input the book you want to delete:"))
            # to check if input is in dictionary
            d1[d] = d1[d]
            # delete a key:value pair
            d1.pop(d)
            d2.pop(d)
            d3.pop(d)
            print("{} is deleted from the dictionary".format(d))
        elif x == "quit":
            print("Thank You!")
            # close the program
            exit()
        else:
            print("Pls. select the following course of action")


while True:
    try:
        main()
    except KeyError:
        print("Book not available pls try again")
