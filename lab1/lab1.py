import logging
from controller10 import Controller10


# Create custom logger
logging.basicConfig(filename='lab1.txt', filemode='w',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)

con0 = Controller10(2, 80)
con0.get_state()
con0.write_data('A', 40)
con0.get_state()
con0.write_data('B', 35)
con0.get_state()
con0.write_data('C', 60)
con0.get_state()
con0.get_data_blocks()

#   № варианта  Уровень RAID    Число дисков	Емкость 1 диска     Объем данных в наборе, GB
#   1.		    RAID 10	        6 и 8	        80GB	            40

