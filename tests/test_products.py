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

    def test_product_attributes_types(self) -> None:
        """Проверяет типы атрибутов Product."""
        product = Product("Test", "Описание", 100.50, 5)
        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)

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
        assert len(category.products) == 1
        assert category.products[0].name == "Samsung Galaxy S23"

    def test_category_count(self, product_samsung: Product) -> None:
        """Проверяет подсчёт количества категорий."""
        assert Category.category_count == 0
        Category("Категория 1", "Описание", [product_samsung])
        assert Category.category_count == 1
        Category("Категория 2", "Описание", [product_samsung])
        assert Category.category_count == 2
        Category("Категория 3", "Описание", [])
        assert Category.category_count == 3

    def test_product_count(
        self, product_samsung: Product, product_iphone: Product
    ) -> None:
        """Проверяет подсчёт количества продуктов."""
        assert Category.product_count == 0
        Category("Категория 1", "Описание", [product_samsung, product_iphone])
        assert Category.product_count == 2
        Category("Категория 2", "Описание", [product_samsung])
        assert Category.product_count == 3

    def test_product_count_empty_category(self) -> None:
        """Пустая категория не увеличивает счётчик товаров."""
        Category("Пустая", "Описание", [])
        assert Category.product_count == 0
        assert Category.category_count == 1

    def test_category_attributes_types(self, product_samsung: Product) -> None:
        category = Category("Test", "Описание", [product_samsung])
        assert isinstance(category.name, str)
        assert isinstance(category.description, str)
        assert isinstance(category.products, list)
        assert isinstance(Category.category_count, int)
        assert isinstance(Category.product_count, int)
