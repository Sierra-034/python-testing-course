import unittest

from product import Product

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.some_value = 'samuel'   # This can be used as self.some_value
        print('>>> setUpClass se ejecuta antes de todo')

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)

    def tearDown(self):
        pass

    def test_product_object(self):
        name = 'manzana'
        price = 1.70

        product = Product(name, price)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)


if __name__ == '__main__':
    unittest.main()
