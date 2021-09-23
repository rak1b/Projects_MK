from selenium.webdriver.common.by import By
class Locator():
    #FIRST PAGE
    CONTACT= (By.ID,'adverts_person')
    EMAIL = (By.ID,'adverts_email')
    TITLE = (By.ID,'post_title')
    PREVIEW = (By.XPATH,'//input[@class="adverts-button adverts-cancel-unload"]')

    #SECOND PAGE
    PUBLISH_LISTING = (By.XPATH,"(//input[@class='adverts-cancel-unload'])[2]")
    # PUBLISH_LISTING = (By.CLASS_NAME,'adverts-cancel-unload[0]')
    #THIRD PAGE
    TITLE_LINK = (By.XPATH,"(//p//a)[1]")

    @classmethod
    def MakeTitleLink(cls,Title):
        cls.TITLE_LINK = (By.LINK_TEXT,Title)


# print(Locator.TITLE_LINK)
# Locator.MakeTitleLink("heres the title")
# print(Locator.TITLE_LINK)

