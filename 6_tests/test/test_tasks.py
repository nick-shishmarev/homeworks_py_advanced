import pytest
import task1
import task2
import task3


def generate_data(data):
    for item in data:
        yield item


data = (
    (1, 8, 15, [-3.0, -5.0]),
    (1, -13, 12, [12.0, 1.0]),
    (-4, 28, -49, [3.5]),
    (1, 1, 1, [None]),
)


@pytest.mark.parametrize('a, b, c, expected', generate_data(data))
def test_task1(a, b, c, expected):
    assert task1.solution(a, b, c) == expected


data = (
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Аристарх Павлов"),
    ("10006", "Аристарх Павлов"),
    ("5455 028765", "Василий Иванов"),
    ("536253", "Документ не найден"),
)


@pytest.mark.parametrize('a, expected', generate_data(data))
def test_task2_get_name(a, expected):
    assert task2.get_name(a) == expected


data = (
    ("2207 876234", "1"),
    ("11-2", "1"),
    ("10006", "2"),
    ("5455 028765", "1"),
    ("536253", "Полки с таким документом не найдено"),
)


@pytest.mark.parametrize('a, expected', generate_data(data))
def test_task2_get_directory(a, expected):
    assert task2.get_directory(a) == expected


data = (
    ("passport", "5492 837462", "Павел Романов", "3"),
    ("driver license", "1542 548792", "Иван Смирнов", "2"),
)


@pytest.mark.parametrize('a, b, c, d', generate_data(data))
def test_task2_add(a, b, c, d):
    task2.add(a, b, c, d)
    assert task2.get_directory(b) == d
    assert task2.get_name(b) == c


data = (
    ([1, 1, 1, 2, 3], 1),
    ([1, 2, 3, 2, 2], 2),
    ([1, 2, 3, 5, 2, 5, 5, 5, 3], 5),
)


@pytest.mark.parametrize('a, expected', generate_data(data))
def test_task3_vote(a, expected):
    task3.vote(a)
    assert task3.vote(a) == expected
