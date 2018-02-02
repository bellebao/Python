import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info('start program')
logging.info('trying to divide 1 by 0')
print (1/0)

logging.info('division success')

logging.info('end program')
