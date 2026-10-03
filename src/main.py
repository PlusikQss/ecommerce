from src.products import Category, Product


def main() -> None:
    """Демонстрация работы классов Product и Category."""
    # Создаём товары
    product1 = Product(
        "Samsung Galaxy S23",
        "Смартфон с отличной камерой",
        79999.99,
        10,
    )
    product2 = Product(
        "iPhone 15",
        "Флагман от Apple",
        99999.50,
        5,
    )
    product3 = Product(
        "Xiaomi Redmi Note 12",
        "Бюджетный смартфон",
        19999.00,
        25,
    )

    # Создаём категории
    smartphones = Category(
        "Смартфоны",
        "Мобильные телефоны и смартфоны",
        [product1, product2, product3],
    )

    laptops = Category(
        "Ноутбуки",
        "Портативные компьютеры",
        [
            Product("MacBook Air", "Лёгкий ноутбук от Apple", 119999.00, 3),
            Product("Lenovo IdeaPad", "Бюджетный ноутбук", 45999.00, 8),
        ],
    )

    # Вывод информации
    print(f"Категория: {smartphones.name}")
    print(f"Описание: {smartphones.description}")
    print(f"Товаров в категории: {len(smartphones.products)}")
    print()
    print(f"Категория: {laptops.name}")
    print(f"Описание: {laptops.description}")
    print(f"Товаров в категории: {len(laptops.products)}")
    print()
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
