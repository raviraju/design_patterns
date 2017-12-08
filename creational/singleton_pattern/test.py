from logger import Logger

logger = Logger('my.log')
logger.write_log('Logging with classic Singleton pattern')
logger2 = Logger('my1.log')
logger2.write_log('Another log record is written to same log file')

logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line, end='')
