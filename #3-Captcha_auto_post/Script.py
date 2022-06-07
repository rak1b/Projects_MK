from pathlib import Path
from multiprocessing.connection import wait
from turtle import update
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
import json
from selenium.webdriver.common.keys import Keys
import pyperclip as pc
import re
import random
import string
from time import sleep

your_pc_user_name = "mdrak"
path = Path(__file__).parent.resolve()
chrome_profile = f'C:\\Users\\{your_pc_user_name}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 10'

options = Options()
options.add_argument(f"user-data-dir={chrome_profile}")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")
driver.maximize_window()
url_list = []
# BASE_URL = "https://www.stopthegrind.org"
# BASE_URL = "https://www.stmpdxschool.org/"
# BASE_URL = "https://www.aptis-translation-interpreting.org/"
email = "mrxoiffsxalqfqeeua@kvhrr.com"
password = "mrxoiffsxalqfqeeua@kvhrr.com"

# my_profile_url = f"{BASE_URL}/profile/{email.split('@')[0]}"


heading_text = "[ONLINE] [TeamA] [TeamB] [HEADING_TAIL] [LIVESTREAM_WORDS]Live Stream NCAA Collage Football 02 September 2021 Full HD Coverage"
heading_tail_list = ['Live Stream', 'Game live',
                     'Op game', 'Live Reddit ', 'Live Free On Tv']
livestream_word_list = ['livestream', 'Live Hd', 'Add more here']

# Second Heading
# second_heading_text=''
second_heading_text = "Welcome To Watch [TeamA] vs. [TeamB]: [SECOND_HEADING_TAIL] [SECOND_LIVESTREAM_WORDS] How to live stream, TV channel, start time for Thursday's NCAA Football game. How to watch [TeamA] vs. [TeamB] football game"
second_heading_tail_list = ['Live Stream', 'Game live',
                            'Op game', 'Live Reddit ', 'Live Free On Tv']
second_livestream_word_list = ['skksk', 'Live Hd', 'Add more here']


PostInfo = {
    1: {
        'TeamA': "Germany vs",
        'TeamB': "Italy",
        'description': '''Enter Your description Here''',
        'url': "https://www.thingstodocincinnati.com",

        'FIRST_LINE': 'Hello',
        'MIDDLE_LINE': 'Welcome',
        'LAST_LINE': 'Bye',
    },

    2: {
        'TeamA': "France v",
        'TeamB': "Norway",
        'description': '''''',
        'url': "https://www.lomaseca.com",
        'FIRST_LINE': '--one--',
        'MIDDLE_LINE': '--two===',
        'LAST_LINE': '--three--',
    },  3: {
        'TeamA': "France v",
        'TeamB': "Norway",
        'description': '''''',
        'url': 'https://www.stmpdxschool.org',
        'FIRST_LINE': '--one--',
        'MIDDLE_LINE': '--two===',
        'LAST_LINE': '--three--',
    },
}


description_first_list = [
    'First line 1',
    'First line 2',
    'First line 3',
    'First line 4',
    'First line 5',
]

description_middle_list = [
    'MIDDLE line 1',
    'MIDDLE line 2',
    'MIDDLE line 3',
    'MIDDLE line 4',
    'MIDDLE line 5',
]

description_end_list = [
    'end line 1',
    'end line 2',
    'end line 3',
    'end line 4',
    'end line 5',
]


