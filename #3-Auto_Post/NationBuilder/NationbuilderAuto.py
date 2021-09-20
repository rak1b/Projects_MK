from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
from selenium.webdriver.common.keys import Keys
import traceback
start_time = time.time()
from pathlib import Path
# pip install pyperclip,selenium
# chrome://version/
path = Path(__file__).parent.resolve()




chrome_profile = 'C:\\Users\\rak13\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1'
chrome_driver_path = r'C:\chromedriver\chromedriver.exe'
number_of_image = 4
linksFile = 'EventLinksN.txt'



email = 'harmon.jaasiel@acelap.com'
password = 'Rakibrk11'
url = 'https://www.keliiakina.com/users/event_pages/new?parent_id=150'
# url = 'https://www.okgrassrootsproject.com/users/event_pages/new?parent_id=6'

venue = 'venue'
address1 = 'address1'
address2 = 'address2'
city = 'city'
state = 'state'
zip = '5555'



Teams = {
    1 : {
        'TeamA':'Brazil',
        'TeamB':'Argentina',
        'LINK' : 'https://source.unsplash.com',
        'LINK_TEXT':"WATCH HERE ▶️▶️"
    },
    # 2:{
    #     'TeamA':'PSG',
    #     'TeamB':'Bercelona'
    # }
}

titles = {
    1: '[HD] [TeamA] vs [TeamB] Live Stream',
    # 2: '[ONLINE] [TeamB] vs [TeamA] Live Stream',
    # 3: '[NCAA] [TeamA] vs [TeamB] Live Online',
    # 4: '[WATCH] [TeamB] vs [TeamA] Live Online',
    # 5: '[LIVE] [TeamA] vs [TeamB] Live Free',
    # 6: '[ITV] [TeamB] vs [TeamA] Live Free',
    # 7: '[STREAMING] [TeamA] vs [TeamB] Live',
    # 8: '[FREE]>>> [TeamB] vs [TeamA] Live',
    # 9: '[HDQ] [TeamA] vs [TeamB] 2021 Live',
    # 10: '[GAME]>>> [TeamB] vs [TeamA] 2021 Live',
}


