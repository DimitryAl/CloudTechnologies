import logging
from controller10 import Controller10


# Create custom logger
logging.basicConfig(filename='lab1.txt', filemode='a',
                    format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)

con0 = Controller10(6, 80)
con0.get_state()
con0.write_data(40)
con0.get_state()
con0.write_data(40)
con0.get_state()
con0.write_data(40)
con0.get_state()



#   № варианта  Уровень RAID    Число дисков	Емкость 1 диска     Объем данных в наборе, GB
#   1.		    RAID 10	        6 и 8	        80GB	            40

