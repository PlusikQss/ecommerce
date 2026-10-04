from typing import Any, Dict, List, Optional


class Product:
    """Класс для описания товара в магазине."""

    name: str
    description: str
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
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для цены с проверкой на положительное значение.

        Если новое значение <= 0 — выводит сообщение и не устанавливает цену.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = new_price

    @classmethod
    def new_product(
        cls,
        product_data: Dict[str, Any],
        existing_products: Optional[List["Product"]] = None,
    ) -> "Product":
        """
        Создаёт новый товар из словаря.

        Если передан список существующих товаров, ищет дубликат по имени.
        При совпадении — складывает количество и выбирает большую цену.

        Параметры
        ---------
        product_data : Dict[str, Any]
            Словарь с ключами name, description, price, quantity.
        existing_products : Optional[List[Product]]
            Список уже существующих товаров для проверки дубликатов.

        Возвращает
        ----------
        Product
            Созданный или обновлённый товар.
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product._price = price
                    return product

        return cls(name, description, price, quantity)


class Category:
    """Класс для описания категории товаров."""

    name: str
    description: str

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
        self._products: List[Product] = []

        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.

        Увеличивает счётчик товаров на 1.

        Параметры
        ---------
        product : Product
            Товар для добавления.
        """
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает строку со всеми товарами категории.

        Формат каждой строки:
        "Название продукта, X руб. Остаток: X шт.\\n"
        """
        result = ""
        for product in self._products:
            result += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return result