import pytest
from src.item import Item

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 10000


def test_apply_discount_rate(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def tes_name_1(item1):
    assert item1.name == 'Смартфон'


def test_name_2(item1):
    item1.name = 'Ноутбук'
    assert item1.name == 'Ноутбук'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.0') == 5


def test_repr(item1):
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    assert item1.__str__() == 'Смартфон'
