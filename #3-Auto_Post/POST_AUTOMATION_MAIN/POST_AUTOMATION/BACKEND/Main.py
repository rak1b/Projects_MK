import time
import traceback
from POST_AUTOMATION.ADVERT.Data import Ad_data
from POST_AUTOMATION.NATIONBUILDER.Data import  Na_data
from POST_AUTOMATION.BACKEND.basicOperations import BasePage
from POST_AUTOMATION.BACKEND.DriverControl import DriverControl as DC
from POST_AUTOMATION.BACKEND.Locators.AdvertLocator import Locator as Ad_Locator
from POST_AUTOMATION.BACKEND.Locators.NationLocator import Locator as Na_Locator
from pathlib import Path
path = Path(__file__).parent.resolve()
start_time = time.time()

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
    def first_page(title, description):
        DC.goto(Ad_data.BASE_URL)
        DC.enter_text(Ad_Locator.CONTACT, Ad_data.CONTACT_PERSON)
        time.sleep(Ad_data.SLEEP)
        DC.enter_text(Ad_Locator.EMAIL, Ad_data.EMAIL)
        time.sleep(Ad_data.SLEEP)

        DC.enter_text(Ad_Locator.PHONE, Ad_data.PHONE)
        time.sleep(Ad_data.SLEEP)

        DC.enter_text(Ad_Locator.TITLE, title)
        time.sleep(Ad_data.SLEEP)

        DC.js_description_post(description)
        time.sleep(Ad_data.SLEEP)

        DC.enter_text(Ad_Locator.ADDRESS, Ad_data.ADDRESS1)

        try:
            DC.click(Ad_Locator.PREVIEW)
        except:
            # traceback.print_exc()
            print("ERROR!Trying next")
            try:
                DC.click_js(Ad_Locator.PREVIEW_XPATH)
            except:
                pass
        # DC.click_js("(//input[@type='submit' and @name='submit'])[1]")
        # Ad_Locator.MakeTitleLink(Ad_data.TITLES[1])

    @staticmethod
    def second_page():
        try:
            DC.click_js('(//input[@type="submit"])[2]')
        except:
            try:
                DC.click_2(Ad_Locator.PUBLISH_LISTING2, 3)
            except:
                # traceback.print_exc()
                pass
    @staticmethod
    def third_page():
        # DC.click(Ad_Locator.TITLE_LINK)
        current_link = DC.Get_link_href(Ad_Locator.TITLE_LINK)
        # return DC.driver.current_url
        return current_link


class RunAdvert():
    LINK_LIST = []

    @staticmethod
    def replace_string(Text, old, new, old2='', new2='', old3='', new3=''):
        Text = Text.replace(old, new)
        Text = Text.replace(old2, new2)
        return Text.replace(old3, new3)

    @staticmethod
    def loop_data():
        try:
            count = 0
            for team in Ad_data.TEAMS.values():
                for title in Ad_data.TITLES.values():
                    title = RunAdvert.replace_string(title, '[TeamA]', team['TeamA'], '[TeamB]', team['TeamB'])
                    for description in Ad_data.DESCRIPTION.values():
                        LINK = team['LINK']
                        LINK_TEXT = team['LINK_TEXT']
                        # link_html = f'<h2><a href="{visit_url}">{url_text}</a></h2>'
                        description = RunAdvert.replace_string(description, '[TeamA]', team['TeamA'], '[TeamB]',
                                                               team['TeamB'])
                        description = RunAdvert.replace_string(description, '[LINK]', LINK, '[LINK_TEXT]',
                                                               LINK_TEXT)

                        Visit_advert_pages.first_page(title,description)
                        Visit_advert_pages.second_page()
                        RunAdvert.LINK_LIST.append(Visit_advert_pages.third_page())
                        count += 1
                        print(f"{count} Post Completed")

            print("Total Time Taken : %s seconds" % (time.time() - start_time))
        except:
            traceback.print_exc()
            DC.stop_driver()
    @staticmethod
    def write_links(path):
        with(open(path/Ad_data.LINKS_FILE_NAME, 'w', encoding='utf-8'))as file:
            for link in RunAdvert.LINK_LIST:
                file.write(link+'\n')
        file.close()



class NationBuilder():
    @staticmethod
    def CheckLogin():
        try:
            DC.goto(Na_data.BASE_URL)
            DC.enter_text(Na_Locator.EMAIL,Na_data.EMAIL,4)
            DC.enter_text(Na_Locator.PASSWORD,Na_data.PASSWORD,4)
            DC.click(Na_Locator.LOGIN_BUTTON,4)
        except:
            traceback.print_exc()
            print("Allready Logged in")
            print('----OR----')
            print("Provide the Login url")
            pass

    @staticmethod
    def EventPage(title,description):
        DC.goto(Na_data.BASE_URL)
        DC.enter_text(Na_Locator.TITLE,title)
        DC.enter_text(Na_Locator.CONTACT,Na_data.NAME)
        DC.enter_text(Na_Locator.PHONE,Na_data.PHONE)
        DC.enter_text(Na_Locator.VENUE,Na_data.VENUE)
        DC.enter_text(Na_Locator.ADDRESS,Na_data.ADDRESS1)
        DC.enter_text(Na_Locator.CITY,Na_data.CITY)
        DC.js_description_post(description)
        DC.click(Na_Locator.SAVE_BUTTON)

        return DC.NextUrlChanges()

class RunNationBuilder():
    LINK_LIST = []

    @staticmethod
    def replace_string(Text, old, new, old2='', new2='', old3='', new3=''):
        Text = Text.replace(old, new)
        Text = Text.replace(old2, new2)
        return Text.replace(old3, new3)

    @staticmethod
    def loop_data():
        try:
            count = 0
            for team in Na_data.TEAMS.values():
                for title in Na_data.TITLES.values():
                    title = RunNationBuilder.replace_string(title, '[TeamA]', team['TeamA'], '[TeamB]', team['TeamB'])
                    for description in Na_data.DESCRIPTION.values():
                        LINK = team['LINK']
                        LINK_TEXT = team['LINK_TEXT']
                        # link_html = f'<h2><a href="{visit_url}">{url_text}</a></h2>'
                        description = RunAdvert.replace_string(description, '[TeamA]', team['TeamA'], '[TeamB]',
                                                               team['TeamB'])
                        description = RunAdvert.replace_string(description, '[LINK]', LINK, '[LINK_TEXT]',
                                                               LINK_TEXT)

                        RunAdvert.LINK_LIST.append(NationBuilder.EventPage(title,description))
                        count += 1
                        print(f"{count} Post Completed")

            print("Total Time Taken : %s seconds" % (time.time() - start_time))
        except:
            traceback.print_exc()
            DC.stop_driver()
    @staticmethod
    def write_links(path):
        with(open(path/Ad_data.LINKS_FILE_NAME, 'w', encoding='utf-8'))as file:
            for link in RunAdvert.LINK_LIST:
                file.write(link+'\n')
        file.close()


def Final_advert_run(path):
    try:
        RunAdvert.loop_data()
        RunAdvert.write_links(path)
        DC.stop_driver()
    except:
        DC.stop_driver()
        traceback.print_exc()



def Final_NationBuilder_run(path):
    try:
        NationBuilder.CheckLogin()
        RunNationBuilder.loop_data()
        RunNationBuilder.write_links(path)
        DC.stop_driver()
    except:
        DC.stop_driver()
        traceback.print_exc()

