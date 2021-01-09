import logging
import datetime

log_name = 'D:\\Apps-cas\\WinPython-3.6.3.0Qt5\\notebooks\\misc\\aap1.log'
#'app.log'
#logging.basicConfig(filename=log_name, filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
#logging.basicConfig(filename=log_name, filemode='a', format='%(message)s',level=logging.DEBUG)
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(filename=log_name, filemode='a', format=FORMAT,level=logging.DEBUG)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logging.warning('This will get logged to a file')
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
logging.debug('test_log '+curDt)