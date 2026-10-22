from typing import Any


class CreationInfoMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{key}={value!r}" for key, value in kwargs.items()]
        params = ", ".join(args_repr + kwargs_repr)
        print(f"{self.__class__.__name__}({params})")
