from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
from selenium.webdriver.common.keys import Keys
start_time = time.time()
# pip install pyperclip,selenium

# email = 'milos.rayn@acelap.com'
# email = 'kadan.seaver@acelap.com'
# email = 'mansoor.avyay@acelap.com'
email = 'brisen.montrey@acelap.com'
passw = 'Rakibrk11'
# url = 'https://www.keliiakina.com/users/event_pages/new?parent_id=150'
url = 'https://www.okgrassrootsproject.com/users/event_pages/new?parent_id=6'
# url = "https://www.thebullyproject.com/users/event_pages/new?parent_id=2572"
# url = "https://www.europeanmovement.co.uk/users/event_pages/new?parent_id=69"
# url = "https://www.parti-socialiste.fr/users/event_pages/new?parent_id=3302"

headline = 'headline'
venue = 'venue'
address1 = 'address1'
address2 = 'address2'
city = 'city'
state = 'state'
zip = '5555'

TeamA = 'Brazil'
TeamB = 'Argentina'

titles = {
    1: f'[HD]{TeamA} vs {TeamB} Live Stream',
    2: f'[ONLINE]{TeamB} vs {TeamA} Live Stream',
    3: f'[NCAA]{TeamA} vs {TeamB} Live Online',
    4: f'[WATCH]{TeamB} vs {TeamA} Live Online',
    5: f'[LIVE]{TeamA} vs {TeamB} Live Free',
    6: f'[ITV]{TeamB} vs {TeamA} Live Free',
    7: f'[STREAMING]{TeamA} vs {TeamB} Live',
    8: f'[FREE]>>>{TeamB} vs {TeamA} Live',
    9: f'[HDQ]{TeamA} vs {TeamB} 2021 Live',
    10: f'[GAME]>>>{TeamB} vs {TeamA} 2021 Live',
}

