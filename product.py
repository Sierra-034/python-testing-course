
class ProductDiscountError(Exception):
    pass

class Product:
    
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price

        if discount > price:
            raise ProductDiscountError('Descuento mayor que precio.')

        self.discount = discount
