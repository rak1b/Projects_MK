from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
start_time = time.time()

# email = 'milos.rayn@acelap.com'
# email = 'kadan.seaver@acelap.com'
# email = 'mansoor.avyay@acelap.com'
email = 'brisen.montrey@acelap.com'
passw = 'Rakibrk11'
# url = 'https://www.keliiakina.com/users/event_pages/new?parent_id=150'
# url = 'https://www.okgrassrootsproject.com/users/event_pages/new?parent_id=6'
# url = "https://www.thebullyproject.com/users/event_pages/new?parent_id=2572"
# url = "https://www.europeanmovement.co.uk/users/event_pages/new?parent_id=69"
url = "https://www.parti-socialiste.fr/users/event_pages/new?parent_id=3302"

headline = 'headline'
venue = 'venue'
address1 = 'address1'
address2 = 'address2'
city = 'city'
state = 'state'
zip = '5555'
description = 'description here'

# chrome://version/
options = Options()
# options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
options.add_argument("user-data-dir=C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
# options.add_argument("user-data-dir=C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\new")
driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options)
driver.maximize_window()
driver.get(url)
# driver.get("https://www.thebullyproject.com/users/event_pages/new?parent_id=2572")

def CheckLogin():
    try:
        driver.find_element_by_xpath('//input[@id="user_session_email"]').send_keys(email)
        driver.find_element_by_xpath('//input[@id="user_session_password"]').send_keys(passw)
        driver.find_element_by_xpath('//input[@name="commit"]').click()

    except:
        print('Already logged in!')


def EventPost(headline,venue,address1,address2,city,state,zip,description):
    driver.get(url)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@name="commit"]')))
    _headline = driver.find_element_by_xpath('//input[@id="event_page_page_headline"]').send_keys(headline)
    try:_capacity = driver.find_element_by_xpath('//input[@id="event_page_capacity_count"]').send_keys('10')
    except:pass
    _venue = driver.find_element_by_xpath('//input[@id="event_page_venue_name"]').send_keys(venue)
    _address1 = driver.find_element_by_xpath('//input[@id="event_page_venue_address_address1"]').send_keys(address1)
    _address2 = driver.find_element_by_xpath('//input[@id="event_page_venue_address_address2"]').send_keys(address2)
    _city = driver.find_element_by_xpath('//input[@id="event_page_venue_address_city"]').send_keys(city)
    try:_state = driver.find_element_by_xpath('//input[@id="event_page_venue_address_state"]').send_keys(state)
    except:pass
    _postal_code = driver.find_element_by_xpath('//input[@id="event_page_venue_address_zip"]').send_keys(zip)
    _description_tiny = driver.find_element_by_xpath('//iframe[@id="event_page_content_editable_ifr"]').send_keys(f" {description}")
    _submit = driver.find_element_by_xpath('//input[@name="commit"]').click()
    # time.sleep(2)
    WebDriverWait(driver, 15).until(EC.url_changes(driver.current_url))
    return driver.current_url



CheckLogin()
links = []
for i in range(5):
    event_url = EventPost(headline,venue,address1,address2,city,state,zip,description)
    print(event_url)
    links.append(event_url)

with open('eventLinks.txt', 'w',encoding="utf-8") as file_name:
    for item in links:
        file_name.write(f"{item}\n")
    file_name.close()



print("Time Taken : %s seconds ---" % (time.time() - start_time))
time.sleep(10)
driver.quit()
