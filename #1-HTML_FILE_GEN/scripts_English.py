# -------------------This File for English Country----------------------------

import random
import webbrowser
import string
from pathlib import Path
import string, random
import re

# Provide the Folder path where you want to save the files
output_directory = Path('H:\max23')  # Important

middle_text_between_team = "Vs"  # TeamA Vs TeamB

# After Title Random Words
title_tail_list = ['Live', 'Live Stream', 'Game live', 'Op game', 'Live Reddit ', 'Live Free On Tv']

# title_tail_list = ['Live Italy', 'Live Stream Italy', 'Game live Italy','Op game Italy', 'Live Reddit Italy ', 'Live Free On Tv Italy'],
livestream_word_list = ['livestream', 'Live Hd', 'Add more here']

# Edit the Infos
TeamInfo = {
    1: {
        'TeamA': "Germany Germany",
        'TeamB': "Italy Italy",
        'redirect_url': 'add redirect url here',
        'description': '''Enter Your description Here''',
        'file_format': '1video-[randomLD5]-[randomLD5]-[random1]-[random1]-[randomLD3]-[random1]-anything[random5]-[numbers].html',
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
        'description': '''Enter Your description Here''',
        'file_format': 'video-2-[randomLD5]-[random1]-[randomLD3]-[random1]-[random4]-[numbers].html',
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
        'description': '''Enter Your description Here''',
        'file_format': 'video3-[random1]-[random1]-[randomLD3]-[randomLD3]-Germany-[numbers].html',
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
        'description': '''Enter Your description Here''',
        'file_format': 'video-4-[random4]-[random1]-[random1]-[randomLD3]-[randomLD3]-bk[numbers].html',
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
        'description': '''Enter Your description Here''',
        'file_format': 'video-5-[random4]-[random1]-[random1]-[randomLD3][numbers].html',
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



description= '''[FIRST_LINE]
[TeamA] [TeamB]
consectetur adipisicing elit. Quis molestiae reiciendis 
nemo, commodi aspernatur natus laudantium ullam inventore itaque a quas, excepturi nam nesciunt nequ
e tenetur non eum accusamus incidunt distinctio cupiditate temporibus tempore nisi voluptatum volupta
s? Esse voluptatum incidunt ea
[MIDDLE_LINE]
recusandae earum similique dolore, expedita molestias minus corrupti 
voluptatem, eaque non explicabo error inventore quas et ex debitis reiciendis. Explicabo fugiat dist
inctio hic dignissimos perferendis quas nemo nisi obcaecati, neque assumenda, aspernatur adipisci eum
mollitia labore eos quod odio saepe. Ipsum, perferendis deleniti consequuntur molestias eveniet quisqu
am, enim mollitia pariatur neque quos suscipit laborum reiciendis id nisi sunt repellat.
[LAST_LINE]
'''


def random_string(onlyString, no_of_string):
    if onlyString:
        return ''.join(random.choice(string.ascii_lowercase) for i in range(int(no_of_string)))
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(int(no_of_string)))


def make_title(title, count):
    if '[numbers]' in title:
        if count < 10:
            title = title.replace('[numbers]', f'0{str(count)}')
        title = title.replace('[numbers]', str(count))
    if re.findall("random[0-9]", title):
        check_random = re.findall("random[0-9]", title)
        for num in range(len(check_random)):
            title = title.replace(f'[{check_random[num]}]', random_string(True, check_random[num][6]),1)
    if re.findall("randomLD[0-9]", title):
        check_randomLD = re.findall("randomLD[0-9]", title)
        for num in range(len(check_randomLD)):
            title = title.replace(f'[{check_randomLD[num]}]', random_string(False,check_randomLD[num][8]),1)

    return title
def make_description(description,teamA,teamB):
    if '[FIRST_LINE]' in description:
        description = description.replace('[FIRST_LINE]',random.choice(description_first_list),1)
    if '[LAST_LINE]' in description:
        description = description.replace('[LAST_LINE]',random.choice(description_end_list),1)
    if '[MIDDLE_LINE]' in description:
        description = description.replace('[MIDDLE_LINE]',random.choice(description_end_list),1)
    if '[TeamA]' in description:
        description = description.replace('[TeamA]',teamA)
    if '[TeamB]' in description:
        description = description.replace('[TeamB]',teamB)
    return description



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
for team_no in range(1, len(TeamInfo) + 1):

    TeamA = TeamInfo[team_no]['TeamA']
    TeamB = TeamInfo[team_no]['TeamB']
    TeamA_ = '-'.join(TeamA.split())
    TeamB_ = '-'.join(TeamB.split())

    redirect_link = TeamInfo[team_no]['redirect_url']
    youtube_link = TeamInfo[team_no]['youtube_url']
    title = f"{TeamA} {middle_text_between_team} {TeamB}"
    for i in range(1, len(youtube_link) + 1):
        title_tail = random.choice(title_tail_list)
        newdescription = make_description(description,TeamA,TeamB)

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


</html>'''.format(title=title, title_tail=title_tail, TeamA=TeamA, TeamB=TeamB, redirect_url=redirect_link,
                  youtube_url=youtube_link[i], description=newdescription,
                  rand_num=''.join(random.choice(numbers) for i in range(4)),
                  livestream=random.choice(livestream_word_list), middle_text_between_team=middle_text_between_team)

        additional_extension = ''.join(
            random.choice(letters) for i in range(3))
        # File_name_html = f'{StartText_For_Filename }-{TeamA_}-vs-{TeamB_}-{MiddleText_For_Filename }-{str(count)}-{additional_extension}.html'
        File_name_html = make_title(TeamInfo[team_no]['file_format'], count)

        file_name_list.append(File_name_html)

        file_location = Path(output_directory, File_name_html)

        with open(file_location, 'w', encoding="utf-8") as html_file:
            html_file.write(content)
            html_file.close()
        count = count + 1

# Adding all the generated html file names with the extensions
with open(Path(output_directory, '#1_filenames.txt'), 'w', encoding="utf-8") as file_name:
    for item in file_name_list:
        file_name.write(f"{item}\n")
    file_name.close()

print(f"Files successfully generated!!!\nLocation = '{output_directory}'")

webbrowser.open(output_directory)  # Opens the output folder.


# make_title(title='[random1] [random1] [random1]',count=0)