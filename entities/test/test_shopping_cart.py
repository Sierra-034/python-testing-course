import unittest

from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart


def is_available_to_skip():
    return False


def is_connected():
    return False


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
        self.assertTrue(self.shopping_cart_1.is_empty(),
                        'El carrito no está vacío')

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

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(
            Product(name='Camara', price=700, discount=70))
        self.shopping_cart_1.add_product(Product(name='PC', price=1000))
        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 2000)
        self.assertEqual(self.shopping_cart_1.total, 1_645.00)

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)

    @unittest.skip('La prueba no cumple con el definition of done.')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    # skipIf -> si evalua verdadero, se salta la prueba
    # skipUnless -> si evalua falso, se salta la prueba
    @unittest.skipUnless(is_connected(), 'No se cuentan con los requerimientos.')
    def test_skip_example_two(self):
        pass

    def test_code_product(self):
        self.assertRegex(self.smartphone.code,
                         self.smartphone.name, 'expresion no encontrada')


if __name__ == '__main__':
    unittest.main()
