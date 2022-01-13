import configparser
import signal
from sys import argv
import logging

log_level_number=1
logging.getLogger().setLevel(logging.INFO)

if '--warning' in argv:
    logging.getLogger().setLevel(logging.WARNING)

def signal_handler(signal, frame):
        global log_level_number
        log_level_number+=1

        if log_level_number>3:
             log_level_number=1

        if log_level_number==1:
            logging.getLogger().setLevel(logging.INFO)
            logging.info("Log Level Set To info")

        elif log_level_number==2:
            logging.getLogger().setLevel(logging.WARNING)
            logging.warning("Log Level Set To warning")

        elif log_level_number==3:
            logging.getLogger().setLevel(logging.CRITICAL)
            logging.critical("Log Level Set To critical")


def print_name():
    try:
         config = configparser.ConfigParser()
         config.read('config.ini')
         a=config['Names']
         if "MiddleName" not in a:
             logging.warning("MiddleName doesn't exist in config file")
             logging.info('Hi'+ ' '+a['Firstname']+' '+a['LastName'])
         else:
              logging.info('Hi'+ ' '+a['Firstname']+' '+a['MiddleName']+' '+a['LastName'])



    except Exception as e:
         logging.critical("can't open config file!")


def alarm_handler(signum, frame):
    print_name();

signal.signal(signal.SIGALRM, alarm_handler)
signal.signal(signal.SIGINT,signal_handler)

while True:
    signal.alarm(10)
    signal.pause()
