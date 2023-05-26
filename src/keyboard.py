from src.item import Item

class Language:
    def __init__(self):
        """Инициализация"""
        self.__language = 'EN'


    @property
    def language(self):
        """
        Геттер для атрибута language
        """
        return self.__language


    def change_lang(self):
        """
        Метод для изменения языка раскладки
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class KeyBoard(Item, Language):
    """
    Класс для товара "клавиатура"
    """
    def __init__(self, name: str, price: float, quantity: int, language='EN') -> None:
        """Инициализация экземпляра класса"""
        super().__init__(name, price, quantity)
