import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageobjects.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_Params:

    url = Readconfig.geturl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    log = LogGenerator.loggen()




    def test_addEmp_04(self, setup, getDataforlogin):
        self.driver = setup
        self.log.info("test_addEmp_04 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to this URL-->" + self.url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(getDataforlogin[0])
        self.log.info("Entering username-->" + getDataforlogin[0])
        self.lp.Enter_Password(getDataforlogin[1])
        self.log.info("Entering password-->" + getDataforlogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login button")
        if self.lp.Login_Status() == True:
            if getDataforlogin[2] == 'Pass':
                self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")
                self.log.info("test_addEmp_04 is Passed")
                assert True
            else:
                self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-fail.png")
                self.log.info("test_addEmp_04 is Failed")
                assert False
        else:
            if getDataforlogin[2] == 'Fail':
                assert True
            else:
                self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-fail.png")
                self.log.info("test_addEmp_04 is Failed")
                assert False


        self.driver.close()
        self.log.info("test_addEmp_04 is Completed")




