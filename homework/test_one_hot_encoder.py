import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_colors(self):
        actual = fit_transform('red', 'green', 'black', 'red', 'green')
        expected = [('red', [0, 0, 1]), ('green', [0, 1, 0]), ('black', [1, 0, 0]), ('red', [0, 0, 1]),
                    ('green', [0, 1, 0])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_philosophy(self):
        actual = fit_transform('I', 'think', 'therefore', 'I', 'am')
        expected = [('I', [0, 0, 0, 1]), ('think', [0, 0, 1, 0]), ('therefore', [0, 1, 0, 0]), ('I', [0, 0, 0, 1]),
                    ('am', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_repeat(self):
        actual = fit_transform('test', 'test', 'test', 'test')
        expected = [('test', [1]), ('test', [1]), ('test', [1]), ('test', [1])]
        self.assertEqual(actual, expected)
