"""Main module"""


import logging
from controller10 import Controller10


# Create custom logger
logging.basicConfig(filename='lab1.txt', filemode='w',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)

number_of_disks = int(input("Enter quntity of disks: "))
disk_space = int(input("Enter disk's space: "))
con0 = Controller10(number_of_disks, disk_space)
variants = "1 - Ввод данных\
            2 - Вывод состояния RAID\
            3 - Показать избыточность\
            4 - Удалить данные\
            5 - Конец работы\n"
while True:
    n = input(variants)
    match n:
        case "1":
            letter, size = input("Введите данные: ").split()
            con0.write_data(letter, int(size))
        case "2":
            print(con0.get_state())
            print(con0.get_data_blocks())
        case "3":
            print(con0.get_redundancy())
        case "4":
            con0.delete_data(input("Введите данные, которые надо удалить"))
        case "5":
            print("Завершение работы")
            break
        case __:
            print("Неправильный ввод!")
