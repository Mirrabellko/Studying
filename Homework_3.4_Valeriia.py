#1
'''
class Cook:
    def __init__(self, name: str, spec: str, position: str, salary: float):
        self.__name = name
        self.__spec = spec
        self.__position = position
        self.__salary = salary

    def get_position(self):
        return f"Specialisation: {self.__spec} \n Position: {self.__position}"

    def set_position(self, new_position):
        self.__position = new_position
        return "Position was updated"

    def set_spec(self, new_spec):
        self.__spec = new_spec
        return "Specialisation was updated"

    def set_new_salary(self, new_salary: float):
        self.__salary = new_salary

    def __eq__(self, other):
        res = False
        if self.__position == other.__position:
            res = True
        return res

    def __ne__(self, other):
        res = False
        if self.__position != other.__position:
            res = True
        return res

    def __str__(self):
        return f"Cook's name: {self.__name} \n Salary: {self.__salary}"

    def food_ready(self):
        return "Order is ready"

povar1 = Cook("Jack", "Japan food", "middle", 55000)
print(povar1)
print(povar1.get_position())
povar1.set_spec("European food")
povar1.set_position("junior")
print(povar1)
print(povar1.get_position())


# 2
#уровень официанта в следующей градации:
# 1-начинающий (может обслужить от 1 до 2 человек за столиком)
# 2-опытный (от 1 до 4)
# 3-специалист (от 1 до 6)
class Waiter:
    def __init__(self, name: str, lvl: int, salary: float):
        self.__name = name
        self.__lvl = lvl
        self.__salary = salary

    def set_lvl(self, new_lvl: int):
        self.__lvl = new_lvl
        return f"Level was updated"

    def set_salary(self, new_salary: float):
        self.__salary = new_salary
        return f"Salary was updated"

    def check_lvl(self, num_people: int):
        result = False
        if self.__lvl == 1 and num_people <= 2:
            result = True
        if self.__lvl == 2 and num_people <= 4:
            result = True
        if self.__lvl == 3 and num_people <= 6:
            result = True
        return result

    def service(self, num_table: int):
        return "The clients were served"

    def __str__(self):
        return f"Waiter: {self.__name} \n level: {self.__lvl} \n salary: {self.__salary}"

waiter1 = Waiter("Bob", 1, 45000)
print(waiter1)
waiter1.set_salary(50000)
waiter1.set_lvl(2)
print(waiter1.check_lvl(6))
print(waiter1.check_lvl(4))
print(waiter1)
print(waiter1.service(5))
'''
# 3
class Singer:
    def __init__(self, name: str, albumlist: list):
        self.__name = name
        self.albumlist = albumlist

    def add_album(self, new_album):
        self.albumlist.append(new_album)
        return "New album was added"

    def remove_album(self, album):
        for i in self.albumlist:
            if i == album:
                self.albumlist.remove(album)
        return "The album was deleted"

    def __str__(self):
        result = f"Singer:{self.__name}| Albums:"
        for i in self.albumlist:
            result = result + i + ","
        return result


class Track:
    def __init__(self, name:str, singer: Singer, genre: str, duration: int):
        self.__name = name
        self.__singer = singer
        self.__genre = genre
        self.__duration = duration

    def change_name(self, new_name):
        self.__name = new_name
        return "Name was chanched"

    def change_duration(self, new_dur):
        self.__duration = new_dur
        return "Duration was chanched"

    def change_genre(self, new_genre):
        self.__genre = new_genre
        return "Genre was changed"

    def change_singer(self, singer: Singer):
        self.__singer = singer
        return "Singer was changed"

    def __str__(self):
        result = f"Track:{self.__name}"
        return result


class Album:
    def __init__(self, name: str, tracklist: list, year: int, singer: Singer):
        self.__name = name
        self.tracklist = tracklist
        self.year = year
        self.singer = singer

    def add_track(self, new_track: Track):
        self.tracklist.append(new_track)
        return "New track was added"

    def remove_track(self, track: Track):
        for i in self.tracklist:
            if i == track:
                self.tracklist.remove(track)
        return "The track was deleted"

    def __str__(self):
        lst = []
        result = f"Album:{self.__name}\n Year:{self.year}\n {self.singer}\n"
        for i in self.tracklist:
            result = result + str(i) + ","
        return result


class MusicCollection:
    def __init__(self, tracklist: list, albumlist: list, singerlist: list):
        self.tracklist = tracklist
        self.albumlist = albumlist
        self.singerlist = singerlist

    def search_track(self, key_word: str):
        result = []
        for i in self.tracklist:
            if i.__name == key_word:
                result.append(i)
        return result

    def search_album(self, key_word: str):
        result = []
        for i in self.albumlist:
            if i.__name == key_word:
                result.append(i)
        return result

    def search_singer(self, key_word: str):
        result = []
        for i in self.singerlist:
            if i.__name == key_word:
                result.append(i)
        return result

    def add_track(self, new_track: Track):
        self.tracklist.append(new_track)
        return "New track was added"

    def remove_track(self, track: Track):
        for i in self.tracklist:
            if i == track:
                self.tracklist.remove(track)
        return "The track was deleted"

    def add_album(self, new_album: Album):
        self.albumlist.append(new_album)
        return "New album was added"

    def remove_album(self, album: Album):
        for i in self.albumlist:
            if i == album:
                self.albumlist.remove(album)
        return "The album was deleted"

    def add_singer(self, new_singer: Singer):
        self.singerlist.append(new_singer)
        return "New singer was added"

    def remove_singer(self, singer: Singer):
        for i in self.singerlist:
            if i == singer:
                self.singerlist.remove(singer)
        return "The singer was deleted"

# Создание певца
singer1 = Singer("Jojo", ["Lilian", "Bobby"])
print(singer1)
singer1.add_album("Vicky")
print(singer1)
singer1.remove_album("Bobby")
print(singer1)

# Создание альбома
album1 = Album("First", [], 2001, singer1)
print(album1)

# Создание треков
track1 = Track("Roses", singer1, "pop", 360)
track2 = Track("Blue", singer1, "pop", 380)
print(track1)
print()

# Добавим треки в альбом
album1.add_track(track1)
album1.add_track(track2)
print(album1)
