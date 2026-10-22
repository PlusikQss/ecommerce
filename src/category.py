from typing import List

from src.product import Product


class Category:
    """Класс для описания категории товаров."""

    name: str
    description: str

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        """Инициализирует категорию."""
        self.name = name
        self.description = description
        self._products: List[Product] = []

        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только Product и его наследников"
            )
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории."""
        return "".join(f"{product}\n" for product in self._products)

    def average_price(self) -> float:
        """
        Считает средний ценник всех товаров категории.

        Если товаров нет — возвращает 0.
        """
        try:
            total = sum(product.price for product in self._products)
            return total / len(self._products)
        except ZeroDivisionError:
            return 0.0
