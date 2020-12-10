import pickle

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


def writemode(data):
    return open(data, "wb")


pickle.dump(d1, (writemode("bookXauthor.dat")))
pickle.dump(d2, (writemode("bookXpbdate.dat")))
pickle.dump(d3, (writemode("bookXavail.dat")))
pickle.dump(d4, (writemode("bookXcustloc.dat")))
