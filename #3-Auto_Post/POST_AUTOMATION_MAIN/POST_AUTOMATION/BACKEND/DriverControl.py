from POST_AUTOMATION.ADVERT.Data import Ad_data
from POST_AUTOMATION.NATIONBUILDER.Data import Na_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = Path(__file__).parent.resolve()
import traceback
start_time = time.time()
from selenium.webdriver.common.by import By
class DriverControl():
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": Ad_data.IMAGE}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"user-data-dir={Ad_data.CHROME_PROFILE}")
    driver = webdriver.Chrome(executable_path=Ad_data.CHROME_EXECUTABLE_PATH, chrome_options=options)
    driver.maximize_window()

    @classmethod
    def stop_driver(cls):
        # To do the cleanup after test has executed.
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()

    @staticmethod
    def goto(url):
        DriverControl.driver.get(url)

    @staticmethod
    def click(by_locator):
        WebDriverWait(DriverControl.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    @staticmethod
    def click_2(by_locator,time):
        WebDriverWait(DriverControl.driver, time).until(EC.element_to_be_clickable(by_locator)).click()
    @staticmethod
    def click_js(xpath):
        element = DriverControl.driver.find_element_by_xpath(xpath)
        DriverControl.driver.execute_script("arguments[0].click();", element)
        # this function asserts comparison of a web element's text with passed in text.

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    @staticmethod
    def NextUrlChanges():
        WebDriverWait(DriverControl.driver, 15).until(EC.url_changes(DriverControl.driver.current_url))
        return DriverControl.driver.current_url

    @staticmethod
    def Get_link_href(by_locator):
        for a in DriverControl.driver.find_elements(By.XPATH,"(//p//a)[1]"):
            return a.get_attribute('href')
        # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    @staticmethod
    def enter_text(by_locator, text,time=10):
        return WebDriverWait(DriverControl.driver, time).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

        # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
        # web element if it is enabled.

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        # this function checks if the web element whose locator has been passed to it, is visible or not and returns
        # true or false depending upon its visibility.

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    @staticmethod
    def js_description_post(description):
        description = DriverControl.driver.execute_script(f'tinyMCE.activeEditor.setContent(`{description}`)')




