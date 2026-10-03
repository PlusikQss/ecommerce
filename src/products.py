from typing import List


class Product:
    """Класс для описания товара."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """
        Инициализирует товар.

        Параметры
        ---------
        name : str
            Название товара.
        description : str
            Описание товара.
        price : float
            Цена товара.
        quantity : int
            Количество в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для описания категории товаров."""

    name: str
    description: str
    products: List[Product]

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        """
        Инициализирует категорию.

        Параметры
        ---------
        name : str
            Название категории.
        description : str
            Описание категории.
        products : List[Product]
            Список товаров категории.
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)
