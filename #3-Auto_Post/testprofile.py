from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
email = 'milos.rayn@acelap.com'
passw = 'Rakibrk11'
# url = 'https://www.keliiakina.com/users/event_pages/new?parent_id=150'
url = "https://www.thebullyproject.com/users/event_pages/new?parent_id=2572"

# chrome://version/
options = Options()
# options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
options.add_argument("user-data-dir=C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
# options.add_argument("user-data-dir=C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\new")
driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options)
driver.maximize_window()
driver.get(url)
# driver.get("https://www.thebullyproject.com/users/event_pages/new?parent_id=2572")
time.sleep(3)
try:
    driver.find_element_by_xpath('//input[@id="user_session_email"]').send_keys(email)
    driver.find_element_by_xpath('//input[@id="user_session_password"]').send_keys(passw)
    driver.find_element_by_xpath('//input[@name="commit"]').click()
    time.sleep(2)
    driver.get(url)
except:
    print('Already logged in!')
    pass




# driver.get("https://www.google.co.in")
# milos.rayn@acelap.com