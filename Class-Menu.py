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

dish_1 = Menu("Пицца", "Пицца Маргарита" , 300, 400, ["Соус-пицца", "Колбаса","Маслины","Помидоры","Моцарелла","Приправы"])
dish_2 = Menu("Пицца", "4 сыра" , 200, 350, ["Соус-пицца", "Моцарелла","Пармезан","Горгонзола","Эмменталь","Приправы"])
dish_3 = Menu("Пицца", "Пицца Пепперонни" , 250, 450, ["Соус-пицца", "Пепперони","Моцарелла","Приправы"])
dish_4 = Menu("Картофель", "Картошка фри" ,80, 100,["Картофель","Соль","Приправы"])
dish_5 = Menu("Напиток", "Кока-кола" ,150, 500, ["Вода","Сироп-кола"])
dish_6 = Menu("Соус", "Чесночный соус" ,50, 25, ["Сметана","Чеснок"])

menu = []

for i in [dish_1,dish_2,dish_3,dish_4,dish_5,dish_6]:
    i.add_menu(menu,i)