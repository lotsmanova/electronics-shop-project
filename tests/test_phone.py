import pytest
from src.phone import Phone

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120000, 20, 1)

def test_init(phone1):
    # TestCase#1 проверка инициализации
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 20
    assert phone1.number_of_sim == 1


def test_number_of_sim(phone1):
    # TestCase#2 проверка сеттера
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2


def test_repr(phone1):
    # TestCase#3 проверка отладочного представления объекта
    assert repr(phone1) == "Phone('iPhone 14', 120000, 20, 1)"


def test_add(phone1):
    # TestCase#4 проверка магического метода сложения
    assert phone1 + phone1 == 40
