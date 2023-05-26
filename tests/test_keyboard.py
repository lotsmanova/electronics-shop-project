import pytest
from src.keyboard import KeyBoard, Language

@pytest.fixture
def keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_init(keyboard):
    # TestCase#1 проверка инициализации
    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == 'EN'


def test_change_lang(keyboard):
    # TestCase#2 проверка смены языка раскладки
    keyboard.change_lang()
    assert str(keyboard.language) == 'RU'
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == 'RU'
