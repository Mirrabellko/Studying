class Dish:
    def __init__(self, name: str, price: float, ingredients: list):
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients

    def info(self):
        print(f"Current dish: {self.__name} \n Consist of {self.__ingredients} \n Price: {self.__price}")

    def __str__(self):
        result = f"Dish:{self.__name}. Ingredients:"
        for i in self.__ingredients:
            result = result + i + ","
        result = result + f"Price: {self.__price}"
        return result


    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


class Worker:
    def __init__(self, name:str, position: str, work_orders: list, feedback: list):
        self.__name = name
        self.__position = position
        self.work_orders = work_orders
        self.__feedback = feedback

    def take_order(self, new_order):
        self.work_orders.append(new_order)

    def delivery_dish(self, dish: Dish):
        return f"Your order {dish.info()} is ready"

    def give_order_to_chef(self, new_order):
        return f"There is a new one order {new_order.info()}"

    def set_feedback(self, new_feedback: str):
        self.__feedback.append(new_feedback)

    def take_payment(self, order):
        return f"Your payment is {order.payment}"

    def __str__(self):
        result = f"Waitor: {self.__name}, position:{self.__position}. "
        result = result + "Work orders: "
        for i in self.work_orders:
            result = result + i + ","
        result = result + "Feedback: "
        for i in self.__feedback:
            result = result + i + ","
        return result


class Order:
    def __init__(self, dish_list: list, waitor: Worker, status: bool = False):
        self.dish_list = dish_list
        self.__waitor = waitor
        self.status = status

    def set_add_dish(self, dish: Dish):
        self.dish_list.append(dish)

    def set_payment(self):
        total = 0
        for dish in self.dish_list:
            total += dish.get_price()
        return total

    def set_status_ready(self):
        self.status = True

    def __str__(self):
        result = f"Order: "
        for i in self.dish_list:
            result = result + str(i) + ","
        return result

    def info(self):
        print(f" {self.__str__()} \n Need to pay: {self.set_payment()} \n {self.__waitor} \n Status:{self.status}")


class Customer:
    def __init__(self, name: str, current_order: Order = "Water"):
        self.name = name
        self.current_order = current_order

    def create_order(self, dish: Dish):
        self.current_order = dish
        return f"My order is {dish.info()}"

    def get_payment(self, summ: float):
        return f"{summ} was payed"

    def get_feedback(self, waitor: Worker):
        return f"This feedback is to {waitor}"

    def use_menu(self, menu: list):
        return "The menu was looked"

    def __str__(self):
        return f"Customer: {self.name}, ordered {self.current_order}"


if __name__ =="__main__":
    # Создание работников
    print("Waitors: ")
    waitor1 = Worker("Alex", "waitor", [], [])
    waitor2 = Worker("Igor", "waitor", [], [])
    print(waitor1)
    print(waitor2)

    # Создание меню
    print("Dishes: ")
    dish1 = Dish("Salad", 300, ["tomato", "olive oil", "cucumber"])
    dish2 = Dish("Soup", 200, ["potato", "onion", "carrot"])
    print(dish1)
    print(dish2)

    # Создание нового клиента

    customer1 = Customer("Lenny")
    customer2 = Customer("Olga")

    # Клиент создает новый заказ
    customer1.create_order(dish2)
    customer2.create_order(dish1)

    # Создание заказа
    order1 = Order([dish2], waitor1)
    order2 = Order([dish1], waitor2)
    order3 = Order([dish1, dish2], waitor2)
    print()

