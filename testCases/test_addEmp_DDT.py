import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageobjects.AddEmp_Page import AddEmployee
from pageobjects.LoginPage import loginpage
from utilities import XLutils
from utilities.Logger import LogGenerator
from utilities.readproperties import Readconfig


class Test_Add_Emp:

    url = Readconfig.geturl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    log = LogGenerator.loggen()
    path = "D:\\sql\\s\\2023 May\\OrangeHRM\\Test Data\\Emplist.xlsx"

    def test_addEmp_03(self, setup):

        self.driver = setup
        self.log.info("test_addEmp_03 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to this Url-->"+self.url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username-->"+self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->"+self.password)
        self.lp.Click_Login()
        self.log.info("Click on login")
        self.ae = AddEmployee(self.driver)



        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)

        self.ae.Click_PIM()
        self.log.info("Click on PIM")
        self.ae.Click_Add()
        self.log.info("Click on Add")
        status_list = []


        for r in range(2, self.rows+1):
            self.FirstName = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)

            time.sleep(2)
            self.ae.Enter_FirstName(self.FirstName)
            self.log.info("Entering Firstname")
            self.ae.Enter_MiddleName(self.MiddleName)
            self.log.info("Entering Middlename")
            self.ae.Enter_LastName(self.LastName)
            self.log.info("Entering Lastname")
            time.sleep(2)
            self.ae.Click_Save()
            self.log.info("Click on Save")
            time.sleep(2)
            if self.ae.Add_Employee_Status() == True:
                self.ae.Click_AddEmpolyee()
                status_list.append("Pass")
                self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_03-pass.png")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Pass")



            else:
                status_list.append("Fail")
                self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-fail.png")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")


        print(status_list)
        time.sleep(2)
        self.lp.Click_MenuButton()
        self.log.info("Click on MenuButton")
        self.lp.Click_Logout()
        self.log.info("Click on Logout")
        if "Fail" not in status_list:
            self.log.info("test_addEmp_03 is Passed")
            assert True
        else:
            self.log.info("test_addEmp_03 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_addEmp_03 is Completed")













