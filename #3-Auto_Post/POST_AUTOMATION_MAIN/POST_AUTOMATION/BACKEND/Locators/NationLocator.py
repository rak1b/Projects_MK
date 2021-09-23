from selenium.webdriver.common.by import By
class Locator():
    #LOGIN
    EMAIL = (By.ID,'user_session_email')
    PASSWORD=(By.ID,'user_session_password')
    LOGIN_BUTTON = (By.XPATH,"(//input[@name='commit'])[1]")


    #FIRST PAGE
    TITLE = (By.ID,'event_page_page_headline')
    CONTACT= (By.ID,"event_page_contact_name")
    PHONE=(By.ID,"event_page_contact_phone_number")
    VENUE = (By.ID,"event_page_venue_name")
    ADDRESS=(By.ID,"event_page_venue_name")
    CITY= (By.ID,"event_page_venue_address_city")
    SAVE_BUTTON= (By.NAME,"commit")
    #SECOND PAGE

    #THIRD PAGE
    TITLE_LINK = (By.XPATH,"(//p//a)[1]")

