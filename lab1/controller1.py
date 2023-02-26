from disk import Disk


# Контроллер RAID1
class Controller1:

    controller_type = 'RAID1'

    def __init__(self) -> None:
        pass

    # Задаём нужно кол-во дисков
    def set_disks(self, qnt: int, size: int) -> None:
        self.disks_number = qnt
        self.disks = []
        for i in range(qnt):
            self.disks.append(Disk(str(i), size))

    # Записываем данные в каждый диск
    def write_data(self, size: int, data: bytearray = 'No data') -> int:
        for disk in self.disks:
            if disk.storage - size < 0:
                return 0
            else:
                disk.storage = disk.storage - size
                disk.write(data)
        return 1

    # Вывести содержимое дисков
    def print_data(self) -> None:
        for disk in self.disks:
            print(disk.read())
