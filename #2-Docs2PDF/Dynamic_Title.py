
import string,random
import re


def random_string(no_of_string):
    return ''.join(random.choice(string.ascii_uppercase )for i in range(int(no_of_string)))

def make_title_format(title,TeamA=None,TeamB=None):
    while(1):
        print(f"Current Title : {title}")
        which_part = input("Enter the part you want to replace : ")
        if which_part.lower() in ['q','Q','quit']:break
        elif which_part not in title:
            print(f'{which_part} is not in Title,Try Again![CASE SENSITIVE]\n')
            continue
        new_part = input(f"\nChange this :'{which_part}' by : ")
        if new_part.lower() in ['q','Q','quit']:break
        elif new_part.lower() == 'random':
            no = input("How many random Letter? ")
            new_part = f'[random{no}]'
        elif new_part.lower() == 'numbers':
            new_part = f'[numbers]'
        elif new_part.lower() == 'TeamA'.lower():
            new_part = '-'.join(TeamA.split())
            print(new_part)
        elif new_part.lower() == 'TeamB'.lower():
            new_part = '-'.join(TeamB.split())
            print(new_part)
            
            
        title = title.replace(which_part,new_part)
        print(f"Your updated Title : {title} \n \n")
    return title


    


def make_title(title,count):
    if '[numbers]' in title:
        if count<10:
            title = title.replace('[numbers]',f'0{str(count)}')
        title = title.replace('[numbers]',str(count))
    if re.findall("random[0-9]", title):
        check_random = re.findall("random[0-9]", title)
        title = title.replace(f'[{check_random[0]}]',random_string(check_random[0][6]))
        
    return title


