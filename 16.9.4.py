class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def get_client(self):
        return f'{self.name} {self.surname}. {self.city}.'

r_1 = Client('Иван', 'Петров', 'Москва', 50)
r_2 = Client('Валерий', "Иванов", "Санкт-Питербург", 66)
r_3 = Client("Жанна", "Васильева", "Иванов", 22)
r_4 = Client("Анна", "Павлова", "Владивосток", 120)

rr = [r_1, r_2, r_3, r_4]
for client in rr:
    print(client.get_client())