descriptions = {

    1: f'''NFL Week 2 – {TeamA} vs {TeamB} Live Preview & Prediction
{TeamA} vs {TeamB} Live kick-off time, TV channel, live stream info and team news
{TeamA} vs {TeamB} Live free live stream and how to watch the NFL Week 2
Live NFL Week 2: {TeamA} vs {TeamB} Live as McKenzie earns rare start at 10
Lavonte David was fined for this non-called penalty so the {TeamA} vs {TeamB} Live will feel like justice has been served, but this potentially swung the game (obviously we are using some hindsight to come to that conclusion). How is that fair?
4. A quick note regarding the “third-and-long” measure as a litmus test for the franchise-iness of a quarterback: In 2019, the Cowboys led the {TeamA} vs {TeamB} Live in third-and-6+ conversion rate (34.5%). In 2020, with Dak Prescott missing two thirds of the season, they fell to dead last (18.8%). In last Thursday’s opener, they went a respectable 2-for-6 (33.3%) against the Bucs.
Potential fits likely dwindled based on Sherman being charged in July with five misdemeanors of driving under the i{TeamA} vs {TeamB} Liveuence, reckless endangerment of roadway workers, criminal trespass in the second degree (domestic violence designation), resisting arrest and malicious mischief in the third degree (domestic violence designation). 
After posting 13 touchdown catches in 2015 and earning a Pro Bowl nod, Eifert suffered through three injury-plagued seasons before bouncing back and playing 16 games in 2019. He signed a two-year, free-agent deal with the {TeamA} the following offseason.
It’s what happened on the third down play, rather after it, that many people were upset by. Dak Prescott’s pass should have been intercepted by Lavonte David and David was so upset that it wasn’t that he slammed his helmet down on the field in frustration. That is a clear and obvious unsportsmanlike conduct penalty.
The Minnesota Vikings signed running back Ameer Abdullah to the active roster. Safety Myles Dorn and quarterback Sean Mannion have been elevated to the active roster for Sunday's game.
Last week I tried to focus on games where the mismatch in the trenches looked the most acute and this is another example. Zach Wilson is going to see some looks that will confuse him. The chasm in experience and accomplishment between the Denver staff and the Jaguars staff is massive at this point. Belichick will have the Broncos prepared as if this is a playoff game because he knows starting 0-2 and, in particular, starting 0-2 against divisional opponents that he feels he should beat, could end up damning their season.
Pittsburgh Steelers receiver Chase Claypool was fined $8,354 for unsportsmanlike conduct in an early dustup against the Bills, Pelissero reported.
MINNESOTA VIKINGS at ARIZONA CARDINALS: The Cardinals are a bigger threat to the Eagles in the NFC than Kirk Cousins’s Vikings are. Root for the Vikings.
Dr. Allen Sills, the league’s chief medical officer, said almost all cases across have been the Delta variant. He said vaccinated individuals have had very mild upper respiratory illness, shorter duration. Sills also said none of the players who’ve tested positive required hospitalization.
You can boil down why the Cowboys lost the game to a few moments. Some people would look to the short missed field goal and extra point from Greg Zuerlein. Others might talk about the quick Antonio Brown touchdown at the end of the first half. But one moment it seems just about everybody would focus on came on the Cowboys’ penultimate possession of the first half.
\"The biggest factor was, I had to think about my career,\" Brown said after agreeing to terms, per Pro Football Talk's Myles Simmons. \"I actually turned down more money to come here. I felt like it was the best decision for my career, so I had to put everything else aside and had to try to decide what would make me happy at the end of the day.\"
KANSAS CITY CHIEFS at BALTIMORE RAVENS: We know the Chiefs will make the playoffs even if they lose this game. But things won’t be looking good for Baltimore if they drop to 0-2. Better for the Ravens to push a playoff spot that could keep Miami and/or Indy out of the mix. Root for the Ravens.
Even when the Ravens roster has been at full strength in recent years, the Chiefs have been their Kryptonite. Last year in prime time, Kansas City came into Baltimore and whacked the Ravens for four quarters. That, of course, was without fans and it will be crazy in Baltimore on Sunday night, but this is also not the Ravens team we have become accustomed to. 
\"The biggest factor was, I had to think about my career,\" Brown said after agreeing to terms, per Pro Football Talk's Myles Simmons. \"I actually turned down more money to come here. I felt like it was the best decision for my career, so I had to put everything else aside and had to try to decide what would make me happy at the end of the day.\"
That's Will Brinson, highlighting Buffalo's defense as a big reason he likes the Bills to bounce back in a big way against their AFC East rivals. Check out Brinson's full rundown of Week 2 picks and best bets, which includes some free props, for more of his projections.
''',

2 : f'''NFL Week 2 – {TeamA} vs {TeamB} Live Preview & Prediction
{TeamA} vs {TeamB} Live kick-off time, TV channel, live stream info and team news
{TeamA} vs {TeamB} Live free live stream and how to watch the NFL Week 2
Live NFL Week 2: {TeamA} vs {TeamB} Live as McKenzie earns rare start at 10
Lavonte David was fined for this non-called penalty so the {TeamA} vs {TeamB} Live will feel like justice has been served, but this potentially swung the game (obviously we are using some hindsight to come to that conclusion). How is that fair?
4. A quick note regarding the “third-and-long” measure as a litmus test for the franchise-iness of a quarterback: In 2019, the Cowboys led the {TeamA} vs {TeamB} Live in third-and-6+ conversion rate (34.5%). In 2020, with Dak Prescott missing two thirds of the season, they fell to dead last (18.8%). In last Thursday’s opener, they went a respectable 2-for-6 (33.3%) against the Bucs.
Potential fits likely dwindled based on Sherman being charged in July with five misdemeanors of driving under the i{TeamA} vs {TeamB} Liveuence, reckless endangerment of roadway workers, criminal trespass in the second degree (domestic violence designation), resisting arrest and malicious mischief in the third degree (domestic violence designation). 
After posting 13 touchdown catches in 2015 and earning a Pro Bowl nod, Eifert suffered through three injury-plagued seasons before bouncing back and playing 16 games in 2019. He signed a two-year, free-agent deal with the {TeamA} the following offseason.
It’s what happened on the third down play, rather after it, that many people were upset by. Dak Prescott’s pass should have been intercepted by Lavonte David and David was so upset that it wasn’t that he slammed his helmet down on the field in frustration. That is a clear and obvious unsportsmanlike conduct penalty.
The Minnesota Vikings signed running back Ameer Abdullah to the active roster. Safety Myles Dorn and quarterback Sean Mannion have been elevated to the active roster for Sunday's game.
Last week I tried to focus on games where the mismatch in the trenches looked the most acute and this is another example. Zach Wilson is going to see some looks that will confuse him. The chasm in experience and accomplishment between the Denver staff and the Jaguars staff is massive at this point. Belichick will have the Broncos prepared as if this is a playoff game because he knows starting 0-2 and, in particular, starting 0-2 against divisional opponents that he feels he should beat, could end up damning their season.
Pittsburgh Steelers receiver Chase Claypool was fined $8,354 for unsportsmanlike conduct in an early dustup against the Bills, Pelissero reported.
MINNESOTA VIKINGS at ARIZONA CARDINALS: The Cardinals are a bigger threat to the Eagles in the NFC than Kirk Cousins’s Vikings are. Root for the Vikings.
Dr. Allen Sills, the league’s chief medical officer, said almost all cases across have been the Delta variant. He said vaccinated individuals have had very mild upper respiratory illness, shorter duration. Sills also said none of the players who’ve tested positive required hospitalization.
You can boil down why the Cowboys lost the game to a few moments. Some people would look to the short missed field goal and extra point from Greg Zuerlein. Others might talk about the quick Antonio Brown touchdown at the end of the first half. But one moment it seems just about everybody would focus on came on the Cowboys’ penultimate possession of the first half.
\"The biggest factor was, I had to think about my career,\" Brown said after agreeing to terms, per Pro Football Talk's Myles Simmons. \"I actually turned down more money to come here. I felt like it was the best decision for my career, so I had to put everything else aside and had to try to decide what would make me happy at the end of the day.\"
KANSAS CITY CHIEFS at BALTIMORE RAVENS: We know the Chiefs will make the playoffs even if they lose this game. But things won’t be looking good for Baltimore if they drop to 0-2. Better for the Ravens to push a playoff spot that could keep Miami and/or Indy out of the mix. Root for the Ravens.
Even when the Ravens roster has been at full strength in recent years, the Chiefs have been their Kryptonite. Last year in prime time, Kansas City came into Baltimore and whacked the Ravens for four quarters. That, of course, was without fans and it will be crazy in Baltimore on Sunday night, but this is also not the Ravens team we have become accustomed to. 
\"The biggest factor was, I had to think about my career,\" Brown said after agreeing to terms, per Pro Football Talk's Myles Simmons. \"I actually turned down more money to come here. I felt like it was the best decision for my career, so I had to put everything else aside and had to try to decide what would make me happy at the end of the day.\"
That's Will Brinson, highlighting Buffalo's defense as a big reason he likes the Bills to bounce back in a big way against their AFC East rivals. Check out Brinson's full rundown of Week 2 picks and best bets, which includes some free props, for more of his projections.
'''
}
# descriptions = {

