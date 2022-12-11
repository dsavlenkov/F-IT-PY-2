import doctest
from typing import Union


class Student:
    """
    Документация на класс
    Класс описывает модель студента
    """
    def __init__(self, age: int, university: str, skills: list):
        """ Инициализация экземпляра класса
        :param: age: возраст студента
        :param: university: университет, в котором обучается студент
        :param: skills: навыки студента
        Пример:
        >>> first_student = Student(21, "SPBPU", ["HTML", "CSS", "JavaScript"])
        """
        if not isinstance(age, int):
            raise TypeError
        self.age = age
        if not isinstance(university, str):
            raise TypeError
        self.university = university
        if not isinstance(skills, list):
            raise TypeError
        self.skills = skills

    def learn_new_skill(self, skill_name: str):
        """
        Метод прибавляет новый навык к списку навков студента
        :param skill_name: новый навык
        Пример:
        >>> first_student = Student(21, "SPBPU", ["HTML", "CSS", "JavaScript"])
        >>> first_student.learn_new_skill("Python")
        """
        if not isinstance(skill_name, str):
            raise TypeError
        self.skills.append(skill_name)

    def change_university(self, new_university):
        """
        "Переводит" студента в новый ВУЗ
        :param new_university: новый ВУЗ
        Пример:
        >>> first_student = Student(21, "SPBPU", ["HTML", "CSS", "JavaScript"])
        >>> first_student.change_university("ITMO")
        """
        self.university = new_university


class PersonalComputer:
    """
    Документация на класс
    Класс описывает модель персонального компьютера
    """
    def __init__(self, cpu: str, ram: int, gpu: str):
        """ Инициализация экземпляра класса
        :param: cpu: процессор
        :param: ram: объем оперативной памяти
        :param: gpu: видеокарта
        Пример:
        >>> my_computer = PersonalComputer("Intel-Core-i5-7600K", 16, "GTX-1060-6GB")
        """
        if not isinstance(cpu, str):
            raise TypeError
        self.cpu = cpu
        if not isinstance(ram, int):
            raise TypeError
        self.ram = ram
        if not isinstance(gpu, str):
            raise TypeError

    def add_more_ram(self, adding_ram):
        """
        Метод добавляет оперативную память к имеющейся
        :param adding_ram: объем добавляемой оперативки
        Пример:
        >>> my_computer = PersonalComputer("Intel-Core-i5-7600K", 16, "GTX-1060-6GB")
        >>> my_computer.add_more_ram(16)
        """
        self.ram += adding_ram

    def change_cpu(self, new_cpu):
        """
        Метод меняет процессор модели компьютера
        :param new_cpu: новый ЦП
        Пример:
        >>> my_computer = PersonalComputer("Intel-Core-i5-7600K", 16, "GTX-1060-6GB")
        >>> my_computer.change_cpu("Intel-Core-i7-7700K")
        """
        self.cpu = new_cpu

    def change_gpu(self, new_gpu):
        """
        Метод меняет видеокарту модели компьютера
        :param new_gpu: новая видеокарта
        Пример:
        >>> my_computer = PersonalComputer("Intel-Core-i5-7600K", 16, "GTX-1060-6GB")
        >>> my_computer.change_gpu("RTX-2060-TI")
        """
        self.cpu = new_gpu


class Car:
    """
    Документация на класс
    Класс описывает модель автомобиля с ДВС
    """
    def __init__(self, brand: str, model: str, engine_volume: Union[int, float], engine_name: str):
        """
        Инициализация экземпляра класса
        :param brand: Бренд авто
        :param model: Модель авто
        :param engine_volume: Объем ДВС
        :param engine_name: Модель ДВС
        Пример:
        >>> my_car = Car("Toyota", "Mark II X100", 2.5, "1JZ-GTE")
        """
        if not isinstance(brand, str):
            raise TypeError
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError
        self.model = model
        if not isinstance(engine_name, str):
            raise TypeError
        self.engine_name = engine_name
        if not isinstance(engine_volume, (int, float)):
            raise TypeError
        self.engine_volume = engine_volume

    def engine_swap(self, new_engine_name, new_engine_volume):
        """
        Метод меняет двигатель в модели автомобиля
        :param new_engine_name: Модель нового ДВС
        :param new_engine_volume: Объем нового ДВС
        Пример:
        >>> my_car = Car("Toyota", "Mark II X100", 2.5, "1JZ-GTE")
        >>> my_car.engine_swap("2JZ-GTE", 3.0)
        """
        self.engine_name = new_engine_name
        self.engine_volume = new_engine_volume


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
