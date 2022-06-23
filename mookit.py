from multiprocessing.sharedctypes import Value
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path="F:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://hello.iitk.ac.in/user/login")
# id="edit-name"
username="rudranshg21"
for i in range(0,11):
    driver.find_element(by=By.ID, value="edit-name").send_keys(username[i])
    time.sleep(0.005)
password= "RudranshG@123"
for i in range(0,13):
    driver.find_element(by=By.ID, value="edit-pass").send_keys(password[i])
    time.sleep(0.005)
driver.find_element(by=By.ID, value="edit-submit").send_keys(Keys.RETURN)
time.sleep(0.2)
y = 8
for timer in range(0,70):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 8
    time.sleep(0.005) 
time.sleep(1)
driver.find_element(by= By.XPATH, value= "//a[@href='https://hello.iitk.ac.in/course/mth102aa2122']").click()
time.sleep(1)
driver.find_element(by= By.ID, value="edit-access-course").click()
time.sleep(1)
weeks= driver.find_elements(by=By.CLASS_NAME, value= "weekWrapper")
# print(weeks)
weeks[1].click()
time.sleep(1)
lectures= driver.find_elements(by=By.CLASS_NAME, value="lectureInfoBoxWatched")
lectures[1].click()
time.sleep(5)
speed=driver.find_element(by=By.ID, value="currentSpeed")
hover = ActionChains(driver).move_to_element(speed)
hover.perform()
time.sleep(5)
menu= driver.find_elements(by=By.ID, value= "menuTitle")
# menu[1].click()
print("length" , len(menu))
