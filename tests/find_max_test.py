from unittest import TestCase
import find_max as f

class FindMaxTest(TestCase):
    def test_get_max(self):
        result = f.get_max(1, 70)
        self.assertEqual(result, 70)
    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        result = f.get_max_with_one_argument(123)
        self.assertEqual(result, 123)

    def test_get_max_with_many_arguments(self):
        result = f.get_max_with_many_arguments(1, 2, 3, 4)
        self.assertEqual(4, result)

    def test_get_max_with_one_or_more_arguments(self):
        first = 124
        array = [10000, 1421, 12]
        result = f.get_max_with_one_or_more_arguments(first, *array)
        self.assertEqual(10000, result)

    def test_get_max_bounded(self):
        kwargs = {
            'low': 0,
            'high': 127
        }
        result = f.get_max_bounded(-54, 45, 23, **kwargs)
        self.assertEqual(45, result)

    def test_make_max(self):
        bounded_min = f.make_max(low=0, high=255)
        self.assertEqual(True, callable(bounded_min))
        if callable(bounded_min):
            result = bounded_min(-5, 12, 13)
            self.assertEqual(13, result)
