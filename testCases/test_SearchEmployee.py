import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageobjects.AddEmp_Page import AddEmployee
from pageobjects.EmployeeSearchPage import EmployeeSearch
from pageobjects.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_Params:

    url = Readconfig.geturl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    log = LogGenerator.loggen()




    def test_searchEmp_05(self, setup):
        self.log.info("test_searchEmp_05 is Started")
        self.driver = setup
        self.log.info("test_searchEmp_05 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to this URL-->" + self.url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering username-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Click on login button")
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click on PIM")
        self.es = EmployeeSearch(self.driver)
        self.es.Enter_EmpName("Babu")
        self.log.info("Entering Emp Name")
        time.sleep(2)
        self.es.Click_Search_Button()
        self.log.info("Clicking on search button")
        time.sleep(2)
        print(self.es.Search_Result())
        if self.es.Search_Result() == True:
            self.log.info("Search Found")
            self.log.info("test_searchEmp_05 is Passed")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton")
            self.lp.Click_Logout()
            self.log.info("Click on Logout")
            assert True
            self.log.info("test_addEmp_03 is Passed")

        else:
            self.log.info("No Search Found")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton")
            self.lp.Click_Logout()
            self.log.info("Click on Logout")
            self.log.info("test_searchEmp_05 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_searchEmp_05 is Completed")
