import inspect
import logging
class custLogger:
    def customlogger(self, loglevel = logging.WARNING):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        fh = logging.FileHandler("reports/Debug.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger