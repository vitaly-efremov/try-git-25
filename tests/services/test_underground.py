import pytest

from services.underground import is_underground_exists


@pytest.mark.parametrize(
    'region_id, result',
    [
        (1, True),
        (10, False),
    ]
)
def test_is_underground_exists(region_id, result):
    # act & assert
    assert is_underground_exists(region_id) == result
