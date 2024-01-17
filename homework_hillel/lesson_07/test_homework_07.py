from homework_07 import list_sorted_up
from homework_07 import list_sorted_down
from homework_07 import list_sorted_words


def test_list_sorted_up():
    assert list_sorted_up([5, 4, -6, 9, 0, 5, 4, 98, 12]) == [-6, 0, 4, 4, 5, 5, 9, 12, 98]


def test_list_sorted_down():
    assert list_sorted_down([9, 65, 74, 101, 13, 7, 86, 65]) == [101, 86, 74, 65, 65, 13, 9, 7]


def test_list_sorted_words():
    assert (list_sorted_words(['BMW', 'Renault', 'Mercedes', 'Suzuki', 'Volvo', 'Tesla'])
            == ['BMW', 'Volvo', 'Tesla', 'Suzuki', 'Renault', 'Mercedes'])
