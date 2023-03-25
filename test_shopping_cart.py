import unittest

from product import Product, ProductDiscountError
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
    
    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_product(product)
        self.assertIn(product, self.shopping_cart_2.products)

    def test_product_notin_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.0, discount=11.0)

if __name__ == '__main__':
    unittest.main()
