BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс описывает модель книги
    """
    def __init__(self, id_: int, name: str, pages: int):
        """Инициализация объекта класс
        :param id_: идентификационный номер книги
        :param name: название книги
        :param pages: количество страниц
        Пример:
        >>> my_book = Book(13, "War and peace", 4000)
        """
        if not isinstance(id_, int):
            raise TypeError ("Must be integer")
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError ("Must be string")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError ("Must be integer")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
