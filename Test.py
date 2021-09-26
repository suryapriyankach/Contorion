from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:/Selenium/Task/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
driver.get("https://www.contorion.de/")
driver.maximize_window()
print(driver.title)
driver.find_element_by_xpath("//button[text()='Alles akzeptieren']").click()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "Anmelden").click()
time.sleep(4)
driver.find_element(By.ID, "login_email").send_keys("priyankarao2691@gmail.com")
time.sleep(4)
driver.find_element_by_xpath("//input[@id='login_password']").click()
driver.find_element_by_xpath("//input[@id='login_password']").send_keys("G@pra060691")
time.sleep(8)
driver.find_element_by_xpath("//button[@class='button button--primary button--large _fit _mt3 lg_c-auto lg_mt0']").click()
msg = driver.find_element(By.TAG_NAME, "body").text

if 'Du bist nun bei Contorion angemeldet' in msg:
    assert True
    print("Login successfull")
else:
    assert False

driver.find_element_by_xpath("//input[@id='search-input']").click()
driver.find_element_by_xpath("//input[@id='search-input']").send_keys("hammer")
driver.find_element(By.XPATH, "//button[@id='search-button']").click()

search = driver.find_element(By.XPATH, "//h2[@class='hidden lg_shown _h1 txt--main _mb2']").text


if 'Suchergebnisse für hammer' in search:
    assert True
    print("Search results for hammer is displayed")
else:
    assert False

'''

driver.find_element(By.ID, 'UserName').send_keys("admin")
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/input[1]").click()
'''
time.sleep(8)

driver.close()
