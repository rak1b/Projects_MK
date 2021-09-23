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
from POST_AUTOMATION.BACKEND.Locators.AdvertLocator import Locator as Ad_Locator

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

class Visit_advert_pages():

    @staticmethod
    def first_page():
        DC.goto(Ad_data.BASE_URL)
        DC.enter_text(Ad_Locator.CONTACT, Ad_data.CONTACT_PERSON)
        DC.enter_text(Ad_Locator.EMAIL, Ad_data.EMAIL)
        DC.enter_text(Ad_Locator.TITLE, Ad_data.TITLES[1])
        DC.js_description_post(Ad_data.DESCRIPTION[2])
        DC.click(Ad_Locator.PREVIEW)
        # Ad_Locator.MakeTitleLink(Ad_data.TITLES[1])
    @staticmethod
    def second_page():
        DC.click(Ad_Locator.PUBLISH_LISTING)

    @staticmethod
    def third_page():
        # DC.click(Ad_Locator.TITLE_LINK)
        current_link = DC.Get_link_href(Ad_Locator.TITLE_LINK)
        # return DC.driver.current_url
        return  current_link




Visit_advert_pages.first_page()
Visit_advert_pages.second_page()
print(Visit_advert_pages.third_page())
DC.stop_driver()
