from os import getenv
import pytest
import ya_folder as yf
from dotenv import load_dotenv
load_dotenv()
ya_token = getenv("ya_token")

data = (
    ("NewFolder", ya_token, 201, 200),
    ("NewFolder1", ya_token, 201, 200),
)


@pytest.mark.parametrize('a, b, expected, expected2', data)
def test_ya_disk_make_folder_positive(a, b, expected, expected2):
    assert yf.make_folder(a, b) == expected
    assert yf.get_folder_info(a) == expected2


data = (
    ("NewFolder", ya_token, 409, 200),
    ("NewFolder2", "wrong token", 401, 404),
)


@pytest.mark.parametrize('a, b, expected, expected2', data)
def test_ya_disk_make_folder_negative(a, b, expected, expected2):
    assert yf.make_folder(a, b) == expected
    assert yf.get_folder_info(a) == expected2
