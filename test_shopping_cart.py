import unittest

from product import Product
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)

        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

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

    def test_shopping_cart_is_empty(self):
        self.assertTrue(self.shopping_cart_1.is_empty(), 'El carrito no está vacío')

    def test_shopping_cart_has_products(self):
        self.assertFalse(self.shopping_cart_2.is_empty())
        self.assertTrue(self.shopping_cart_2.has_products())


if __name__ == '__main__':
    unittest.main()
