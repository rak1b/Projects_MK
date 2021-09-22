import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
from selenium.webdriver.common.keys import Keys
import traceback
from pathlib import Path
path = Path(__file__).parent.resolve()
from By_Oop.InputData import Data
class DriverControl():
    def setUp(self):
        # Setting up how we want Chrome to run
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(Data.CHROME_EXECUTABLE_PATH, options=chrome_options)

        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()


class AutoPost():
    chrome_profile = 'C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1'
    chrome_driver_path = r'C:\chromedriver\chromedriver.exe'
    number_of_image = 4
    linksFile = 'EventLinksN.txt'
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 5}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"user-data-dir={self.profile}")
    driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
    driver.maximize_window()
    def __init__(self,url,username=None,password=None,profile=chrome_profile,driver_path=chrome_driver_path,image=number_of_image,links_file_name=linksFile):
        self.profile = profile
        self.driver_path=driver_path
        self.image = image
        self.links_file_name = links_file_name
        self.username = username
        self.password = password
        self.url = url


    def go_url(self):
        driver = AutoPost.dr

    def details(self):
        print(f'Profile:{self.profile}\driver_path={self.driver_path}\nimage={self.image}\nfile_name={self.links_file_name}\nurl={self.url}')


n = AutoPost(url='youtube.com')
n.go_url()