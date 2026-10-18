import pytest

from src.products import (
    BaseProduct,
    Category,
    CreationInfoMixin,
    LawnGrass,
    Product,
    Smartphone,
)


class TestProduct:

    def test_product_init(self) -> None:
        product = Product("Test", "Описание", 100.50, 5)
        assert product.name == "Test"
        assert product.description == "Описание"
        assert product.price == 100.50
        assert product.quantity == 5

    def test_product_str(self) -> None:
        product = Product("iPhone 15", "Флагман", 99999.50, 5)
        assert str(product) == "iPhone 15, 99999.5 руб. Остаток: 5 шт."

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

    def test_new_product(self) -> None:
        data = {
            "name": "New",
            "description": "Описание",
            "price": 500.0,
            "quantity": 10,
        }
        product = Product.new_product(data)
        assert product.name == "New"
        assert product.quantity == 10


class TestProductAdd:

    def test_add_two_products(self) -> None:
        a = Product("A", "Описание A", 100.0, 10)
        b = Product("B", "Описание B", 200.0, 2)
        assert a + b == 1400.0

    def test_add_with_invalid_type(self) -> None:
        product = Product("A", "Описание", 100.0, 10)
        with pytest.raises(TypeError):
            product + "not a product"

    def test_add_different_classes_raises(
        self,
        smartphone_samsung: Smartphone,
        lawn_grass: LawnGrass,
    ) -> None:
        with pytest.raises(TypeError):
            smartphone_samsung + lawn_grass

    def test_add_same_smartphones(
        self,
        smartphone_samsung: Smartphone,
        smartphone_iphone: Smartphone,
    ) -> None:
        result = smartphone_samsung + smartphone_iphone
        expected = (
            smartphone_samsung.price * smartphone_samsung.quantity
            + smartphone_iphone.price * smartphone_iphone.quantity
        )
        assert result == pytest.approx(expected)


class TestSmartphone:

    def test_smartphone_attributes(self, smartphone_samsung: Smartphone) -> None:
        assert smartphone_samsung.efficiency == 95.0
        assert smartphone_samsung.model == "Galaxy S23"
        assert smartphone_samsung.memory == 256
        assert smartphone_samsung.color == "чёрный"
        assert isinstance(smartphone_samsung, Product)

    def test_smartphone_str(self, smartphone_samsung: Smartphone) -> None:
        assert str(smartphone_samsung) == (
            "Samsung Galaxy S23, 79999.99 руб. Остаток: 10 шт."
        )


class TestLawnGrass:

    def test_lawn_grass_attributes(self, lawn_grass: LawnGrass) -> None:
        assert lawn_grass.country == "Россия"
        assert lawn_grass.germination_period == "7-14 дней"
        assert lawn_grass.color == "зелёный"
        assert isinstance(lawn_grass, Product)

    def test_lawn_grass_str(self, lawn_grass: LawnGrass) -> None:
        assert str(lawn_grass) == ("Газонная трава, 1200.0 руб. Остаток: 50 шт.")


class TestCategory:

    def setup_method(self) -> None:
        Category.category_count = 0
        Category.product_count = 0

    def test_category_init(self, smartphone_samsung: Smartphone) -> None:
        category = Category("Смартфоны", "Описание", [smartphone_samsung])
        assert category.name == "Смартфоны"
        assert category.description == "Описание"
        assert "Samsung Galaxy S23" in category.products

    def test_add_product(self, smartphone_samsung: Smartphone) -> None:
        category = Category("Смартфоны", "Описание", [])
        assert Category.product_count == 0
        category.add_product(smartphone_samsung)
        assert Category.product_count == 1

    def test_add_product_invalid_type(self) -> None:
        category = Category("Смартфоны", "Описание", [])
        with pytest.raises(TypeError):
            category.add_product("not a product")

    def test_add_product_subclass(self, lawn_grass: LawnGrass) -> None:
        category = Category("Трава", "Описание", [])
        category.add_product(lawn_grass)
        assert "Газонная трава" in category.products

    def test_product_count(
        self,
        smartphone_samsung: Smartphone,
        lawn_grass: LawnGrass,
    ) -> None:
        Category(
            "Категория",
            "Описание",
            [smartphone_samsung, lawn_grass],
        )
        assert Category.product_count == 2

    def test_category_str(
        self,
        smartphone_samsung: Smartphone,
        smartphone_iphone: Smartphone,
    ) -> None:
        category = Category(
            "Смартфоны",
            "Описание",
            [smartphone_samsung, smartphone_iphone],
        )
        assert str(category) == "Смартфоны, количество продуктов: 15 шт."


class TestBaseProduct:

    def test_base_product_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            BaseProduct()  # type: ignore[abstract]

    def test_product_is_base_product_subclass(self, product_samsung: Product) -> None:
        assert isinstance(product_samsung, BaseProduct)

    def test_smartphone_is_base_product_subclass(
        self, smartphone_samsung: Smartphone
    ) -> None:
        assert isinstance(smartphone_samsung, BaseProduct)

    def test_lawn_grass_is_base_product_subclass(self, lawn_grass: LawnGrass) -> None:
        assert isinstance(lawn_grass, BaseProduct)


class TestCreationInfoMixin:

    def test_mixin_prints_on_product_creation(
        self, capsys: pytest.CaptureFixture
    ) -> None:
        Product("Продукт1", "Описание продукта", 1200.0, 10)
        captured = capsys.readouterr()
        assert "Product(" in captured.out
        assert "Продукт1" in captured.out
        assert "1200.0" in captured.out

    def test_mixin_prints_on_smartphone_creation(
        self, capsys: pytest.CaptureFixture
    ) -> None:
        Smartphone(
            "Samsung",
            "Смартфон",
            79999.99,
            10,
            efficiency=95.0,
            model="S23",
            memory=256,
            color="чёрный",
        )
        captured = capsys.readouterr()
        assert "Smartphone(" in captured.out
        assert "Samsung" in captured.out

    def test_mixin_prints_on_lawn_grass_creation(
        self, capsys: pytest.CaptureFixture
    ) -> None:
        LawnGrass(
            "Трава",
            "Описание",
            1200.0,
            50,
            country="Россия",
            germination_period="7-14 дней",
            color="зелёный",
        )
        captured = capsys.readouterr()
        assert "LawnGrass(" in captured.out
        assert "Трава" in captured.out

    def test_mixin_in_mro(self) -> None:
        assert CreationInfoMixin in Product.__mro__
