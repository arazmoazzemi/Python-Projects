https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/

https://pypi.org/project/selenium/


---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

---




pip install selenium
pip install pandas




pip list

pip check

pip show pandas

(venv) C:\> python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt

pip install -r requirements.txt




-------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()
browser.maximize_window()

browser.get('http://192.168.206.4/')

browser.find_element(By.ID, "Username").send_keys(200121)
browser.find_element(By.ID, "Password").send_keys(200121)

browser.find_element(By.CSS_SELECTOR, ".pull-right > .btn").click()
browser.find_element(By.LINK_TEXT, "گزارشات").click()
time.sleep(3)

browser.find_element(By.LINK_TEXT, "گزارشات مرخصی ماموریت").click()
time.sleep(3)

browser.find_element(By.LINK_TEXT, "مانده مرخصی پرسنل").click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, ".btn-success").click()
time.sleep(2)
browser.find_element(By.XPATH, "//td[2]/div/table/tbody/tr/td[2]").click()
time.sleep(2)
browser.find_element(By.XPATH, "//div[5]/table/tbody/tr/td[2]").click()
time.sleep(2)
browser.find_element(By.XPATH, "//div[4]/table/tbody/tr/td/div").click()
time.sleep(2)


browser.close()























