from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def main() -> None:
    """Демонстрация работы классов."""
    smartphone1 = Smartphone(
        "Samsung Galaxy S23",
        "Смартфон с отличной камерой",
        79999.99,
        10,
        efficiency=95.0,
        model="Galaxy S23",
        memory=256,
        color="чёрный",
    )
    smartphone2 = Smartphone(
        "iPhone 15",
        "Флагман от Apple",
        99999.50,
        5,
        efficiency=98.0,
        model="iPhone 15",
        memory=128,
        color="белый",
    )
    grass = LawnGrass(
        "Газонная трава",
        "Быстрорастущая трава для газона",
        1200.00,
        50,
        country="Россия",
        germination_period="7-14 дней",
        color="зелёный",
    )
    regular_product = Product(
        "Xiaomi Redmi Note 12",
        "Бюджетный смартфон",
        19999.00,
        25,
    )

    category = Category(
        "Смартфоны и товары",
        "Разные товары магазина",
        [smartphone1, smartphone2, grass, regular_product],
    )

    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    print("Товары:")
    print(category.products)
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    print("\n--- Сложение одинаковых классов ---")
    print(f"Смартфон + Смартфон = {smartphone1 + smartphone2}")
    print(f"Трава + Трава = {grass + grass}")

    print("\n--- Ограничения сложения ---")
    try:
        smartphone1 + grass
    except TypeError as exc:
        print(f"Ошибка: {exc}")

    print("\n--- Ограничения добавления ---")
    try:
        category.add_product("не продукт")
    except TypeError as exc:
        print(f"Ошибка: {exc}")

    print("\n--- new_product ---")
    new_data = {
        "name": "Google Pixel 8",
        "description": "Смартфон от Google",
        "price": 69999.00,
        "quantity": 7,
    }
    new_product = Product.new_product(new_data)
    print(f"Создан: {new_product}")


if __name__ == "__main__":
    main()
