from typing import List
from product import Product

class ShoppingCart:

    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def is_empty(self) -> bool:
        return len(self.products) == 0

    def has_products(self) -> bool:
        return not self.is_empty()
