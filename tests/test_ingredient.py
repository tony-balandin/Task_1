import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    'ingredient_type, name, price',
    [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100.0),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 300.5),
    ],
)
def test_ingredient_getters_return_init_values(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
