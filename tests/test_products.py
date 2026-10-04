import pytest

from src.products import Category, Product


class TestProduct:

    def test_product_init(self) -> None:
        """Проверяет корректность инициализации Product."""
        product = Product("Test", "Описание", 100.50, 5)
        assert product.name == "Test"
        assert product.description == "Описание"
        assert product.price == 100.50
        assert product.quantity == 5

    def test_price_getter(self) -> None:
        """Геттер цены возвращает значение."""
        product = Product("Test", "Описание", 100.50, 5)
        assert product.price == 100.50

    def test_price_setter_valid(self) -> None:
        """Сеттер с положительной ценой обновляет значение."""
        product = Product("Test", "Описание", 100.50, 5)
        product.price = 200.0
        assert product.price == 200.0

    def test_price_setter_zero(self, capsys: pytest.CaptureFixture) -> None:
        """Сеттер с нулевой ценой не устанавливает значение."""
        product = Product("Test", "Описание", 100.50, 5)
        product.price = 0
        assert product.price == 100.50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_negative(self, capsys: pytest.CaptureFixture) -> None:
        """Сеттер с отрицательной ценой не устанавливает значение."""
        product = Product("Test", "Описание", 100.50, 5)
        product.price = -10
        assert product.price == 100.50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_new_product(self) -> None:
        """Класс-метод создаёт товар из словаря."""
        data = {
            "name": "New",
            "description": "Описание",
            "price": 500.0,
            "quantity": 10,
        }
        product = Product.new_product(data)
        assert product.name == "New"
        assert product.price == 500.0
        assert product.quantity == 10

    def test_new_product_duplicate_higher_price(self) -> None:
        """Дубликат: количество суммируется, цена берётся выше."""
        existing = [Product("Test", "Описание", 100.0, 5)]
        data = {
            "name": "Test",
            "description": "Описание",
            "price": 150.0,
            "quantity": 10,
        }
        product = Product.new_product(data, existing)
        assert product is existing[0]
        assert product.quantity == 15
        assert product.price == 150.0

    def test_new_product_duplicate_lower_price(self) -> None:
        """Дубликат с меньшей ценой: старая цена сохраняется."""
        existing = [Product("Test", "Описание", 200.0, 5)]
        data = {
            "name": "Test",
            "description": "Описание",
            "price": 150.0,
            "quantity": 10,
        }
        product = Product.new_product(data, existing)
        assert product.quantity == 15
        assert product.price == 200.0

    def test_new_product_without_duplicates(self) -> None:
        """Нет дубликатов — создаётся новый товар."""
        existing = [Product("Other", "Описание", 100.0, 5)]
        data = {
            "name": "New",
            "description": "Описание",
            "price": 500.0,
            "quantity": 10,
        }
        product = Product.new_product(data, existing)
        assert product.name == "New"
        assert product.quantity == 10
        assert len(existing) == 1

    @pytest.mark.parametrize(
        "name, description, price, quantity",
        [
            ("Товар 1", "Описание 1", 10.0, 1),
            ("Товар 2", "Описание 2", 99999.99, 100),
            ("Товар 3", "Описание 3", 0.01, 0),
        ],
    )
    def test_product_parametrized(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        product = Product(name, description, price, quantity)
        assert product.name == name
        assert product.price == price
        assert product.quantity == quantity


class TestCategory:

    def setup_method(self) -> None:
        """Сбрасывает счётчики перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_init(self, product_samsung: Product) -> None:
        """Проверяет корректность инициализации Category."""
        category = Category("Смартфоны", "Мобильные телефоны", [product_samsung])
        assert category.name == "Смартфоны"
        assert category.description == "Мобильные телефоны"
        assert Category.product_count == 1

    def test_add_product(self, product_samsung: Product) -> None:
        """Проверяет добавление товара через add_product."""
        category = Category("Смартфоны", "Мобильные телефоны", [])
        assert Category.product_count == 0
        category.add_product(product_samsung)
        assert Category.product_count == 1
        assert "Samsung Galaxy S23" in category.products

    def test_add_product_increments_by_one(self, product_samsung: Product) -> None:
        """add_product увеличивает счётчик на 1."""
        category = Category("Категория", "Описание", [])
        category.add_product(product_samsung)
        category.add_product(product_samsung)
        assert Category.product_count == 2

    def test_products_getter_format(self, product_samsung: Product) -> None:
        """Геттер products возвращает строку по шаблону."""
        category = Category("Смартфоны", "Мобильные телефоны", [product_samsung])
        result = category.products
        assert "Samsung Galaxy S23" in result
        assert "79999.99 руб." in result
        assert "Остаток: 10 шт." in result
        assert result.endswith("\n")

    def test_products_getter_empty(self) -> None:
        """Пустая категория — пустая строка."""
        category = Category("Пустая", "Описание", [])
        assert category.products == ""

    def test_category_count(self, product_samsung: Product) -> None:
        """Проверяет подсчёт количества категорий."""
        Category("Категория 1", "Описание", [product_samsung])
        Category("Категория 2", "Описание", [product_samsung])
        Category("Категория 3", "Описание", [])
        assert Category.category_count == 3

    def test_product_count(
        self, product_samsung: Product, product_iphone: Product
    ) -> None:
        """Проверяет подсчёт количества продуктов."""
        Category("Категория 1", "Описание", [product_samsung, product_iphone])
        assert Category.product_count == 2
        Category("Категория 2", "Описание", [product_samsung])
        assert Category.product_count == 3

    def test_product_count_empty_category(self) -> None:
        """Пустая категория не увеличивает счётчик товаров."""
        Category("Пустая", "Описание", [])
        assert Category.product_count == 0
        assert Category.category_count == 1