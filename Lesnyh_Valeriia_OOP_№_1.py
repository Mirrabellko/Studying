
#1
class Animal:
    def __init__(self, name: str, kind: str, age: float, sound: str) -> None:
        self.name = name
        self.kind = kind
        self.age = age
        self.sound = sound

    def get_info(self):
        print(f"Name: {self.name} \n Kind: {self.kind} \n Age: {self.age}")
        print("---" * 5)

    def get_sound(self):
        print(f"{self.kind} makes a sound: {self.sound}")
        print("---" * 5)


cat = Animal("Jonh", "cat", 5, "meow")
dog = Animal("Bobby", "dog", 2, "woof-woof")
horse = Animal("Sion", "horse", 4, "neigh-neigh")

cat.get_info()
cat.get_sound()
dog.get_info()
dog.get_sound()
horse.get_info()
horse.get_sound()

#2
class Book:
    def __init__(self, name: str, author: str, num_pages: int) -> None:
        self.name = name
        self.author = author
        self.num_pages = num_pages

    def info(self):
        print(f"Name: {self.name} \n Author: {self.author} \n Pages: {self.num_pages}")

    def open_page(self, page: int):
        if page <= self.num_pages:
            print("This page was open")
        else:
            print("This page isn't found")
        print()


book1 = Book("Harry Potter", "Joanne Rowling", 200)
book2 = Book("Discworld", "Terry Pratchett", 400)
book3 = Book("Sherlock Holmes", "Arthur Conan Doyle", 300)

book1.info()
book1.open_page(201)
book2.info()
book2.open_page(100)
book3.info()
book3.open_page(200)

#3
class PassengerPlane:
    def __init__(self, brand: str, model: str, capacity: int, cur_height: float, cur_speed: float) -> None:
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.cur_height = cur_height
        self.cur_speed = cur_speed

    def info(self):
        print(f"Information about current aircraft")
        print(f"Brand: {self.brand} \n Model: {self.model} \n Capacity: {self.capacity} \n Current height: {self.cur_height} \n Current speed: {self.cur_speed}")
        print()

    def starting(self, height: float, speed: float):
        if self.cur_height == 0 and self.cur_speed == 0:
            self.cur_height = height
            print(f"{self.brand}{self.model} took off")
        else:
            print(f"Error!{self.brand}{self.model} isn't on the ground!")
        print()

    def landing(self):
        height = 0
        if self.cur_height != height:
            self.cur_height = height
            self.cur_speed = 0
        print(f"{self.brand}{self.model} was landed")
        print()

    def change_height(self, new_height: float) -> None:
        self.cur_height = new_height

    def change_speed(self, new_speed: float) -> None:
        self.cur_speed = new_speed


aircraft1 = PassengerPlane("Boeing", "Airbus A300", 300, 100, 210)
aircraft2 = PassengerPlane("Boeing", "757-200", 235, 0, 0)
aircraft3 = PassengerPlane("NPK IRKUT", "Sukhoi Superjet 100", 108, 200, 150)

aircraft1.info()
aircraft1.landing()
aircraft1.info()

aircraft2.info()
aircraft2.starting(170, 180)
aircraft2.change_speed(200)
aircraft2.info()

aircraft3.info()
aircraft3.change_height(300)
aircraft3.change_speed(300)
aircraft3.info()



class MusicAlbum:
    def __init__(self, singer_name: str, album_name: str, genre: str, tracklist: list):
        self.singer_name = singer_name
        self.album_name = album_name
        self.genre = genre
        self.tracklist = tracklist

    def add_track(self, new_track: str):
        if new_track not in self.tracklist:
            self.tracklist.append(new_track)
            print(f"{new_track} was added to album")
            print()

    def remove_track(self, track: str):
        if track in self.tracklist:
            self.tracklist.remove(track)
            print(f"{track} was removed from album")
            print()

    def play_track(self, track: str):
        if track in self.tracklist:
            print(f"{track} is playing")
            print()

    def info(self):
        print(f"Singer: {self.singer_name} \n Album: {self.album_name}, \n Genre:{self.genre} \n Track: ", end="")
        for i in self.tracklist:
            print(i, end=", ")
        print()


album1 = MusicAlbum("Rolling_Stones", "Let It Bleed", "rock", ["track1", "track2", "track3"])
album2 = MusicAlbum("Queen", "A Kind of Magic", "rock", ["track4", "track5"])
album3 = MusicAlbum("Skillet", "Comatose", "rock", ["track6"])

album1.info()
album1.remove_track("track1")
album1.play_track("track2")
album1.info()

album2.info()
album2.play_track("track4")
album2.add_track("track7")
album2.info()

album3.info()
album3.add_track("track8")
album3.add_track("track9")
album3.info()

class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        if den == 0:
            raise Exception("This number can't be used as denominator")
        else:
            self.den = den


    def __add__(self, other):
        summa_num = 0
        total_den = 0
        if self.den == other.den:
            summa_num = self.num + other.num
            total_den = self.den
        else:
            total_den = self.den * other.den
            summa_num = self.num * other.den + other.num * self.den
        return Fraction(summa_num, total_den)

    def __sub__(self, other):
        sub_num = 0
        total_den = 0
        if self.den == other.den:
            sub_num = self.num - other.num
            total_den = self.den
        else:
            total_den = self.den * other.den
            sub_num = self.num * other.den - other.num * self.den
        return Fraction(sub_num, total_den)

    def __mul__(self, other):
        mul_num = 0
        mul_den = 0
        mul_num = self.num * other.num
        mul_den = self.den * other.den
        return Fraction(mul_num, mul_den)

    def __truediv__(self, other):
        div_num = 0
        div_den = 0
        div_num = self.num * other.den
        div_den = self.den * other.num
        return Fraction(div_num, div_den)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __eq__(self, other):
        isEq = False
        if self.den == other.den and self.num == other.num:
            isEq = True
        return isEq

    def __ne__(self, other):
        NotEq = False
        if self.den != other.den:
            if self.num * other.den != other.num * self.den:
                NotEq = True
        else:
            if self.num != other.num:
                NotEq = True
        return NotEq

    def __lt__(self, other):
        Less = False
        if self.den != other.den:
            if self.num * other.den < other.num * self.den:
                Less = True
        else:
            if self.num < other.num:
                Less = True
        return Less

    def __le__(self, other):
        LessEq = False
        if self.den != other.den:
            if self.num * other.den <= other.num * self.den:
                LessEq = True
        else:
            if self.num <= other.num:
                LessEq = True
        return LessEq

    def __gt__(self, other):
        Gr = False
        if self.den != other.den:
            if self.num * other.den > other.num * self.den:
                Gr = True
        else:
            if self.num > other.num:
                Gr = True
        return Gr

    def __ge__(self, other):
        GrEq = False
        if self.den != other.den:
            if self.num * other.den >= other.num * self.den:
                GrEq = True
        else:
            if self.num >= other.num:
                GrEq = True


num1 = Fraction(3, 4)
num2 = Fraction(5, 6)
num3 = Fraction(1, 3)
num4 = Fraction(3, 5)

print(num1)
print(num1 + num3)
print(num2 - num3)
print(num2 > num3)
print(num4 != num1)
