import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageobjects.LoginPage import loginpage
from utilities import XLutils
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_ddt:
    url = Readconfig.geturl()

    log = LogGenerator.loggen()
    path = "D:\\sql\\s\\2023 May\\OrangeHRM\\Test Data\\LoginTest.xlsx"

    def test_login_ddt_06(self, setup):
        self.driver = setup
        self.log.info("test_login_ddt_06 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to this URL-->" + self.url)
        self.lp = loginpage(self.driver)
        self.rows = XLutils.getrowCount(self.path, "Sheet1")
        print("Number of rows are --->", self.rows)
        login_status = []
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.Enter_UserName(self.username)
            self.log.info("Entering username-->" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering password-->" + self.username)

            self.lp.Click_Login()
            self.log.info("Click on login button")
            if self.lp.Login_Status() == True:
                self.driver.save_screenshot(
                    "D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\" + self.username + self.password + "test_Login_02-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")
                login_status.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")



            else:
                login_status.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                self.driver.save_screenshot(
                    "D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\" + self.username + self.password + "test_Login_02-fail.png")

        print(login_status)
        if "Fail" not in login_status:
            assert True
        else:
            assert False

        self.driver.close()
        self.log.info("test_login_ddt_06 is Completed")
