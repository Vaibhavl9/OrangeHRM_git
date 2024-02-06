import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageobjects.AddEmp_Page import AddEmployee
from pageobjects.LoginPage import loginpage
from utilities.Logger import LogGenerator
from utilities.readproperties import Readconfig


class Test_Add_Emp:

    url = Readconfig.geturl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    log = LogGenerator.loggen()

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
        self.ae.Click_PIM()
        self.log.info("Click on PIM")
        self.ae.Click_Add()
        self.log.info("Click on Add")
        self.ae.Enter_FirstName("Vaibhav")
        self.log.info("Entering Firstname")
        self.ae.Enter_MiddleName("M")
        self.log.info("Entering Middlename")
        self.ae.Enter_LastName("L")
        self.log.info("Entering Lastname")
        time.sleep(2)
        self.ae.Click_Save()
        self.log.info("Click on Save")
        time.sleep(2)
        if self.ae.Add_Employee_Status() == True:
            self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_03-pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton")
            self.lp.Click_Logout()
            self.log.info("Click on Logout")
            assert True
            self.log.info("test_addEmp_03 is Passed")
        else:
            self.driver.save_screenshot("D:\\sql\\s\\2023 May\\OrangeHRM\\ScreenShots\\test_Login_02-fail.png")
            self.log.info("test_addEmp_03 is Failed")
            assert False



        self.driver.close()
        self.log.info("test_addEmp_03 is Completed")


      # # driver = webdriver.Firefox()
      # # driver.implicitly_wait(10)
      # # driver.get("https://opensource-demo.orangehrmlive.com/")
      #   self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
      #   self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
      #   self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
      #   self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
      #   self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
      #   self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Naveen")
      #   self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("G")
      #   self.driver.find_element(By.XPATH, "  ").send_keys("T")
      #   time.sleep(2)
      #   self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
      #   print(self.driver.find_element(By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']").text)
      #   try:
      #       self.driver.find_element(By.XPATH,"//h6[normalize-space()='Personal Details']")
      #       print("test_addEmp_02 is Passed")
      #       self.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
      #       self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
      #       assert True
      #   except NoSuchElementException:
      #       print("test_addEmp_02 is Failed")
      #       print("test_addEmp_02 is Completed")
      #       assert False
      #   self.driver.close()