descriptions = {
    1: '''NFL Week 2 – [TeamA] vs [TeamB] Live Preview & Prediction
[TeamA] vs [TeamB] Live kick-off time, TV channel, live stream info and team news
[TeamA] vs [TeamB] Live free live stream and how to watch the NFL Week 2
[LINK]
Live NFL Week 2: [TeamA] vs [TeamB] Live as McKenzie earns rare start at 10
Lavonte David was fined for this non-called penalty so the [TeamA] vs [TeamB] Live will feel like justice has been served, but this potentially swung the game (obviously we are using some hindsight to come to that conclusion). How is that fair?
4. A quick note regarding the “third-and-long” measure as a litmus test for the franchise-iness of a quarterback: In 2019, the Cowboys led the [TeamA] vs [TeamB] Live in third-and-6+ conversion rate (34.5%). In 2020, with Dak Prescott missing two thirds of the season, they fell to dead last (18.8%). In last Thursday’s opener, they went a respectable 2-for-6 (33.3%) against the Bucs.
Potential fits likely dwindled based on Sherman being charged in July with five misdemeanors of driving under the i[TeamA] vs [TeamB] Liveuence, reckless endangerment of roadway workers, criminal trespass in the second degree (domestic violence designation), resisting arrest and malicious mischief in the third degree (domestic violence designation). 
After posting 13 touchdown catches in 2015 and earning a Pro Bowl nod, Eifert suffered through three injury-plagued seasons before bouncing back and playing 16 games in 2019. He signed a two-year, free-agent deal with the [TeamA] the following offseason.
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
That's Will Brinson, highlightingddkfkfdkdfdf Buffalo's defense as a big reason he likes the Bills to bounce back in a big way against their AFC East rivals. Check out Brinson's full rundown of Week 2 picks and best bets, which includes some free props, for more of his projections.
''',

2: '''NFL Week 2 – [TeamA] vs [TeamB] Live Preview & Prediction
[TeamA] vs [TeamB] Live kick-off time, TV channel, live stream info and team news
[TeamA] vs [TeamB] Live free live stream and how to watch the NFL Week 2
[LINK]
Live NFL Week 2: [TeamA] vs [TeamB] Live as McKenzie earns rare start at 10
Lavonte David was fined for this non-called penalty so the [TeamA] vs [TeamB] Live will feel like justice has been served, but this potentially swung the game (obviously we are using some hindsight to come to that conclusion). How is that fair?
4. A quick note regarding the “third-and-long” measure as a litmus test for the franchise-iness of a quarterback: In 2019, the Cowboys led the [TeamA] vs [TeamB] Live in third-and-6+ conversion rate (34.5%). In 2020, with Dak Prescott missing two thirds of the season, they fell to dead last (18.8%). In last Thursday’s opener, they went a respectable 2-for-6 (33.3%) against the Bucs.
Potential fits likely dwindled based on Sherman [TeamA] being charged in July with five misdemeanors of driving under the i[TeamA] vs [TeamB] Liveuence, reckless endangerment of roadway workers, criminal trespass in the second degree (domestic violence designation), resisting arrest and malicious mischief in the third degree (domestic violence designation). 
After posting 13 touchdown catches in 2015 and earning a Pro Bowl nod, Eifert suffered through three injury-plagued seasons before bouncing back and playing 16 games in 2019. He signed a two-year, free-agent deal with the [TeamA] the following offseason.
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

linksFile = path/linksFile

options = Options()
prefs = {"profile.managed_default_content_settings.images": 5}
options.add_experimental_option("prefs", prefs)
options.add_argument(f"user-data-dir={chrome_profile}")
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
driver.maximize_window()

def replace_string(Text,old,new,old2='',new2='',old3='',new3=''):
    Text=Text.replace(old,new)
    Text = Text.replace(old2,new2)
    return Text.replace(old3,new3)


    
def CheckLogin():
    try:
        driver.get(url)
        driver.find_element_by_id('user_session_email').send_keys(email)
        driver.find_element_by_id('user_session_password').send_keys(password)
        driver.find_element_by_name('commit').click()
    except:
        print('Already logged in!')



def EventPost(headline, venue, address1, address2, city, state, zip,description):
    driver.get(url)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="commit"]')))
    _headline = driver.find_element_by_id('event_page_page_headline').send_keys(headline)
    try:_capacity = driver.find_element_by_id('event_page_capacity_count').send_keys('10')
    except:pass
    _venue = driver.find_element_by_id('event_page_venue_name').send_keys(venue)
    _address1 = driver.find_element_by_id("event_page_venue_address_address1").send_keys(address1)
    _address2 = driver.find_element_by_id("event_page_venue_address_address2").send_keys(address2)
    _city = driver.find_element_by_id("event_page_venue_address_city").send_keys(city)
    try:_state = driver.find_element_by_id("event_page_venue_address_state").send_keys(state)
    except:pass
    _postal_code = driver.find_element_by_id("event_page_venue_address_zip").send_keys(zip)
    description = driver.execute_script(f'tinyMCE.activeEditor.setContent(`{description}`)')

    _submit = driver.find_element_by_name('commit').click()
    WebDriverWait(driver, 15).until(EC.url_changes(driver.current_url))
    return driver.current_url


try:
    CheckLogin()
    # def make_description(visit_url,url_text,description):
    # link_html =f'<a href="{visit_url}">{url_text}</a>'
    # description = description.replace('[LINK]',{link_html})
    # driver.execute_script(f'tinyMCE.activeEditor.setContent(`{description}`)')

    count = 0
    with(open(linksFile,'w',encoding='utf-8'))as file:
        for team in Teams.values():
            for headline in titles.values():
                headline = replace_string(headline,'[TeamA]',team['TeamA'],'[TeamB]',team['TeamB'])
                for description in descriptions.values():
                    visit_url = team['LINK']
                    url_text = team['LINK_TEXT']
                    link_html =f'<h2><a href="{visit_url}">{url_text}</a></h2>'
                    description = replace_string(description,'[TeamA]',team['TeamA'],'[TeamB]',team['TeamB'],'[LINK]',link_html)
                    event_url = EventPost(headline, venue, address1,address2, city, state, zip, description)
                    text = f'{event_url}\n'
                    file.write(text)
                    count+=1
                    print(f"{count} Post Completed")
                    print("Time Taken : %s seconds ---" % (time.time() - start_time))
                    if count<=2 : break
                    
        file.close()

    
    print("Time Taken : %s seconds ---" % (time.time() - start_time))
    time.sleep(10)
    driver.quit()
    
except Exception:
    driver.quit()
    traceback.print_exc()
    