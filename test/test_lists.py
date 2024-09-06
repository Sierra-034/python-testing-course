import unittest

class TestLists(unittest.TestCase):
    def test_list(self):
        assert [1, 2, 3] == [1, 2, 3]
        self.assertEqual([1, 2, 3], [1, 2, 3])
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertIsNot([1, 2, 3], [1, 2, 3])
        self.assertCountEqual([2, 3, 1], [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
