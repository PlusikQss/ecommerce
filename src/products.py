from typing import Any, Dict, List, Optional


class Product:
    """Базовый класс для описания товара в магазине."""

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

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Сложение двух товаров — общая стоимость на складе.

        Складывать можно только товары одного класса.
        """
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя сложить Product с {type(other).__name__}")
        if type(self) is not type(other):
            raise TypeError(
                "Нельзя складывать товары разных классов: "
                f"{type(self).__name__} и {type(other).__name__}"
            )
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой на положительное значение."""
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
        """Создаёт новый товар из словаря."""
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


class Smartphone(Product):
    """Класс для описания смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализирует смартфон.

        Дополнительные параметры:
        efficiency — производительность,
        model — модель,
        memory — объём встроенной памяти,
        color — цвет.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для описания газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализирует газонную траву.

        Дополнительные параметры:
        country — страна-производитель,
        germination_period — срок прорастания,
        color — цвет.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
        """
        Добавляет товар в категорию.

        Принимает только объекты Product и его наследников.
        Иначе выбрасывает TypeError.
        """
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
