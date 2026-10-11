import pytest

from src.products import Category, Product


# ---------- Фикстуры ----------
@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23", "Смартфон", 79999.99, 10)


@pytest.fixture
def product_iphone() -> Product:
    return Product("iPhone 15", "Флагман", 99999.50, 5)


# ---------- Тесты Product ----------
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


class TestProductPrice:
    """Тесты для геттера и сеттера цены."""

    def test_price_getter(self) -> None:
        product = Product("Test", "Описание", 100.50, 5)
        assert product.price == 100.50

    def test_price_setter_valid(self) -> None:
        product = Product("Test", "Описание", 100.50, 5)
        product.price = 200.0
        assert product.price == 200.0

    def test_price_setter_zero(self, capsys: pytest.CaptureFixture) -> None:
        product = Product("Test", "Описание", 100.50, 5)
        product.price = 0
        assert product.price == 100.50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_negative(self, capsys: pytest.CaptureFixture) -> None:
        product = Product("Test", "Описание", 100.50, 5)
        product.price = -10
        assert product.price == 100.50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out


class TestProductNewProduct:
    """Тесты для класс-метода new_product."""

    def test_new_product(self) -> None:
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


class TestProductStr:
    """Тесты для __str__ класса Product."""

    def test_product_str(self) -> None:
        product = Product("iPhone 15", "Флагман", 99999.50, 5)
        assert str(product) == "iPhone 15, 99999.5 руб. Остаток: 5 шт."

    def test_product_str_with_float_price(self) -> None:
        product = Product("Test", "Описание", 80.0, 15)
        assert str(product) == "Test, 80.0 руб. Остаток: 15 шт."

    def test_product_str_with_zero_quantity(self) -> None:
        product = Product("Test", "Описание", 100.0, 0)
        assert str(product) == "Test, 100.0 руб. Остаток: 0 шт."

    @pytest.mark.parametrize(
        "name, price, quantity, expected",
        [
            ("A", 100.0, 10, "A, 100.0 руб. Остаток: 10 шт."),
            ("B", 200.5, 2, "B, 200.5 руб. Остаток: 2 шт."),
            ("C", 0.99, 100, "C, 0.99 руб. Остаток: 100 шт."),
        ],
    )
    def test_product_str_parametrized(
        self, name: str, price: float, quantity: int, expected: str
    ) -> None:
        product = Product(name, "Описание", price, quantity)
        assert str(product) == expected


class TestProductAdd:
    """Тесты для __add__ класса Product."""

    def test_add_two_products(self) -> None:
        product_a = Product("A", "Описание A", 100.0, 10)
        product_b = Product("B", "Описание B", 200.0, 2)
        assert product_a + product_b == 1400.0

    def test_add_returns_number(self) -> None:
        product_a = Product("A", "Описание", 100.0, 10)
        product_b = Product("B", "Описание", 200.0, 2)
        result = product_a + product_b
        assert isinstance(result, (int, float))

    def test_add_with_itself(self) -> None:
        product = Product("A", "Описание", 100.0, 10)
        assert product + product == 2000.0

    def test_add_with_zero_quantity(self) -> None:
        product_a = Product("A", "Описание", 100.0, 10)
        product_b = Product("B", "Описание", 200.0, 0)
        assert product_a + product_b == 1000.0

    def test_add_with_invalid_type(self) -> None:
        product = Product("A", "Описание", 100.0, 10)
        with pytest.raises(TypeError):
            product + "not a product"

    @pytest.mark.parametrize(
        "price_a, qty_a, price_b, qty_b, expected",
        [
            (100.0, 10, 200.0, 2, 1400.0),
            (50.0, 5, 50.0, 5, 500.0),
            (0.01, 1000, 1.0, 1, 11.0),
        ],
    )
    def test_add_parametrized(
        self,
        price_a: float,
        qty_a: int,
        price_b: float,
        qty_b: int,
        expected: float,
    ) -> None:
        a = Product("A", "Описание", price_a, qty_a)
        b = Product("B", "Описание", price_b, qty_b)
        assert a + b == pytest.approx(expected)


# ---------- Тесты Category ----------
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
        assert "Samsung Galaxy S23" in category.products

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


class TestCategoryProductsGetter:
    """Тесты для геттера products."""

    def setup_method(self) -> None:
        Category.category_count = 0
        Category.product_count = 0

    def test_products_getter_format(self, product_samsung: Product) -> None:
        """Геттер возвращает строку по шаблону через __str__ продукта."""
        category = Category("Смартфоны", "Описание", [product_samsung])
        result = category.products
        assert result == "Samsung Galaxy S23, 79999.99 руб. Остаток: 10 шт.\n"

    def test_products_getter_empty(self) -> None:
        """Пустая категория — пустая строка."""
        category = Category("Пустая", "Описание", [])
        assert category.products == ""

    def test_products_getter_multiple(self, product_samsung: Product, product_iphone: Product) -> None:
        """Несколько товаров — каждая строка заканчивается \\n."""
        category = Category("Смартфоны", "Описание", [product_samsung, product_iphone])
        result = category.products
        assert result.count("\n") == 2
        assert "Samsung Galaxy S23" in result
        assert "iPhone 15" in result


class TestCategoryStr:
    """Тесты для __str__ класса Category."""

    def setup_method(self) -> None:
        Category.category_count = 0
        Category.product_count = 0

    def test_category_str(self, product_samsung: Product, product_iphone: Product) -> None:
        """Проверяет строковое представление категории."""
        category = Category(
            "Смартфоны", "Мобильные телефоны", [product_samsung, product_iphone]
        )
        assert str(category) == "Смартфоны, количество продуктов: 15 шт."

    def test_category_str_empty(self) -> None:
        """Пустая категория — 0 шт."""
        category = Category("Пустая", "Описание", [])
        assert str(category) == "Пустая, количество продуктов: 0 шт."

    def test_category_str_one_product(self, product_samsung: Product) -> None:
        """Категория с одним товаром."""
        category = Category("Смартфоны", "Описание", [product_samsung])
        assert str(category) == "Смартфоны, количество продуктов: 10 шт."

    def test_category_str_sums_quantities(self) -> None:
        """Проверяет, что количество суммируется по всем товарам."""
        products = [
            Product("A", "Описание", 100.0, 3),
            Product("B", "Описание", 200.0, 5),
            Product("C", "Описание", 300.0, 7),
        ]
        category = Category("Категория", "Описание", products)
        assert str(category) == "Категория, количество продуктов: 15 шт."

    @pytest.mark.parametrize(
        "quantities, expected_total",
        [
            ([1, 2, 3], 6),
            ([10], 10),
            ([0, 0, 0], 0),
            ([100, 200], 300),
        ],
    )
    def test_category_str_parametrized(
        self, quantities: list, expected_total: int
    ) -> None:
        products = [
            Product(f"P{i}", "Описание", 100.0, qty)
            for i, qty in enumerate(quantities)
        ]
        category = Category("Категория", "Описание", products)
        assert str(category) == f"Категория, количество продуктов: {expected_total} шт."