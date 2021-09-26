from selenium.webdriver.common.by import By


class Login:
    button_acceptCookies_xpath = "//button[text()='Alles akzeptieren']"
    button_register_link_text = "Anmelden"
    textbox_email_id = "//input[@id='login_email']"
    textbox_Password_xpath = "//input[@id='login_password']"
    button_Register_xpath = "//button[@class='button button--primary button--large _fit _mt3 lg_c-auto lg_mt0']"
    textbox_search_xpath = "//input[@id='search-input']"
    button_searchbox_xpath = "//button[@id='search-button']"


    def __init__(self,driver):
        self.driver = driver

    def click_accept_cookies(self):
        self.driver.find_element(By.XPATH, self.button_acceptCookies_xpath).click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.button_register_link_text).click()

    def enter_email(self, username):
        self.driver.find_element(By.XPATH, self.textbox_email_id).click()
        self.driver.find_element(By.XPATH, self.textbox_email_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_Register_xpath).click()

    def enter_search(self, iphammer):
        self.driver.find_element(By.XPATH, self.textbox_search_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_search_xpath).send_keys(iphammer)

    def click_searchbox(self):
        self.driver.find_element(By.XPATH, self.button_searchbox_xpath).click()


