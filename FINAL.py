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

class Order:
    def __init__(self,client):
        self.name = client.name
        self.adress = client.adress
        self.list_order = client.list_order
        self.deliv_order = "Собран"
        
    def __str__(self):
        return f"{self.name}"
        return f"{self.adress}"
        
    def sum_order(self,menu):
        s = 0
        for o_item in self.list_order:
            for m_item in menu:
                if o_item == m_item.name:
                    s += m_item.price
                    break
            else:
                print(f"\nБлюда {o_item} нет в меню!")
        return f"Итоговая сумма заказа: {s} руб."
        
    def print_order(self,menu):
        print(f"Заказ клиента {self.name}:\n")
        for o_item in self.list_order:
            for m_item in menu:
                if o_item == m_item.name:
                    print(f"{o_item} - {m_item.price} руб.")
        print(f"\n{self.sum_order(menu)}")

    def delivery_order(self):
        print(f"Статус доставки заказа клиента {self.name} по адресу {self.adress}:\n")
        time.sleep(3)
        print(f"{self.deliv_order}")
        self.deliv_order = "В пути"
        time.sleep(3)
        print(f"{self.deliv_order}")
        self.deliv_order = "Доставлен"
        time.sleep(3)
        print(f"{self.deliv_order}")