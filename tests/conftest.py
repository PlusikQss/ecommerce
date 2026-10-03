import pytest

from src.products import Category, Product


@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23", "Смартфон", 79999.99, 10)


@pytest.fixture
def product_iphone() -> Product:
    return Product("iPhone 15", "Флагман", 99999.50, 5)


@pytest.fixture
def category_smartphones(product_samsung: Product, product_iphone: Product) -> Category:
    # Сбрасываем счётчики перед созданием
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Смартфоны", "Мобильные телефоны", [product_samsung, product_iphone]
    )
