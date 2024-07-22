
import pytest
from src.forma_fun.forma_func import list_remove, list_append, list_empty


@pytest.mark.parametrize("grocery_list, grocery, expected", [
    ([], "poMme", ["Pomme"]),
    (["Pomme"], "Pomme", ["Pomme"]),
    ([], "Pomme Poire", ["Pomme", "Poire"]),
    ([], "1pomme", []),
    (None, "Pomme", ["Pomme"]),
    ([], None, []),
    (None, None, None)
])
def test_list_append(grocery_list, grocery, expected):
    assert list_append(grocery_list, grocery) == expected

@pytest.mark.parametrize("grocery_list, grocery, expected", [
    ([], "Pomme", []),
    (["Pomme", "Poire"], "pomme", ["Poire"]),
    (["Pomme", "Poire"], "Pomme poire", []),
    (None, "Pomme", None),
    ([], None, []),
    (None, None, None)
])
def test_list_remove(grocery_list, grocery, expected):
    list_remove(grocery_list, grocery)
    assert grocery_list == expected


@pytest.mark.parametrize("grocery_list, expected", [
    (["Pomme", "Poire"], []),
    ([], []),
    (None, None)
])
def test_list_empty(grocery_list, expected):
    list_empty(grocery_list)
    assert grocery_list == expected
