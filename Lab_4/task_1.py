class PersonalComputer:
    """Базовый класс модели персонального компьютера"""
    def __init__(self, brand: str, os: str, display_diagonal: float):
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть типа str")
        self._brand = brand
        if not isinstance(display_diagonal, float):
            raise TypeError("Диагональ экрана должна быть типа float")
        self._display_diagonal = display_diagonal
        if not isinstance(os, str):
            raise TypeError("Имя операционной системы должно быть типа str")
        self.os = os

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def display_diagonal(self) -> float:
        return self._display_diagonal

    def __str__(self):
        return f'Бренд: {self._brand}, Операционная система: {self.os}, Диагональ экрана: {self._display_diagonal}'

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self._brand!r}, os={self.os!r}, display_diagonal={self._display_diagonal!r})"


class DesktopComputer(PersonalComputer):
    def __init__(self, brand: str, os: str, display_diagonal: float, is_there_water_cooling: bool):
        super().__init__(brand, os, display_diagonal)
        if not isinstance(is_there_water_cooling, bool):
            raise TypeError("Инфрмация о наличии водяного охлаждения должна иметь тип bool")
        self.is_there_water_cooling = is_there_water_cooling


class LaptopComputer(PersonalComputer):
    def __init__(self, brand: str, os: str, display_diagonal: float, mass: float):
        super().__init__(brand, os, display_diagonal)
        if not isinstance(mass, float):
            raise TypeError("Значение массы должно быть типа float")
        self._mass = mass
if __name__ == "__main__":
    # Write your solution here
    pass
