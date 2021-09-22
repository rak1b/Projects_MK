import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
from selenium.webdriver.common.keys import Keys
import traceback
from POST_AUTOMATION.ADVERT.Data import Data as Ad_data
from POST_AUTOMATION.BACKEND.basicOperations import BasePage
from POST_AUTOMATION.BACKEND.DriverControl import DriverControl as DC
from pathlib import Path
from POST_AUTOMATION.BACKEND.Locators.AdvertLocator import Locator

path = Path(__file__).parent.resolve()


class Main(BasePage):
    @staticmethod
    def replace_string(Text, old, new, old2='', new2='', old3='', new3=''):
        Text = Text.replace(old, new)
        Text = Text.replace(old2, new2)
        return Text.replace(old3, new3)

    @classmethod
    def CheckLogin(cls, url, email, passw):
        try:
            cls.driver.get(url)
            cls.driver.find_element_by_id('user_session_email').send_keys(email)
            cls.driver.find_element_by_id('user_session_password').send_keys(passw)
            cls.driver.find_element_by_name('commit').click()
        except:
            print('Already logged in!')

    @classmethod
    def visit_advert_pages(cls):
        DC.enter_text((By.ID,Locator.contact_id),Ad_data.CONTACT_PERSON)

# (By.XPATH, "//p[@id='']")
Main.visit_advert_pages()
