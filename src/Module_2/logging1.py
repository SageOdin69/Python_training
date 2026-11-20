import logging

logging.basicConfig(filename='C:/Python_training/logs/app.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('This is the info message')
logging.warning('This is the warning message')
logging.error('This is the error message')

print('Logging successful')