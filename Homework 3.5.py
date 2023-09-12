"""Создать класс Man (человек), с полями: имя, возраст, пол и вес. Определить методы переназначения имени,
изменения возраста и изменения веса. Создать производный класс Student, имеющий поле года обучения.
Определить методы переназначения и увеличения года обучения."""
#1

class Man:
    def __init__(self, name: str, age: int, sex: bool, weight: int):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    def set_name(self, new_name: str):
        self.name = new_name
        return f"Name {self.name} was updated"

    def change_age(self, new_age: int):
        self.age = new_age
        return f"Age {self.age} was updated"

    def change_weight(self, new_weight):
        self.weight = new_weight
        return f"Weight {self.weight} was updated"

    def __str__(self):
        return f"Name:{self.name},\nAge:{self.age},\nSex:{self.sex},\nWeight:{self.weight}"


class Student(Man):
    def __init__(self, name: str, age: int, sex: bool, weight: int, study_year: int):
        super().__init__(name, age, sex, weight)
        self.study_year = study_year

    def change_year(self, new_year: int):
        self.study_year = new_year
        return f"Year {self.study_year} was updated"

    def encr_year(self, difference: int):
        self.study_year += difference
        return f"Year {self.study_year} was encreased"

    def __str__(self):
        base = super().__str__()
        return base + f"\nYear {self.study_year}"

student1 = Student("Oleg", 20, 1, 80, 2000)
print(student1)
student1.encr_year(5)
student1.change_weight(90)
student1.change_age(25)
print()
print(student1)
'''
Создать класс Triangle с полями-сторонами. Определить методы изменения сторон, вычисления углов, 
вычисления периметра. Создать производный класс RightAngled (прямоугольный), имеющий поле площади. 
Определить метод вычисления площади.
'''
#2
class Triangle:
    def __init__(self, one: float, two: float, three: float):
        self.one = one
        self.two = two
        self.three = three

    def set_one(self, new_one):
        self.one = new_one
        return f"One side was changed"

    def set_two(self, new_two):
        self.two = new_two
        return f"Two side was changed"

    def set_three(self, new_three):
        self.three = new_three
        return f"Three side was changed"

    def perimeter(self):
        result = self.one + self.two + self.three
        return result


class RightAngled(Triangle):
    def __init__(self, one, two, three, square):
        super().__init__(one, two, three)
        self.square = square

    def change_square(self):
        self.square = self.one * self.two * self.three
        return self.square

obj1 = RightAngled(15, 18, 20, 0)
print(obj1.change_square())
obj1.set_one(1)
obj1.set_two(2)
obj1.set_three(3)
print(obj1.change_square())

'''
Создайте класс Date для работы с датами в формате «год.месяц.день». Дата представляется тремя полями типа int: 
для года, месяца и дня. Класс должен включать конструктор, который принимает н вход строку «год.месяц.день». 
Обязательными операциями являются: вычисление даты через заданное количество дней, вычитание заданного количества 
дней из даты, присвоение и получение отдельных частей даты (день, месяц, год), сравнение дат (равно, до после), 
вычисление количества дней между датами.
'''
# 3
# первый элемент 0 для сохранения порядковых номеров месяцев
MONTHS_LIST = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    def __init__(self, date: str):
        date_list = date.split(".")
        self.year = int(date_list[0])
        self.month = int(date_list[1])
        self.day = int(date_list[2])

    def __str__(self):
        return f"{self.year}.{self.month}.{self.day}"

    def add_day(self, num_days: int):
        last_day = MONTHS_LIST[self.month]
        new_day = self.day + num_days
        while True:
            if new_day > last_day:
                new_day -= last_day
                self.month = self.month + 1
                if self.month > 12:
                    self.month -= 12
                    self.year += 1
                last_day = MONTHS_LIST[self.month]

            else:
                self.day = new_day
                return f"{self.year}.{self.month}.{self.day}"

    def sub_day(self, num_days: int):
        last_day = MONTHS_LIST[self.month]
        new_day = self.day - num_days
        while True:
            if new_day < 1:
                self.month -= 1
                if self.month < 1:
                    self.month += 12
                    self.year -= 1
                last_day = MONTHS_LIST[self.month]
                new_day = last_day + new_day
            else:
                self.day = new_day
                return f"{self.year}.{self.month}.{self.day}"

    def is_day_true(self, day: int, month: int):
        if MONTHS_LIST[month] >= day:
            self.day = day
            self.month = month
        else:
            return print(f"There are maximum {MONTHS_LIST[month]} days in this month")

    def set_day(self, new_day: int):
        if new_day > 0 and new_day <= 31:
            self.is_day_true(new_day, self.month)
        else:
            return print(f"There are maximum {MONTHS_LIST[self.month]} days in this month")


    def set_month(self, new_month: int):
        if new_month > 0 and new_month <= 12:
            self.is_day_true(self.day, new_month)
        else:
            return print(f"Error, there are 12 months")

    def set_year(self, new_year: int):
        if new_year > 0:
            self.year = new_year

    def show_day(self):
        return self.day

    def show_month(self):
        return self.month

    def show_year(self):
        return self.year


a = Date("1992.11.27")
print(a.year)
print(a.month)
print(a.day)

print(a.add_day(170))
print(a.year)
print(a.month)
print(a.day)

print(a.sub_day(358))
print(a.year)
print(a.month)
print(a.day)


a.set_day(20)
a.set_month(10)
print(a)
