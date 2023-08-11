import pytest
import os
from src.item import Item
from src.phone import Phone

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def phone1():
    return Phone("Смартфон", 10000, 20, 1)


def test_calculate_total_price(item1):
    # TestCase#1 проверка вывода общей стоимости
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    # TestCase#2 проверка пересчета скидки
    item1.apply_discount()
    assert item1.price == 10000


def test_apply_discount_rate(item1):
    # TestCase#3 проверка замены значения скидки
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def tes_name_1(item1):
    # TestCase#4 проверка геттера name
    assert item1.name == 'Смартфон'


def test_name_2(item1):
    # TestCase#5 проверка сеттера name
    item1.name = 'Ноутбук'
    assert item1.name == 'Ноутбук'


def test_string_to_number():
    # TestCase#6 проверка статического метода
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.0') == 5


def test_repr(item1):
    # TestCase#7 проверка отладочного представления объекта
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    # TestCase#8 проверка строкового представления объекта
    assert item1.__str__() == 'Смартфон'


def test_add(item1, phone1):
    # TestCase#9 проверка магического метода сложения
    assert item1 + phone1 == 40


def test_instantiate_from_csv_file_not_found(capsys):
    with capsys.disabled():
        # path = os.path.join(os.path.abspath("../src/"), "items_test.csv")
        with capsys.disabled():
            print(Item.instantiate_from_csv('../src/item.csv'))


def test_instantiate_from_csv_instance_csv_error(capsys):
    with capsys.disabled():
        path = os.path.join(os.path.abspath("../src/"), "items_test.csv")
        with capsys.disabled():
            print(Item.instantiate_from_csv(path))