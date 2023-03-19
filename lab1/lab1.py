"""Main module"""


import logging
from controller10 import Controller10


# Create custom logger
logging.basicConfig(filename='lab1.txt', filemode='w',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)

number_of_disks = int(input("Enter quntity of disks: "))
disk_space = int(input("Enter disk's space: "))
con0 = Controller10(number_of_disks, disk_space)
con0.get_state()
con0.write_data('A', 40)
con0.write_data('C', 30)
con0.write_data('B', 20)
con0.get_state()

con0.get_data_blocks()
con0.delete_data("A")
con0.get_data_blocks()
