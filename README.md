## Абстрактный класс и миксин

### `BaseProduct` — абстрактный базовый класс

Родительский класс для `Product`. Описывает общий интерфейс всех продуктов:
- `__str__` — строковое представление
- `__add__` — сложение продуктов одного класса

Напрямую создать `BaseProduct` нельзя — только наследников.

```python
from src.products import BaseProduct
BaseProduct()  # TypeError: Can't instantiate abstract class