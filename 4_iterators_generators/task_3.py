class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = make_flat_list(list_of_list)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.cursor]
        return item


def make_flat_list(lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(make_flat_list(elem))
        else:
            result.append(elem)
    return result


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
