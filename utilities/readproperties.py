import configparser

configuration = configparser.RawConfigParser()
configuration.read("D:\\sql\\s\\2023 May\\OrangeHRM\\.pytest_cache\\Configurations\\config.ini")

class Readconfig():

    @staticmethod
    def geturl():
        url = configuration.get('common info', 'Url')
        return url

    @staticmethod
    def getUsername():
        username = configuration.get('common info', 'Username')
        return username

    @staticmethod
    def getPassword():
        password = configuration.get('common info', 'Password')
        return password

