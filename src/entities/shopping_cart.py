from typing import List
from src.entities.product import Product


class ShoppingCart:

    def __init__(self) -> None:
        self.__products: List[Product] = []

    @property
    def products(self):
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def is_empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self) -> bool:
        return not self.is_empty()

    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)

    @property
    def total(self):
        return sum([
            (product.price - product.discount)
            for product in self.__products
        ])
