import logging

class LogGenerator:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logfile = logging.FileHandler("D:\\sql\\s\\2023 May\\OrangeHRM\\Log\\OrangeHRM_Automation")
        format = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s :")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger










# get log --> logging.getLogger()
# logfile --> path and name
# format --> logs format
# setFormatter --> link file and format
# addhaldler --> maintain --> log file