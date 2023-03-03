#from disk import Disk
from controller1 import Controller1

# Контроллер RAID10
class Controller10:

    controller_type = 'RAID10'

    def __init__(self, qnt = 6, size = 80) -> None:
        print('Creating RAID10')
        self.add_disks(qnt, size)

    def get_state(self):
        print(self.controller_type)
        print(self.disks_number)
        print(self.disks_size)

    
    # Добавляем диски в RAID 
    def add_disks(self, qnt = 6, size = 80) -> None:
        self.disks_number = qnt
        self.disks_size = size
        self.disks = []
        for i in range(qnt):
            #self.disks.append(Disk(str(i), size))
            self.disks.append(Controller1(8, size))

    # Записываем данные на диски
    def write_data(self, size: int) -> int:
        
        # Вычисляем размер данных, которые необходимо записать на каждый диск
        part = size / self.disks_number
        
        # Проверяем есть ли на дисках место
        if self.disks[0].get_storage() < part:
            return 0
        
        # Пишем данные на диск
        for disk in self.disks:
            disk.write_data(size)
        
        return 1