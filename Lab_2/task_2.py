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
        """Инициализация экземпляра класса
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


class Library:
    """Класс описывает модель библиотеки"""
    def __init__(self, books=None):
        """Инициализация экземпляра класса
        Пример:
        >>> my_lib = Library()
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """Метод возвращает ID следующей книги"""
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        """Метод возвращает порядок книги в библиотке по запрашиваемому ID"""
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
        raise ValueError ("There's no book with requested id")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
