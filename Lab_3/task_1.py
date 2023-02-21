import doctest

class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """ Инициализация экземпляра класса
        :param name : название книги
        :param author : автор книги
        Пример:
        >>> my_book = Book("Гоголь", "На дне")
        """
        if not isinstance(name, str):
            raise TypeError ("Имя книги должно быть строкового типа")
        self._name = name
        if not isinstance(author, str):
            raise TypeError ("Имя автора должно быть строкового типа")
        self._author = author

    @property
    def name(self) -> str:
        """Геттер для защиты от несакцианированного изменения имени книги"""
        return self._name

    @property
    def author(self) -> str:
        """Геттер для защиты от несакцианированного изменения имени автора"""
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс от класса Book, описывает модель бумажной книги """
    def __init__(self, name: str, author: str, pages: int):
        """ Инициализация экземпляра класса
        :param name : название книги
        :param author : автор книги
        :param pages : количество страниц в книге
        Пример:
        >>> my_book = Book("Гоголь", "На дне", 150)
        """
        super().__init__(name, author)
        # наследование параметров name и author из базового класса
        if not isinstance(pages, int):
            raise TypeError ("Количество страниц должно быть типа int")
        elif pages <= 0:
            raise ValueError ("Значения количества страниц должно быть положительным")
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:
        self._pages = new_pages

    def __str__(self):
        return super().__str__() + f" Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Дочерний класс от класса Book, описывает модель электронной книги """
    def __init__(self, name: str, author: str, duration: float):
        """ Инициализация экземпляра класса
                :param name : название книги
                :param author : автор книги
                :param duration : количество страниц в книге
                Пример:
                >>> my_book = Book("Гоголь", "На дне", 23.34)
                """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError ("Длительность книги должна быть типа float")
        elif duration <= 0:
            raise ValueError ("Значение длительности книги должно быть положительным")
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        self._duration = new_duration

    def __str__(self):
        return super().__str__() + f" Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

book1 = PaperBook("Dostoevsky", "Crime and Punishment", 500)
book2 = AudioBook("Tolstoy", "War and Peace", 234.34)
book2.duration = 43.43
print(book2.duration)
print(book1.__str__())
print(book2)

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