description_text = '''[FIRST_LINE]
Watch [TeamA] vs. [TeamB]: How to live stream, TV channel, start time for Thursday's NCAA Football game
How to watch [TeamA] vs. [TeamB] football game
Who's Playing
[TeamB] @ [TeamA]

Last Season Records: [TeamA] 0-6; [TeamB] 5-2

What to Know
The [TeamA] Rebels will play against a Division II opponent, the [TeamB] Eagles, in an early-season tune-up Thursday at 10 p.m. ET at Allegiant Stadium. Coming off of an uninspired 0-6 last-season record, the Rebels have set their aspirations higher this year.

The neutral point spread forecasts a close one for these two. We'll see if the game is as close as the oddsmakers expect or if one of these teams has a surprise blowout in them.

How To Watch
When: Thursday at 10 p.m. ET
Where: Allegiant Stadium -- Paradise, Nevada
TV: STADIUM
Follow: CBS Sports App
Ticket Cost: $15.00
Odds
The Rebels are a slight 2-point favorite against the Eagles, according to the latest college football odds.


[MIDDLE_LINE]



The oddsmakers had a good feel for the line for this one, as the game opened with the Rebels as a 3-point favorite.

Over/Under: -110

See college football picks for every single game, including this one, from SportsLine's advanced computer model. Get picks now.

Series History
This is the first time these teams have played each other within the last six years.

How to Watch [TeamB] Eagles  at [TeamA] Rebels: Live Stream, TV Channel, Start Time
[TeamA] looks to pick up its first win in two years when it hosts [TeamB] in the season opener Thursday night.

[TeamA] made a splash by signing transfer Tate Martell right before school started, but in a mild surprise, he was nowhere to be found when the Rebels released their depth chart. The Rebels, who have not won a game since 2019, need a spark and many thought he would be it. Instead, they will wait for him to play quarterback at least another week.

How to Watch:

Date: Sept. 2, 2021

Time: 10:00 p.m. ET

TV: Stadium

You can stream the game on fuboTV: Start with a 7-day free trial!

[TeamA] has a rough start to its schedule, and if it can't find a way to beat [TeamB], it could be a while before the Rebels win. After their opening game, they travel to No. 25 Arizona State before hosting Iowa State. They are going to be huge underdogs in those games, so they need to find a way to beat the Eagles.

[TeamB] went 5-2 in the spring of 2021 after the fall schedule was postponed due to COVID-19. The Eagles lost to North Dakota State in the first round of the playoffs after losing just one game in the regular season.

The Eagles are not going to be an easy game for the Rebels, and if you are looking for an FCS team to upset an FBS team this would be the game to watch. The Rebels haven't had a winning season since 2013 and have had a hard time winning even four games in a year. [TeamB] will give them everything they can handle and could easily win this game.

[LAST_LINE]

'''
 

 

def CheckLogin(url):
    url = f"{url}/account/my-account"

    driver.get(url)
    try:
        time.sleep(3)

        login_button = driver.find_element(
            by=By.XPATH, value="//*[@class='_3VCEv']")
        login_button.click()

        time.sleep(1)

        login_with_email_button = driver.find_element(
            by=By.XPATH, value="//*[@class='_1fbEI']")
        login_with_email_button.click()

        time.sleep(1)

        email_inp = driver.find_element(
            by=By.XPATH, value='//input[contains(@id,"emailInput")]')
        email_inp.send_keys(email)

        time.sleep(1)
        pas_inp = driver.find_element(
            by=By.XPATH, value='//input[contains(@id,"passwordInput")]')
        pas_inp.send_keys(password)

        time.sleep(1)

        login_button = driver.find_element(
            by=By.XPATH, value="//*[@class='_1fbEI']")
        login_button.click()
        time.sleep(2)
    except:
        print(traceback.format_exc())

        pass


def update_profile(username):
    #     profile_name_input = driver.find_element(by=By.ID, value="display-name-id")
    try:
        time.sleep(1)
        profile_name_input = driver.find_element(
            by=By.ID, value="display-name-id")
        profile_name_input.click()
        driver.execute_script(
            f"document.getElementById('display-name-id').value=''")
        profile_name_input.send_keys(username)

        profile_update = driver.find_element(
            by=By.XPATH, value="(//button[@data-hook='MyAccount-saveAccountButton'])[2]//span")
        profile_update.click()
        sleep(3)
    except:
        print(traceback.format_exc())

        pass
    


def edit_profile_url(username):
    print("_____________________")
    print(username)
    print("_____________________")
    try:
        time.sleep(1)
        url_update_open = driver.find_element(
            by=By.XPATH, value="(//div[@class='s3Tfmf'])[1]")
        url_update_open.click()
        time.sleep(1)

        url_edit_btn = driver.find_element(
            by=By.XPATH, value="//span[text()='Edit URL']")
        url_edit_btn.click()
        time.sleep(1)

        url_submit_input = driver.find_element(
            by=By.XPATH, value="//input[contains(@id,'label-for-id')]")
        url_submit_input.click()
        time.sleep(2)

        driver.execute_script(
            f"document.querySelector('[id^=label-for-id]').value=''")
        time.sleep(2)

       

        url_submit_input.send_keys(username)
        time.sleep(1)
        url_save = driver.find_element(
            by=By.XPATH, value="//button//span[text()='Save']")
        url_save.click()
        sleep(3)
    except:
        print(traceback.format_exc())
        pass



