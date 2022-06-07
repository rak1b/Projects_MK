from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import traceback
from multiprocessing import Process

start_time = time.time()
from pathlib import Path
path = Path(__file__).parent.resolve()
options = Options()
# options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")
driver.maximize_window()

main_url = "https://www.stopthegrind.org"
main_url = "https://www.stmpdxschool.org/"
main_url = "https://www.aptis-translation-interpreting.org/"
url = f"{main_url}/account/my-account"
email = "gycyxape@teleg.eu"
password = "gycyxape@teleg.eu"
my_profile_url =f"{main_url}/profile/{email.split('@')[0]}"

def CheckLogin():
        driver.get(url)

        time.sleep(3)

        login_button = driver.find_element(by=By.XPATH,value="//*[@class='_3VCEv']")
        login_button.click() 
        
        time.sleep(1)

        login_with_email_button = driver.find_element(by=By.XPATH,value="//*[@class='_1fbEI']")
        login_with_email_button.click()
        
        time.sleep(1)

        email_inp = driver.find_element(by=By.XPATH,value='//input[contains(@id,"emailInput")]')
        email_inp.send_keys(email)


        time.sleep(1)
        pas_inp= driver.find_element(by=By.XPATH, value = '//input[contains(@id,"passwordInput")]')
        pas_inp.send_keys(password)

        time.sleep(1)

        login_button = driver.find_element(by=By.XPATH,value="//*[@class='_1fbEI']")
        login_button.click()
        time.sleep(2)



# def tab1():
#         print("-------------------------")
#         print("In tab1")
#         print("-------------------------")
#         # driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         # driver1.get(url1)
        


# def tab2():
#         print("-------------------------")
#         print("In tab2")
#         print("-------------------------")
#         # driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         # driver2.get(url2)

#         # driver.execute_script("window.open('about:blank','secondtab');")
#         # driver.switch_to.window("secondtab")
#         # driver.get(my_profile_url)

  
# if __name__=='__main__':
#     p1 = Process(target = tab1)
#     p1.start()
#     p2 = Process(target = tab2)
#     p2.start()

CheckLogin()

time.sleep(205)
driver.close()