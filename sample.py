import logging
import employee

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
# ERROR: Due to a more seious problem, the software has not been able to perform some function.
# CRITICAL: A serious eror, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename='sample.log', level=logging.DEBUG, 
#                     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# print('Add: {} - {} = {}'.format(num_1, num_2, sub_result))
# logging.info('Add: {} - {} = {}'.format(num_1, num_2, sub_result))
logger.debug('Add: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print('Add: {} * {} = {}'.format(num_1, num_2, mul_result))
# logging.info('Add: {} * {} = {}'.format(num_1, num_2, mul_result))
logger.debug('Add: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# print('Add: {} / {} = {}'.format(num_1, num_2, div_result))
# logging.info('Add: {} / {} = {}'.format(num_1, num_2, div_result))
logger.debug('Add: {} / {} = {}'.format(num_1, num_2, div_result))

# print(__name__)
# print(__main__)
