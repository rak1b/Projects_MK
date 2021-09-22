from POST_AUTOMATION.ADVERT.Data import Data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = Path(__file__).parent.resolve()
import traceback
start_time = time.time()

class DriverControl():
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": Data.IMAGE}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"user-data-dir={Data.CHROME_PROFILE}")
    driver = webdriver.Chrome(executable_path=Data.CHROME_EXECUTABLE_PATH, chrome_options=options)
    driver.maximize_window()

    @classmethod
    def stop_driver(cls):
        # To do the cleanup after test has executed.
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()

    @classmethod
    def goto(self,url=Data.BASE_URL):
        self.driver.get(url)

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

        # this function asserts comparison of a web element's text with passed in text.

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

        # this function performs text entry of the passed in text, in a web element whose locator is passed to it.

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

        # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
        # web element if it is enabled.

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        # this function checks if the web element whose locator has been passed to it, is visible or not and returns
        # true or false depending upon its visibility.

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)



