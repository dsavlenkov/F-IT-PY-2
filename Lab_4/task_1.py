class PersonalComputer:
    """Базовый класс модели персонального компьютера"""
    def __init__(self, brand: str, os: str, display_diagonal: float, price: int):
        """
        Инициализация экземпляра класса
        :param brand: Бренд компьютера
        :param os: Операционная система, установленная на компьютере
        :param display_diagonal: Диагональ дисплея компьютера
        >>> my_pc = PersonalComputer("Lenovo", "FreeDOS", 17.1, 50000) """
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть типа str")
        self._brand = brand
        if not isinstance(display_diagonal, float):
            raise TypeError("Диагональ экрана должна быть типа float")
        elif display_diagonal <= 0:
            raise ValueError("")
        self._display_diagonal = display_diagonal
        if not isinstance(os, str):
            raise TypeError("Имя операционной системы должно быть типа str")
        self._os = os
        if not isinstance(price, int):
            raise TypeError("Цена должна быть типа int")
        elif price < 0:
            raise ValueError("Цена должна быть не меньше нуля")
        self._price = price

    @property
    def brand(self) -> str:
        """
        Геттер для защиты от несанкционированного изменения имени бренда
        Сеттер не прописан, поскольку возможность смены бренда не предусмотрена """
        return self._brand

    @property
    def display_diagonal(self) -> float:
        """
        Геттер для защиты от несанкционированного изменения значения диагонали экрана
        Сеттер не прописан, поскольку возможность смены диагонали дисплея не предусмотрена """
        return self._display_diagonal

    @property
    def os(self) -> str:
        """ Геттер для инкапсулированной передачи информации об ОС """
        return self._os

    @os.setter
    def os(self, new_os) -> None:
        """ Сеттер для инкапсулированной смены ОС """
        self._os = new_os

    def change_os(self, os):
        ...

    def index_price(self, multiplier: float):
        """ Индексирует цену компьютера путем умножения на множитель
        >>> my_pc = PersonalComputer("Lenovo", "FreeDOS", 17.1, 50000)
        >>> my_pc.index_price(0.9)
        """
        self._price *= multiplier

    def __str__(self):
        return f'Бренд: {self._brand}, Операционная система: {self._os}, Диагональ экрана: {self._display_diagonal}, Цена: {self._price}'

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self._brand!r}, os={self._os!r}, display_diagonal={self._display_diagonal!r})"


class DesktopComputer(PersonalComputer):
    """ Дочерний класс модели стационарного компьютера """
    def __init__(self, brand: str, os: str, display_diagonal: float, is_there_water_cooling: bool, price: int):
        """ Инициализация экземпляра класса
        :param is_there_water_cooling: Показывает наличие либо отсутствие водяного охлаждения в системном блоке
        >>> my_pc = DesktopComputer("Invasion Labs", "Windows", 24.6, True, 150000)
        """
        super().__init__(brand, os, display_diagonal, price)
        # наследование конструктора базового класса
        if not isinstance(is_there_water_cooling, bool):
            raise TypeError("Информация о наличии водяного охлаждения должна иметь тип bool")
        self.is_there_water_cooling = is_there_water_cooling

    def change_os(self, os):
        ...

    def __str__(self):
        return super().__str__() + f'Наличие водяного охлаждения: {self.is_there_water_cooling}'

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self._brand!r}, os={self._os!r}, display_diagonal={self._display_diagonal!r}, is_there_water_cooling={self.is_there_water_cooling!r}, price={self._price!r})"


class LaptopComputer(PersonalComputer):
    """ Дочерний класс модели ноутбука"""
    def __init__(self, brand: str, os: str, display_diagonal: float, mass: float, price: int):
        """Инициализация экземпляра класса
        :param mass: Масса ноутбука
        >>> my_pc = LaptopComputer("Dell", "Kali", 16.7, 1.9, 65000)
        """
        super().__init__(brand, os, display_diagonal, price)
        if not isinstance(mass, float):
            raise TypeError("Значение массы должно быть типа float")
        self._mass = mass

    def change_os(self, os):
        ...

    def __str__(self) -> str:
        return super().__str__() + f', Масса: {self._mass}'

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self._brand!r}, os={self._os!r}, display_diagonal={self._display_diagonal!r}, mass={self._mass!r}, price={self._price!r})"

pc1 = LaptopComputer("ASUS", "Windows", 17.3, 3.2, 70000)
pc1.os = "Ubuntu"
pc1.index_price(1.3)
print(pc1)
print(pc1.__str__())
print(pc1.__repr__())