#     1: f'''NFL Week 2 – {TeamA} vs {TeamB} Live Preview & Prediction'''
# }
# chrome://version/
options = Options()
# options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
options.add_argument(
    "user-data-dir=C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
# options.add_argument("user-data-dir=C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\new")
driver = webdriver.Chrome(
    executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options)
driver.maximize_window()
driver.get(url)


def CheckLogin():
    try:
        driver.find_element_by_xpath(
            '//input[@id="user_session_email"]').send_keys(email)
        driver.find_element_by_xpath(
            '//input[@id="user_session_password"]').send_keys(passw)
        driver.find_element_by_xpath('//input[@name="commit"]').click()

    except:
        print('Already logged in!')


def EventPost(headline, venue, address1, address2, city, state, zip, description):
    driver.get(url)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="commit"]')))
    _headline = driver.find_element_by_xpath('//input[@id="event_page_page_headline"]').send_keys(headline)
    try:
        _capacity = driver.find_element_by_xpath(
            '//input[@id="event_page_capacity_count"]').send_keys('10')
    except:
        pass
    _venue = driver.find_element_by_xpath(
        '//input[@id="event_page_venue_name"]').send_keys(venue)
    _address1 = driver.find_element_by_xpath(
        '//input[@id="event_page_venue_address_address1"]').send_keys(address1)
    _address2 = driver.find_element_by_xpath(
        '//input[@id="event_page_venue_address_address2"]').send_keys(address2)
    _city = driver.find_element_by_xpath(
        '//input[@id="event_page_venue_address_city"]').send_keys(city)
    try:
        _state = driver.find_element_by_xpath(
            '//input[@id="event_page_venue_address_state"]').send_keys(state)
    except:
        pass
    _postal_code = driver.find_element_by_xpath(
        '//input[@id="event_page_venue_address_zip"]').send_keys(zip)
    _description_tiny = driver.find_element_by_xpath('//iframe[@id="event_page_content_editable_ifr"]')
    pc.copy(description)
    _description_tiny.send_keys(Keys.CONTROL, 'v')  #because it takes a long time with send keys()
    _submit = driver.find_element_by_xpath('//input[@name="commit"]').click()
    # time.sleep(2)
    WebDriverWait(driver, 15).until(EC.url_changes(driver.current_url))
    return driver.current_url


CheckLogin()
links = []
for headline in titles.values():
    for description in descriptions.values():
        event_url = EventPost(headline, venue, address1,
                            address2, city, state, zip, description)
        print(event_url)
        links.append(event_url)

with open('eventLinks.txt', 'w', encoding="utf-8") as file_name:
    for item in links:
        file_name.write(f"{item}\n")
    file_name.close()
    
# count = 1
# with(open('text.txt','w',encoding='utf-8'))as file:
#     for headline in titles.values():
#         for description in descriptions.values():
#             event_url = EventPost(headline, venue, address1,
#                             address2, city, state, zip, description)
#             text = f'{event_url}\n'
#             file.write(text)
#             count+=1
#     file.close()

print("Time Taken : %s seconds ---" % (time.time() - start_time))
time.sleep(10)
driver.quit()
