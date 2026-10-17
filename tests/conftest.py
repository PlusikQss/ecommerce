import pytest

from src.products import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23", "Смартфон", 79999.99, 10)


@pytest.fixture
def product_iphone() -> Product:
    return Product("iPhone 15", "Флагман", 99999.50, 5)


@pytest.fixture
def smartphone_samsung() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23",
        "Смартфон с отличной камерой",
        79999.99,
        10,
        efficiency=95.0,
        model="Galaxy S23",
        memory=256,
        color="чёрный",
    )


@pytest.fixture
def smartphone_iphone() -> Smartphone:
    return Smartphone(
        "iPhone 15",
        "Флагман от Apple",
        99999.50,
        5,
        efficiency=98.0,
        model="iPhone 15",
        memory=128,
        color="белый",
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    return LawnGrass(
        "Газонная трава",
        "Быстрорастущая трава для газона",
        1200.00,
        50,
        country="Россия",
        germination_period="7-14 дней",
        color="зелёный",
    )


@pytest.fixture
def category_smartphones(
    smartphone_samsung: Smartphone,
    smartphone_iphone: Smartphone,
) -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Смартфоны",
        "Мобильные телефоны",
        [smartphone_samsung, smartphone_iphone],
    )
