import csv
import os
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)


    def __repr__(self) -> str:
        """Магический метод для отладочного представления объекта"""
        return f"{self.__class__.__name__}('{self.__name}', " \
               f"{self.price}, {self.quantity})"


    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return f"{self.__name}"


    @property
    def name(self):
        """
        Геттер для атрибута name
        """
        return self.__name


    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер для атрибута name
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls) -> 'Item':
        """Класс-метод, инициализирующий экземпляры класса"""
        PATH_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        PATH_CSV = os.path.join(PATH_DIR, 'src', 'items.csv')

        with open(PATH_CSV, newline='', encoding='1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])


    @staticmethod
    def string_to_number(num: str) -> int:
        """Статический метод, возвращающий число из числа строки"""
        return int(float(num))


    def __add__(self, other: int) -> int or ValueError:
        """Магический метод для сложения
        количества товара"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от него')
        return self.quantity + other.quantity
