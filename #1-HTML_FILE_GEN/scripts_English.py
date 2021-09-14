# -------------------This File for English Country----------------------------

import random
import webbrowser
import string
from pathlib import Path
from Dynamic_Title import make_title,random_string,make_title_format


# Provide the Folder path where you want to save the files
output_directory = Path('H:\max23')  # Important
demo_title = 'video-evr-bur-9YH.html'

middle_text_between_team = "Vs"# TeamA Vs TeamB

# After Title Random Words
title_tail_list = ['Live', 'Live Stream', 'Game live','Op game', 'Live Reddit ', 'Live Free On Tv']

# title_tail_list = ['Live Italy', 'Live Stream Italy', 'Game live Italy','Op game Italy', 'Live Reddit Italy ', 'Live Free On Tv Italy'],
livestream_word_list = ['livestream','Live Hd','Add more here']




# Edit the Infos
TeamInfo = {
    1: {
        'TeamA': "Germany Germany",
        'TeamB': "Italy Italy",
        'redirect_url': 'add redirect url here',
        'description':'''Enter Your description Here''',
        'youtube_url': {
            1: 'https://www.youtube.com/',
            2: 'https://www.youtube.com/',
            3: 'https://www.youtube.com/',
            4: 'https://www.youtube.com/',
            5: 'https://www.youtube.com/',
            6: 'https://www.youtube.com/',
            7: 'https://www.youtube.com/',
            8: 'https://www.youtube.com/',
            9: 'https://www.youtube.com/',
            10: 'https://www.youtube.com/',
            11: 'https://www.youtube.com/',
            12: 'https://www.youtube.com/',
            13: 'https://www.youtube.com/',
            14: 'https://www.youtube.com/',
            15: 'https://www.youtube.com/',
            16: 'https://www.youtube.com/',
            17: 'https://www.youtube.com/',
            18: 'https://www.youtube.com/',
            19: 'https://www.youtube.com/',
            20: 'https://www.youtube.com/',
            21: 'https://www.youtube.com/',
            22: 'https://www.youtube.com/',
            23: 'https://www.youtube.com/',
            24: 'https://www.youtube.com/',
            25: 'https://www.youtube.com/',
            26: 'https://www.youtube.com/',
            27: 'https://www.youtube.com/',
            28: 'https://www.youtube.com/',
            29: 'https://www.youtube.com/',
            30: 'https://www.youtube.com/',
        },
    },
    2: {
        'TeamA': "Argentina",
        'TeamB': "Brazil",
        'redirect_url': 'add redirect url here',
        'description':'''Enter Your description Here''',
        'youtube_url': {
            1: 'https://www.youtube.com/',
            2: 'https://www.youtube.com/',
            3: 'https://www.youtube.com/',
            4: 'https://www.youtube.com/',
            5: 'https://www.youtube.com/',
            6: 'https://www.youtube.com/',
            7: 'https://www.youtube.com/',
            8: 'https://www.youtube.com/',
            9: 'https://www.youtube.com/',
            10: 'https://www.youtube.com/',
            11: 'https://www.youtube.com/',
            12: 'https://www.youtube.com/',
            13: 'https://www.youtube.com/',
            14: 'https://www.youtube.com/',
            15: 'https://www.youtube.com/',
            16: 'https://www.youtube.com/',
            17: 'https://www.youtube.com/',
            18: 'https://www.youtube.com/',
            19: 'https://www.youtube.com/',
            20: 'https://www.youtube.com/', 
            21: 'https://www.youtube.com/',
            22: 'https://www.youtube.com/',
            23: 'https://www.youtube.com/',
            24: 'https://www.youtube.com/',
            25: 'https://www.youtube.com/',
            26: 'https://www.youtube.com/',
            27: 'https://www.youtube.com/',
            28: 'https://www.youtube.com/',
            29: 'https://www.youtube.com/',
            30: 'https://www.youtube.com/',
            },

    },
    3: {
        'TeamA': "Bercelona",
        'TeamB': "PSG",
        'redirect_url': 'add redirect url here',
        'description':'''Enter Your description Here''',
        'youtube_url': {
            1: 'https://www.youtube.com/',
            2: 'https://www.youtube.com/',
            3: 'https://www.youtube.com/',
            4: 'https://www.youtube.com/',
            5: 'https://www.youtube.com/',
            6: 'https://www.youtube.com/',
            7: 'https://www.youtube.com/',
            8: 'https://www.youtube.com/',
            9: 'https://www.youtube.com/',
            10: 'https://www.youtube.com/',
            11: 'https://www.youtube.com/',
            12: 'https://www.youtube.com/',
            13: 'https://www.youtube.com/',
            14: 'https://www.youtube.com/',
            15: 'https://www.youtube.com/',
            16: 'https://www.youtube.com/',
            17: 'https://www.youtube.com/',
            18: 'https://www.youtube.com/',
            19: 'https://www.youtube.com/',
            20: 'https://www.youtube.com/',
            21: 'https://www.youtube.com/',
            22: 'https://www.youtube.com/',
            23: 'https://www.youtube.com/',
            24: 'https://www.youtube.com/',
            25: 'https://www.youtube.com/',
            26: 'https://www.youtube.com/',
            27: 'https://www.youtube.com/',
            28: 'https://www.youtube.com/',
            29: 'https://www.youtube.com/',
            30: 'https://www.youtube.com/', 
            },
        
    },
    4: {
        'TeamA': "England",
        'TeamB': "Spain",
        'redirect_url': 'add redirect url here',
        'description':'''Enter Your description Here''',
        'youtube_url': {
            1: 'https://www.youtube.com/',
            2: 'https://www.youtube.com/',
            3: 'https://www.youtube.com/',
            4: 'https://www.youtube.com/',
            5: 'https://www.youtube.com/',
            6: 'https://www.youtube.com/',
            7: 'https://www.youtube.com/',
            8: 'https://www.youtube.com/',
            9: 'https://www.youtube.com/',
            10: 'https://www.youtube.com/',
            11: 'https://www.youtube.com/',
            12: 'https://www.youtube.com/',
            13: 'https://www.youtube.com/',
            14: 'https://www.youtube.com/',
            15: 'https://www.youtube.com/',
            16: 'https://www.youtube.com/',
            17: 'https://www.youtube.com/',
            18: 'https://www.youtube.com/',
            19: 'https://www.youtube.com/',
            20: 'https://www.youtube.com/',
            21: 'https://www.youtube.com/',
            22: 'https://www.youtube.com/',
            23: 'https://www.youtube.com/',
            24: 'https://www.youtube.com/',
            25: 'https://www.youtube.com/',
            26: 'https://www.youtube.com/',
            27: 'https://www.youtube.com/',
            28: 'https://www.youtube.com/',
            29: 'https://www.youtube.com/',
            30: 'https://www.youtube.com/test120', 
            },
        

    },
    5: {
        'TeamA': "Brazil",
        'TeamB': "Italy",
        'redirect_url': 'add redirect url here',
        'description':'''Enter Your description Here''',
        'youtube_url': {
            1: 'https://www.youtube.com/',
            2: 'https://www.youtube.com/',
            3: 'https://www.youtube.com/',
            4: 'https://www.youtube.com/',
            5: 'https://www.youtube.com/',
            6: 'https://www.youtube.com/',
            7: 'https://www.youtube.com/',
            8: 'https://www.youtube.com/',
            9: 'https://www.youtube.com/',
            10: 'https://www.youtube.com/',
            11: 'https://www.youtube.com/',
            12: 'https://www.youtube.com/',
            13: 'https://www.youtube.com/',
            14: 'https://www.youtube.com/',
            15: 'https://www.youtube.com/',
            16: 'https://www.youtube.com/',
            17: 'https://www.youtube.com/',
            18: 'https://www.youtube.com/',
            19: 'https://www.youtube.com/',
            20: 'https://www.youtube.com/',
            21: 'https://www.youtube.com/',
            22: 'https://www.youtube.com/',
            23: 'https://www.youtube.com/',
            24: 'https://www.youtube.com/',
            25: 'https://www.youtube.com/',
            26: 'https://www.youtube.com/',
            27: 'https://www.youtube.com/',
            28: 'https://www.youtube.com/',
            29: 'https://www.youtube.com/',
            30: 'https://www.youtube.com/test150', 
        },
        
        
    },
}





# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

if output_directory.exists():
    pass
else:
    Path(output_directory).mkdir(parents=True, exist_ok=True)

count = 1
file_name_list = []
letters = string.ascii_uppercase + string.digits
numbers = string.digits

# for item in len(TeamInfo)
for team_no in range(1, len(TeamInfo)+1):
    
    TeamA = TeamInfo[team_no]['TeamA']
    TeamB = TeamInfo[team_no]['TeamB']
    TeamA_ = '-'.join(TeamA.split())
    TeamB_ = '-'.join(TeamB.split())
    print(f'\n\nFormat No {team_no} - For {TeamA}-{TeamB}')
    
    format = make_title_format(demo_title,TeamA,TeamB)
    
    redirect_link = TeamInfo[team_no]['redirect_url']
    youtube_link = TeamInfo[team_no]['youtube_url']
    description = TeamInfo[team_no]['description']
    title = f"{TeamA} {middle_text_between_team} {TeamB}"
    for i in range(1, len(youtube_link)+1):
        title_tail = random.choice(title_tail_list)

        content = '''\
    




            
<html dir='rtl'><head>
<meta charset="utf-8">
<meta content='width=devicevswidth,minimumvsscale=1,initialvsscale=1' name='viewport' />
<meta name='robots' content='noarchive' />
<meta name="description" content="{title} {title_tail}">
<h1><a href="{redirect_url}">{title} {title_tail}</a></h1>
<title>{title} {title_tail}
++>{livestream}:{TeamA} {middle_text_between_team} {TeamB} Football Live {TeamA} {middle_text_between_team} {TeamB} Game Live: {TeamA} {middle_text_between_team} {TeamB} Live Streams >{TeamA} {middle_text_between_team} {TeamB} Live op tv >{TeamB} {middle_text_between_team} {TeamA} Live Reddit {TeamB} {middle_text_between_team} {TeamA} Live !!2021++>>(NCAAF-2021)**{TeamB} {middle_text_between_team} {TeamA} Live 05 September 2021 Broadcast Today US.TV Live op tv {TeamB} {middle_text_between_team} {TeamA} Live Free On Tv {TeamB} {middle_text_between_team} {TeamA} Live score (NCAAF 2021) {TeamB} {middle_text_between_team} {TeamA} Live #{TeamB} {middle_text_between_team} {TeamA} Live Update Score #{TeamB} {middle_text_between_team} {TeamA} Live #{TeamB} {middle_text_between_team} {TeamA} Live #{TeamB} {middle_text_between_team} {TeamA} Live>> {TeamB} {middle_text_between_team} {TeamA}Live on radio #2021 {TeamB} {middle_text_between_team} {TeamA} Live Start Time Today #{TeamB} {middle_text_between_team} {TeamA} Live redit HD*{rand_num}

</title>
<div style='visibility:hidden'>
<img src='0' onerror= top.location.href="{redirect_url}">
<iframe width='100%' height='500' src="{youtube_url}" frameborder='0' allow='autoplay; encryptedvsmedia' allowfullscreen></iframe>
{description}
</div></body>


</html>'''.format(title=title, title_tail=title_tail, TeamA=TeamA, TeamB=TeamB, redirect_url=redirect_link, youtube_url=youtube_link[i],description=description,rand_num = ''.join(random.choice(numbers) for i in range(4)),livestream = random.choice(livestream_word_list),middle_text_between_team=middle_text_between_team)

        
        additional_extension = ''.join(
        random.choice(letters) for i in range(3))
        # File_name_html = f'{StartText_For_Filename }-{TeamA_}-vs-{TeamB_}-{MiddleText_For_Filename }-{str(count)}-{additional_extension}.html'
        File_name_html = make_title(format,count)

        file_name_list.append(File_name_html)

        file_location = Path(output_directory, File_name_html)

        with open(file_location, 'w') as html_file:
            html_file.write(content)
            html_file.close()
        count = count + 1


# Adding all the generated html file names with the extensions
with open(Path(output_directory, '#1_filenames.txt'), 'w') as file_name:
    for item in file_name_list:
        file_name.write(f"{item}\n")
    file_name.close()


print(f"Files successfully generated!!!\n Location = '{output_directory}'")


webbrowser.open(output_directory)  # Opens the output folder.