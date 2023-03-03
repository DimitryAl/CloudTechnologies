from disk import Disk

# Контроллер RAID0
class Controller0:

    controller_type = 'RAID0'

    def __init__(self) -> None:
        pass

    # Задаём нужно кол-во дисков
    def set_disks(self, qnt: int, size: int) -> None:
        self.disks_number = qnt
        self.disks = []
        for i in range(qnt):
            self.disks.append(Disk(str(i), size))

    # Записываем данные на диски
    def write_data(self, size: int) -> int:
        # разбиваем данные между дисками
        part = size / self.disks_number
        ###
        # НУЖНА ПРОВЕРКА ЕСТЬ ЛИ МЕСТО
        ###
        for disk in self.disks:
            if disk.storage - part < 0:
                return 0
            else:
                disk.storage = disk.storage - part
                disk.write()
        return 1

    # Вывести содержимое дисков
    #def print_data(self):
        #for disk in self.disks:
        #    print(disk.read())

    