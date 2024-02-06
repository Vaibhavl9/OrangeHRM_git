import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageobjects.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login:

    url = Readconfig.geturl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_pageTitle_01(self, setup):
        self.driver = setup
        self.log.info("test_pageTitle_01 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to this url-->"+self.url)
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_pageTitle_01 is pass")
            self.log.info("Page Title is-->"+self.driver.title)
        else:
            self.log.info("test_pageTitle_01 is failed")
            assert False



        self.driver.close()
        self.log.info("test_pageTitle_01 is completed")

    @pytest.mark.sanity
    def test_Login_02(self, setup):
        self.driver = setup
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.get(self.url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_Password(self.password)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Click_Login()
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # try:
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        #     print("test_Login_01 is Passed")
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     assert True
        #
        # except NoSuchElementException:
        #     print("test_Login_01 is Failed")
        #     assert False


        if self.lp.Login_Status() == True:
            self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-pass.png")
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-fail.png")
            assert False

        self.driver.close()

    @pytest.mark.sanity
    def test_addEmp_03(self, setup):
        self.driver = setup
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Naveen")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("G")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("T")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print(self.driver.find_element(By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']").text)
        try:
            self.driver.find_element(By.XPATH,"//h6[normalize-space()='Personal Details']")
            print("test_addEmp_02 is Passed")
            self.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
            self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
            assert True
        except NoSuchElementException:
            print("test_addEmp_02 is Failed")
            print("test_addEmp_02 is Completed")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    def test_addEmp_04(self, setup):
        self.driver = setup
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Naveen")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("G")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
            print("test_addEmp_02 is Passed")
            self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            addemp = True
        except NoSuchElementException:
            print("test_addEmp_02 is Failed")
            print("test_addEmp_02 is Completed")
            addemp = False

        if addemp == True:
            assert True
        else:
            assert False

        self.driver.close()


