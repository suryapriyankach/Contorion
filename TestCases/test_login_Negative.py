import time

from pageObject.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testdata/Testdata.xlsx"

    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.click_accept_cookies()
        time.sleep(5)
        self.lp.click_register()
        time.sleep(4)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a excel:", self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.enter_email(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            time.sleep(8)
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_loginNegative.png")

            if self.exp=="pass":
                self.driver.close()
                lst_status.append("Pass")
            elif self.exp=="fail":
                lst_status.append("Fail")

        if "fail" not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False








