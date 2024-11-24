class Client:
    def __init__(self):
        self.name = ""
        self.adress = ""
        self.list_order = []

    def input_data(self):
        self.name = input("Введите своё имя: ")
        self.adress = input("Укажите адресс доставки: ")

    def input_order(self):
        order = ""
        while order != ".":
            order = input(f"Клиент {self.name} введите блюдо из меню: ")
            self.list_order.append(order)
        del self.list_order[len(self.list_order)-1]

client = Client()

client.input_data()