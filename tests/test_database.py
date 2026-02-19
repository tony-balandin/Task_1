import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_available_buns_returns_three_buns():
    db = Database()

    buns = db.available_buns()

    assert len(buns) == 3


@pytest.mark.parametrize(
    'index, expected_name, expected_price',
    [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300),
    ],
)
def test_buns_have_expected_data(index, expected_name, expected_price):
    db = Database()

    bun = db.available_buns()[index]

    assert bun.get_name() == expected_name
    assert bun.get_price() == expected_price


def test_available_ingredients_returns_six_ingredients():
    db = Database()

    ingredients = db.available_ingredients()

    assert len(ingredients) == 6


@pytest.mark.parametrize(
    'index, expected_type, expected_name, expected_price',
    [
        (0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
        (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
        (5, INGREDIENT_TYPE_FILLING, 'sausage', 300),
    ],
)
def test_ingredients_have_expected_data(index, expected_type, expected_name, expected_price):
    db = Database()

    ingredient = db.available_ingredients()[index]

    assert ingredient.get_type() == expected_type
    assert ingredient.get_name() == expected_name
    assert ingredient.get_price() == expected_price
