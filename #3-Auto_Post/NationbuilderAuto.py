from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# email = 'milos.rayn@acelap.com'
email = 'kadan.seaver@acelap.com'
passw = 'Rakibrk11'
# url = 'https://www.keliiakina.com/users/event_pages/new?parent_id=150'
# url = 'https://www.okgrassrootsproject.com/users/event_pages/new?parent_id=6'
url = "https://www.thebullyproject.com/users/event_pages/new?parent_id=2572"
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

try:
    driver.find_element_by_xpath('//input[@id="user_session_email"]').send_keys(email)
    driver.find_element_by_xpath('//input[@id="user_session_password"]').send_keys(passw)
    driver.find_element_by_xpath('//input[@name="commit"]').click()

    driver.get(url)
except:
    print('Already logged in!')


def EventPost(headline,venue,address1,address2,city,state,zip,description):
    driver.implicitly_wait(10)
    _headline = driver.find_element_by_xpath('//input[@id="event_page_page_headline"]').send_keys(headline)
    _capacity = driver.find_element_by_xpath('//input[@id="event_page_capacity_count"]').send_keys('10')
    _venue = driver.find_element_by_xpath('//input[@id="event_page_venue_name"]').send_keys(venue)
    _address1 = driver.find_element_by_xpath('//input[@id="event_page_venue_address_address1"]').send_keys(address1)
    _address2 = driver.find_element_by_xpath('//input[@id="event_page_venue_address_address2"]').send_keys(address2)
    _city = driver.find_element_by_xpath('//input[@id="event_page_venue_address_city"]').send_keys(city)
    _state = driver.find_element_by_xpath('//input[@id="event_page_venue_address_state"]').send_keys(state)
    _postal_code = driver.find_element_by_xpath('//input[@id="event_page_venue_address_zip"]').send_keys(zip)
    _description_tiny = driver.find_element_by_xpath('//iframe[@id="event_page_content_editable_ifr"]').send_keys(f" {description}")
    _submit = driver.find_element_by_xpath('//input[@name="commit"]').click()


EventPost(headline,venue,address1,address2,city,state,zip,description)
print('working')
# driver.get("https://www.google.co.in")
# milos.rayn@acelap.com