def edit_about(username,description,url):
    try:
        sleep(1)
        driver.get(f"{url}/profile/{username}/profile")
        # open_edit = driver.find_element(by=By.XPATH, value="//div[@data-hook='Profile-AboutOverlay']")
        sleep(3)
        open_edit = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-hook='Profile-AboutOverlay']"))
            )
        sleep(1)

        open_edit.click()
        sleep(2)

    

        input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
        )

        input.send_keys(Keys.CONTROL, 'a')  
        input.send_keys(Keys.CONTROL, 'x')
        pc.copy(description) 
        input.send_keys(Keys.CONTROL, 'v')
        sleep(0.5)
        driver.find_element(by=By.XPATH, value="//button[@data-hook='InputDialog-primaryButton']").click()
    except:
        print(traceback.format_exc())

        pass

    

    # driver.execute_script(
    #         f'''document.getElementsByClassName("public-DraftStyleDefault-block public-DraftStyleDefault-ltr")[0].innerHTML = "<h2>Hello</h2>" ''')


def random_string(onlyString, no_of_string):
    if onlyString:
        return ''.join(random.choice(string.ascii_lowercase) for i in range(int(no_of_string)))
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(int(no_of_string)))




def make_description(description, post_no, teamA, teamB):
    if '[FIRST_LINE]' in description:
        if len(PostInfo[post_no]['FIRST_LINE']) == 0:
            description = description.replace(
                '[FIRST_LINE]', random.choice(description_first_list), 1)
        else:
            description = description.replace(
                '[FIRST_LINE]', PostInfo[post_no]['FIRST_LINE'], 1)

    if '[LAST_LINE]' in description:
        if len(PostInfo[post_no]['LAST_LINE']) == 0:
            description = description.replace(
                '[LAST_LINE]', random.choice(description_end_list), 1)
        else:
            description = description.replace(
                '[LAST_LINE]', PostInfo[post_no]['LAST_LINE'], 1)
    if '[MIDDLE_LINE]' in description:
        if len(PostInfo[post_no]['MIDDLE_LINE']) == 0:
            description = description.replace(
                '[MIDDLE_LINE]', random.choice(description_end_list), 1)
        else:
            description = description.replace(
                '[MIDDLE_LINE]', PostInfo[post_no]['MIDDLE_LINE'], 1)
    if '[TeamA]' in description:
        description = description.replace('[TeamA]', teamA)
    if '[TeamB]' in description:
        description = description.replace('[TeamB]', teamB)
    return description


def make_heading(heading, teamA, teamB):
    if '[HEADING_TAIL]' in heading:
        heading = heading.replace(
            '[HEADING_TAIL]', random.choice(heading_tail_list), 1)
    if '[LIVESTREAM_WORDS]' in heading:
        heading = heading.replace(
            '[LIVESTREAM_WORDS]', random.choice(livestream_word_list), 1)
    if '[TeamA]' in heading:
        heading = heading.replace('[TeamA]', teamA)
    if '[TeamB]' in heading:
        heading = heading.replace('[TeamB]', teamB)
    return heading


def make_second_heading(heading, teamA, teamB):
    if '[SECOND_HEADING_TAIL]' in heading:
        heading = heading.replace(
            '[SECOND_HEADING_TAIL]', random.choice(second_heading_tail_list), 1)
    if '[SECOND_LIVESTREAM_WORDS]' in heading:
        heading = heading.replace(
            '[SECOND_LIVESTREAM_WORDS]', random.choice(second_livestream_word_list), 1)
    if '[TeamA]' in heading:
        heading = heading.replace('[TeamA]', teamA)
    if '[TeamB]' in heading:
        heading = heading.replace('[TeamB]', teamB)
    return heading


for i in range(1,len(PostInfo)+1):
    TeamA = PostInfo[i]['TeamA']
    TeamB = PostInfo[i]['TeamB']
    URL = PostInfo[i]['url']
    username =  make_heading(heading_text,TeamA,TeamB)
    username = username.replace(" ","-").replace("[","").replace("]","")[0:250]
    profile_url = URL+"/profile/"+username+"/profile"
    url_list.append(profile_url)
    description = make_description(description_text,1,TeamA,TeamB)
    CheckLogin(URL)
    update_profile(username)
    edit_profile_url(username)
    edit_about(username,description,URL)

# jsonString = json.dumps(url_list)
# jsonFile = open("status.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()
with open('links.json', 'w', encoding='utf-8') as f:
    json.dump(url_list, f, ensure_ascii=False, indent=4)
time.sleep(20)
driver.close()
