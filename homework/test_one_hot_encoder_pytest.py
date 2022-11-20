import pytest

from one_hot_encoder import fit_transform


def test_colors():
    actual = fit_transform('red', 'green', 'black', 'red', 'green')
    expected = [('red', [0, 0, 1]), ('green', [0, 1, 0]), ('black', [1, 0, 0]), ('red', [0, 0, 1]),
                ('green', [0, 1, 0])]
    assert actual == expected


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_philosophy():
    actual = fit_transform('I', 'think', 'therefore', 'I', 'am')
    expected = [('I', [0, 0, 0, 1]), ('think', [0, 0, 1, 0]), ('therefore', [0, 1, 0, 0]), ('I', [0, 0, 0, 1]),
                ('am', [1, 0, 0, 0])]
    assert actual == expected


def test_repeat():
    actual = fit_transform('test', 'test', 'test', 'test')
    expected = [('test', [1]), ('test', [1]), ('test', [1]), ('test', [1])]
    assert actual == expected
