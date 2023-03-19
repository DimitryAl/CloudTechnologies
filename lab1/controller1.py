"""Контроллер RAID1ы"""

import logging
from disk import Disk


logging.basicConfig(filename='lab1.txt', filemode='w',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)


class Controller1:
    """RAID1 Controller"""

    controller_type = 'RAID1'
    disks = []

    def __init__(self, qnt: int, size: int) -> None:
        self.__set_disks(qnt, size)

    def get_state(self):
        """Вывести состояние контроллера"""
        logging.info("Controller state: Controller type - %s, Number of disks - %i, Free space - %f",
                     self.controller_type, self.disks_number, self.get_free_storage())

    def __set_disks(self, qnt: int, size: int) -> None:
        """Задаём нужно кол-во дисков"""
        self.disks_number = qnt
        self.disks_size = size
        self.disks = []
        for i in range(qnt):
            self.disks.append(Disk(str(i), size))

    def write_data(self, size: int) -> int:
        """Запись данных на диск"""
        for disk in self.disks:
            disk.write(size)
        return 1

    def get_free_storage(self) -> float:
        """Возвращает сколько свободного места"""
        return self.disks[0].get_free_storage()

    def print_data(self) -> None:
        """Вывод содержимого массива"""
        for disk in self.disks:
            print(disk.read())
