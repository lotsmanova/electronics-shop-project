from src.item import Item


class Phone(Item):
    """Дочерний класс Item"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """Инициализация экземпляра класса"""
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    @property
    def number_of_sim(self):
        """
        Геттер для атрибута number_of_sim
        """
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, num_sim: int) -> int or ValueError:
        """
        Сеттер для атрибута number_of_sim
        """
        if type(num_sim) is int and num_sim > 0:
            self.__number_of_sim = num_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')


    def __repr__(self) -> str:
        """
        Магический метод для отладочного представления объекта
        """
        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.price}, {self.quantity}, {self.number_of_sim})"

