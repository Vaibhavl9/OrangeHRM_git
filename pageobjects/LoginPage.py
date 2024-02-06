import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class loginpage:

    Text_UserName_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[normalize-space()='Login']")
    Click_Menu_Button_XPATH = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver


    def Enter_UserName(self, UserName):
        self.driver.find_element(*loginpage.Text_UserName_XPATH).send_keys(UserName)

    def Enter_Password(self, Password):
        self.driver.find_element(*loginpage.Text_Password_XPATH).send_keys(Password)

    def Click_Login(self):
        self.driver.find_element(*loginpage.Click_Login_Button_XPATH).click()

    def Click_MenuButton(self):
        self.driver.find_element(*loginpage.Click_Menu_Button_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*loginpage.Click_Logout_XPATH).click()

    def Login_Status(self):
        time.sleep(2)
        try:
            self.driver.find_element(*loginpage.Click_Menu_Button_XPATH)
            return True

        except NoSuchElementException:
            return False
