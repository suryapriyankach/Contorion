from selenium.webdriver.common.by import By
import time

from pageObject.LoginPage import Login
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()



    def test_homepagetitle(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.maximize_window()

        if act_title== "Contorion: Der smarte Shop fürs Handwerk":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False


    def test_loginSearch(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.click_accept_cookies()
        time.sleep(5)
        self.lp.click_register()
        time.sleep(4)

        self.lp.enter_email(self.username)
        time.sleep(4)
        self.lp.enter_password(self.password)
        time.sleep(8)
        self.lp.click_login()
        time.sleep(8)

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'Du bist nun bei Contorion angemeldet' in self.msg:
            assert True
            print("Login successfull")
        else:
            assert False
        self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")


        self.lp.enter_search("hammer")
        self.lp.click_searchbox()
        time.sleep(4)
        self.search = self.driver.find_element(By.XPATH, "//h2[@class='hidden lg_shown _h1 txt--main _mb2']").text

        if 'Suchergebnisse für hammer' in self.search:
            assert True
            print("Search results for hammer is displayed")
        else:
            assert False
        self.driver.save_screenshot(".\\Screenshots\\" + "Searchresults.png")

        self.driver.close()

