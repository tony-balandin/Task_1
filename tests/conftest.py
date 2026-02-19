import pytest
from unittest.mock import Mock


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = 'test bun'
    bun.get_price.return_value = 50.0
    return bun


@pytest.fixture
def ingredient_mock():
    ingr = Mock()
    ingr.get_type.return_value = 'SAUCE'
    ingr.get_name.return_value = 'hot sauce'
    ingr.get_price.return_value = 10.0
    return ingr
