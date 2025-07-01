import logging
logging.basicConfig(level=logging.INFO, filename='test.log',
                    format='%(asctime)s - %(levelname)s -%(message)s')

logger= logging.getLogger('test')
console_handler =logging.StreamHandler()
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)