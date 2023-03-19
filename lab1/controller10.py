"""Когтроллер RAID10"""


import math
import logging
from controller1 import Controller1


logging.basicConfig(filename='lab1.txt', filemode='w',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)


class Controller10:
    """RAID10 Controller"""

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    controller_type = 'RAID10'
    disks_number = 0
    disks_size = 0
    disks = []
    disks_data = []

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

    def get_data_blocks(self) -> None:
        """ Вывести блоки данных в каждом диске"""
        logging.info("Data blocks:")
        for data in self.disks_data:
            logging.info("%s%i, %i", data[1], data[0], data[2])


    def __add_disks(self, qnt=6, size=80) -> None:
        """Добавить диски"""
        self.disks_number = qnt
        self.disks_size = size
        self.disks = []
        for __ in range(qnt):
            self.disks.append(Controller1(8, size))

    def write_data(self, letter, size: int) -> None:
        """Запись данных на диск"""

        logging.info("Trying to write %i GB", size)
        # Вычисляем размер данных, которые необходимо записать на каждый диск
        part = size / self.disks_number
        if not part.is_integer():
            part = math.trunc(part) + 1
        # Проверяем есть ли на дисках место
        if self.disks[0].get_free_storage() < part:
            logging.error("Not enough free space in RAID!")
            return 0

        # Пишем данные на диск
        #for disk in self.disks:
        for i in range(len(self.disks)):
            self.disks[i].write_data(part)
            #disk.write_data(part)
            self.disks_data.append((i, letter, part))

    def delete_data(self, letter: str) -> None:
        """Удалить данные из RAID"""
        logging.info("Deleting data block %s", letter)
        flag = True
        while True:
            flag = True
            for data in self.disks_data:
                if data[1] == letter:
                    self.disks_data.remove(data)
                    flag = False
            if flag:
                break

