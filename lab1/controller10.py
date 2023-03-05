"""Когтроллер RAID10"""


import logging
from controller1 import Controller1


logging.basicConfig(filename='lab1.txt', filemode='a',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)


class Controller10:
    """RAID10 Controller"""

    controller_type = 'RAID10'
    disks_number = 0
    disks_size = 0
    disks = []

    def __init__(self, qnt=6, size=80) -> None:
        logging.info(
            "Creating RAID10: Number of disks = %i, Disk's size = %i", qnt, size)
        self.__add_disks(qnt, size)

    def __del__(self):
        """Деструктор"""
        logging.info("RAID10 destroyed")

    def get_state(self) -> None:
        """Вывести состояние контроллера"""
        logging.info("Controller state: Controller type - %s, Number of disks - %i, Free space - %f",
                     self.controller_type, self.disks_number, self.disks[0].get_free_storage())

    def __add_disks(self, qnt=6, size=80) -> None:
        """Добавить диски"""
        self.disks_number = qnt
        self.disks_size = size
        self.disks = []
        for __ in range(qnt):
            self.disks.append(Controller1(8, size))

    def write_data(self, size: int) -> int:
        """Запись данных на диск"""

        # Вычисляем размер данных, которые необходимо записать на каждый диск
        part = size / self.disks_number

        # Проверяем есть ли на дисках место
        if self.disks[0].get_free_storage() < part:
            logging.info("Not enough free space in RAID!")
            return 0

        # Пишем данные на диск
        for disk in self.disks:
            disk.write_data(part)

        return 1
