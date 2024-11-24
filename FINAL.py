import time

class Menu:
    def __init__(self,category,name,price,weight,ingredients):
        self.category = category
        self.name = name
        self.price = price
        self.weight = weight
        self.ingredients = ingredients
    
    def __str__(self):
        return f"{self.category}: {self.name}({self.weight} г) - {self.price} руб."

    def add_menu(self,menu,dish):
        menu.append(dish)

    def print_menu(self,dish):
        print(dish)
        print(f"Состав блюда: {", ".join(map(str,self.ingredients))}\n")

class Restaurant:
    def __init__(self,title,menu,client):
        self.title = title
        self.menu = menu
        self.name = client.name
        self.pay_order = "Ожидание оплаты заказа"
        self.status_order = "успешно принят"

    def payment_order(self):
        print(f"Статус оплаты заказа, клиента {self.name}:\n")
        time.sleep(3)
        print(f"{self.pay_order}")
        self.pay_order = "Заказ оплачен"
        time.sleep(3)
        print(f"{self.pay_order}")
        self.pay_order = "Оплата получена"
        time.sleep(3)
        print(f"{self.pay_order}")
    
    def accept_order(self):
        print(f"Статус заказа клиента {self.name}:\n")
        time.sleep(3)
        print(f"Клиент {self.name}, ваш заказ {self.status_order}")
        self.status_order = "успешно оформлен"
        time.sleep(3)
        print(f"Клиент {self.name}, ваш заказ {self.status_order}")