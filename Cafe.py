class Dish:
    def __init__(self, name: str, price: float, ingredients: list):
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients

    def info(self):
        print(f"Current dish: {self.__name} \n Consist of {self.__ingredients} \n Price: {self.__price}")


class Worker:
    def __init__(self, name:str, position: str, work_orders: list, feedback: list):
        self.__name = name
        self.__position = position
        self.work_orders = work_orders
        self.__feedback = feedback

    def take_order(self, new_order):
        self.work_orders.append(new_order)

    def delivery_dish(self, dish: Dish):
        print(f"Your order {dish.info()} is ready")

    def give_order_to_chef(self, new_order):
        print(f"There is a new one order {new_order.info()}")

    def set_feedback(self, new_feedback: str):
        self.__feedback.append(new_feedback)

    def take_payment(self, order):
        print(f"Your payment is {order.payment}")


class Order:
    def __init__(self, dish_list: list, payment: float, waitor: Worker, status: bool = False):
        self.dish_list = dish_list
        self.payment = payment
        self.__waitor = waitor
        self.status = status

    def set_add_dish(self, dish: Dish):
        self.dish_list.append(dish)

    def set_payment(self):
        print(f"Customer need to pay {self.payment}")

    def set_status_ready(self):
        self.status = True

    def info(self):
        print(f"Order: {self.dish_list} \n Need to pay: {self.payment} \n Waitor: {self.__waitor} \n Status:{self.status}")


class Customer:
    def __init__(self, name: str, current_order: Order = "Water"):
        self.name = name
        self.current_order = current_order


    def create_order(self, dish: Dish):
        self.current_order = dish
        print(f"My order is {dish.info()}")

    def get_payment(self, summ: float):
        print(f"{summ} was payed")

    def get_feedback(self, waitor: Worker):
        print(f"This feedback is to {waitor}")

    def use_menu(self, menu: list):
        print("The menu was looked")


if __name__ =="__main__":
    # Создание работников
    waitor1 = Worker("Alex", "waitor", [], [])
    waitor2 = Worker("Igor", "waitor", [], [])

    # Создание меню
    dish1 = Dish("Salad", 300, ["tomato", "olive oil", "cucumber"])
    dish2 = Dish("Soup", 200, ["potato", "onion", "carrot"])

    # Создание нового клиента
    customer1 = Customer("Lenny")
    customer2 = Customer("Olga")

    # Клиент создает новый заказ
    customer1.create_order(dish2)
    customer2.create_order(dish1)

    # Создание заказа
    order1 = Order([dish2], 200, waitor1)
    order2 = Order([dish1], 300, waitor2)

    # Официант относит повару
    waitor1.give_order_to_chef(order1)
    waitor2.give_order_to_chef(order2)

    # Заказы готовы
    order1.set_status_ready()
    order2.set_status_ready()

    # Получаем оплату
    customer1.get_payment(order1.payment)
    customer2.get_payment(order2.payment)

