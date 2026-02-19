import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    'name, price',
    [
        ('black bun', 100.0),
        ('white bun', 200.5),
    ],
)
def test_bun_getters_return_init_values(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price
