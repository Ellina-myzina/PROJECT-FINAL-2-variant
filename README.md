README ДЛЯ 

«СИСТЕМА ОНЛАЙН-ЗАКАЗА ЕДЫ»

Описание

Данный проект представляет собой приложение, в котором пользователи могут просматривать меню, размещать заказы и отслеживать статус доставки. 
Код программы позволяет вводить данные пользователя, вводить пользователям блюда из меню и отслеживать статус своего заказа. Код состоит из следующих классов, в которых есть необходимые методы, которые выполняют определенный задачи:

Классы и методы

1.	Класс Menu
В этом классе хранится информация о блюде: категория блюда, название блюда, цена, вес и состав блюда:

![image](https://github.com/user-attachments/assets/fe51d36b-aa1c-48e0-a4cf-611475755366)


Методы класса Menu:

•	Метод __str__(self) позволяет получить строковое представление об информации блюда, включая его название:

![image](https://github.com/user-attachments/assets/897b4450-7292-40fe-b5bf-a24a48e73c38)

•	Метод add_menu(self, menu, dish) добавляет блюдо в список menu[]:

![image](https://github.com/user-attachments/assets/830650df-3bb2-47ee-ac44-11eb62c44701)

•	Метод print_menu(self, dish) выводит информацию о каждом блюде:

![image](https://github.com/user-attachments/assets/24593e6a-61ca-4bd1-8dd5-d00f149ece32)

2.	Класс Restaurant
Представляет ресторан с названием, меню и клиентом. Аргумент «клиент» является экземпляром класса Client, т.к. в классе Restaurant используется атрибут класса Client – «self.name», а также атрибуты «self.pay_order» и «self.status_order» для отображения статуса оплаты заказа и статуса заказа:

![image](https://github.com/user-attachments/assets/23f4ff94-127d-4994-b096-37da590b9c8f)

Методы класса Restaurant:

•	Метод pyment_order(self) выводит информацию о статусе оплаты заказа клиента, используя функцию sleep из модуля time для имитации отслеживания статуса оплаты:

![image](https://github.com/user-attachments/assets/9585bd36-885b-4d94-bae7-5b0c25d04fcf)

•	Метод accept_order(self) выводит информацию о статусе заказа клиента, используя функцию sleep из модуля time для имитации отслеживания статуса заказа:

![image](https://github.com/user-attachments/assets/84b0e584-fe8c-45b9-8056-ddb7116bb329)

3.	Класс Client
Содержит информацию о клиенте: имя, адрес доставки, а также список заказанных блюд клиентом:

![image](https://github.com/user-attachments/assets/a541d3cd-e30d-46a0-936c-47425e157fbb)

Методы класса Client:

•	Метод input_data(self) запрашивает у пользователя имя и адрес доставки:

![image](https://github.com/user-attachments/assets/567bf30d-1e54-424a-8df3-325179a81289)

•	Метод input_order(self) просит ввести пользователя блюда из меню и добавляет каждое блюдо в список:

![image](https://github.com/user-attachments/assets/4e0b2052-e921-41be-b8f1-d6573cda4f27)

4.	Класс Order
Хранит информацию о клиенте, заказе клиента и статусе доставки заказа:

![image](https://github.com/user-attachments/assets/801e8f1d-4857-4bf4-83b8-6bf257b17b6d)

Методы класса Order:

•	Метод __str__(self) позволяет получить строковое представление об имени клиента и адреса доставки:

![image](https://github.com/user-attachments/assets/b8f1415d-7987-47ad-bc08-dc323402368c)

•	Метод sum_order(self, menu) считает сумму заказа клиента и выводит информацию, что блюда нет в меню, если клиент ввел неправильное название блюда:

![image](https://github.com/user-attachments/assets/5900b2e4-df76-40e4-b613-d358052b02ae)

•	Метод print_order(self, menu) подробно выводит заказ клиента:

![image](https://github.com/user-attachments/assets/59d5e0df-108e-4b4e-a29e-fa81ed0d3d2d)

•	Метод delivery_order(self) выводит информацию о статусе доставки заказа клиента, используя функцию sleep из модуля time для имитации отслеживания статуса доставки заказа:

![image](https://github.com/user-attachments/assets/2f650a42-d94a-4c45-abad-e0c136451fbb)

Использование программы

1.	Запустите программу;
2.	Введите ваше имя и адрес доставки, когда будет предложено;
3.	Введите блюда из меню, вводя их названия. Чтобы завершить выбор, введите точку (.);
4.	После ввода данных клиента и блюд из меню, программа выведет информацию о вашем заказе, итоговой сумме, а также статус заказа, статусы оплаты и доставки заказа.

Пример работы программы:

![image](https://github.com/user-attachments/assets/a74d0a5b-d6bd-441f-83d6-10a27c7289c8)
![image](https://github.com/user-attachments/assets/868bcd2b-8ca5-41ca-b881-edbab15c410e)




