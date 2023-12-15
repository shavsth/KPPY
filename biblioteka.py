import json

class Item:
    def __init__(self, title, creator, year):
        self.__title = title
        self.__creator = creator
        self.year = year

    @property
    def title(self):
        return self.__title
    @property
    def creator(self):
        return self.__creator
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, y):
        if type(y) != int:
            print(f"Nieprawidłowy format roku (year = {y})")
            self.__year = None
        else:
            self.__year = y

    def display_info(self):
        print(f"Title: {self.title}\nCreator: {self.creator}\nYear: {self.year}")

class Book(Item):
    def __init__(self, title, creator, year, genre, isbn):
        super().__init__(title, creator, year)
        self.__genre = genre
        self.isbn = isbn

    @property
    def genre(self):
        return self.__genre
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        isbn_clear = isbn.replace('-', '')
        if isbn_clear.isdigit() and len(isbn_clear) == 13:
            self.__isbn = isbn
        else:
            print(f"Nieprawidłowy format ISBN (isbn = {isbn})")
            self.__isbn = None

    def display_info(self):
        return super().display_info(), print(f"Genre: {self.genre}\nISBN: {self.isbn}\n")

class Movie(Item):
    def __init__(self, title, creator, year, genre, duration):
        super().__init__(title, creator, year)
        self.__genre = genre
        self.duration = duration

    @property
    def genre(self):
        return self.__genre
    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, duration):
        if type(duration) != int or duration < 0:
            print(f"Nieprawidłowy format długości (duration = {duration})")
            self.__duration = None
        else:
            self.__duration = duration

    def display_info(self):
        return super().display_info(), print(f"Genre: {self.genre}\nDuration: {self.duration} minutes\n")

class Library:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        if isinstance(item, (Book, Movie)) and all(getattr(item, attr) is not None for attr in item.__dict__.keys()):
            self.__items.append(item)
        else:
            print(f"Nieprawidłowy obiekt (title: {item.title}...).")

    def display_items(self):
        print()
        for item in self.__items: item.display_info()

    def save_to_file(self, filename):
        filename = filename if ".json" not in filename else filename.replace(".json","")
        with open(filename + ".json", "w") as file:
            lib_dict = {}
            i = 1
            for item in self.__items:         
                lib_dict.update({'Item' + str(i): item.__dict__})
                i+=1
            json_obj = json.dumps(lib_dict, indent=4)
            file.write(json_obj)

    def load_from_file(self, filename):
        filename = filename if ".json" not in filename else filename.replace(".json","")
        with open(filename + ".json", "r") as file:
            json_obj = json.load(file)
            for item in json_obj.values():
                args = list(item.values())
                if "_Movie__genre" in item:
                    self.add_item(Movie(args[0], args[1], args[2], args[3], args[4]))
                else:
                    self.add_item(Book(args[0], args[1], args[2], args[3], args[4]))
            
    def recommendation(self, item_user):
        print(f"\nPolecane filmy podobne do {item_user.title} to:") if isinstance(item_user, Movie) else print(f"\nPolecane książki podobne do {item_user.title} to:")
        i = 0
        for item_lib in self.__items:
            if item_lib.title != item_user.title and item_lib.genre == item_user.genre:
                item_lib.display_info()
                i+=1
        if i == 0:
            print("Niestety nie posiadamy takich przedmiotów w bibliotece.")

    # funkcja pomocnicza do recommendation_general
    def __search(self, item_type, genre):
        print("Polecane filmy to:") if item_type == Movie else print("Polecane książki to:")
        i = 0
        for item in self.__items:
            if item.genre == genre and isinstance(item, item_type):
                item.display_info()
                i+=1
        if i == 0:
            print("\nNiestety nie posiadamy takich przedmiotów w bibliotece.")

    # book_or_movie - nazwa klasy lub string z szukym typem rekomendacji
    def recommendation_general(self, book_or_movie, genre):
        if book_or_movie == Movie or book_or_movie == Book:
            self.__search(book_or_movie, genre)
        elif type(book_or_movie) == str and book_or_movie.upper() in ["KSIĄŻKA", "BOOK"]:
            self.__search(Book, genre)
        elif type(book_or_movie) == str and book_or_movie.upper() in ["FILM", "MOVIE"]:
            self.__search(Movie, genre)
        else:
            print(f"\nBrak obiektów typu {book_or_movie} w bibliotece.")


# ### testowe ###
            
bk = Book("Zbrodnia i Kara", "Fiodor Dostojewski", 1866, "Psychological Fiction", "838-7-13-138264-9")
bk.display_info()

# nieprawidłowy nr isbn:
bk_err = Book("Kara i Zbrodnia", "Fjodor Dostoiewski", 1866, "Psychological Fiction", "838-7-1:-13t264-9")

mv = Movie("2001: A Space Odyssey", "Stanley Kubrick", 1968, "Sci-Fi", 139)

# nieprawidłowe dane:
mv_err = Movie("3001: A Space Odyssey", "Stanlei Kubrick", 1968, "Sci-Fi", "139")
mv2_err = Movie("2077: Space Odyssey", "Stanley Cubrik", "dawno", "Sci-Fi", 139)
mv2_err.display_info() # podmiana na None

lib = Library()
print("\nDODANIE PRZEDMIOTÓW DO <lib>:")
lib.add_item(bk)
lib.add_item(bk_err)
lib.add_item(mv2_err)
lib.add_item(mv)
lib.add_item(Movie("Blade Runner 2049", "Denis Villeneuve", 2017, "Sci-Fi", 163))
lib.add_item(Movie("Whiplash", "Damien Chazelle", 2014, "Psychological Drama", 106))

print("\nPRZEDMIOTY W <lib>:")
lib.display_items()

print("\nREKOMENDACJE (TYP, GATUNEK):")
lib.recommendation_general("movie", "Sci-Fi")
lib.recommendation_general(Book, "Poetry")

print("\nREKOMENDACJE (PODOBNE DO):")
lib.recommendation(mv)

print("\nZAPIS DO PLIKU <test.json>")
lib.save_to_file("test.json")

print("\nWCZYTANIE DANYCH Z PLIKU <test.json> DO BIBLIOTEKI <lib2>:")
lib2 = Library()
lib2.load_from_file("test.json")
lib2.display_items()
