"""Модуль предоставляет класс Disk"""


class Disk:
    """Диск"""

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.free_storage = size
        self.data = []

    def get_free_storage(self) -> float:
        """Возвращает количество свободного места"""
        return self.free_storage

    def __fill_storage(self, size: int) -> None:
        """Изменение количества свободного места"""
        self.free_storage -= size

    def write(self, size: int, data: bytearray = bytearray('No data', encoding='utf-8')) -> None:
        """Запись данных на диск"""
        self.__fill_storage(size)
        self.data.append(data)

    def read(self) -> bytearray:
        """Чтение с диска"""
        return self.data
