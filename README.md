## Наследование

### `Smartphone` — наследник `Product`

Дополнительные атрибуты:
- `efficiency` (float) — производительность
- `model` (str) — модель
- `memory` (int) — объём встроенной памяти
- `color` (str) — цвет

```python
from src.products import Smartphone

phone = Smartphone(
    "Samsung Galaxy S23", "Смартфон", 79999.99, 10,
    efficiency=95.0, model="Galaxy S23", memory=256, color="чёрный",
)
print(phone)
# Samsung Galaxy S23, 79999.99 руб. Остаток: 10 шт.