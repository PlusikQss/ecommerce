from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов магазина."""

    name: str
    description: str
    quantity: int

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        ...

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение продуктов одного класса."""
        ...
