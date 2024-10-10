from func import scrolling,saving_files,drop_duplicate,headless_selenium_init,saving_path_csv,selenium_init
from bs4 import BeautifulSoup
import time
from lxml import html
import pandas as pd



def frapapa_func():
    path = f'{saving_path_csv}/FRAPAPA.csv'
    driver,wait,EC,By = selenium_init()
    driver.get('https://mobile.frapapa.com/')
    time.sleep(10)

    upcoming = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[3]/div[2]/div[3]")))
    time.sleep(10)
    upcoming.click()
    time.sleep(100)

    # wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/main/div/div/div/div/article/div/div/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div[7]')))
    

    matches = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'bto-sb-event-odds-content')))
    matches = matches.text.replace('\n','!').split('!')
    # print(matches)


    int_vals = [str(x) for x in range(1000,10000)]

    new_matches = []
    for x in matches:
        x = x.strip()
        if x in int_vals or '+' in x or '-' in x or '/' in x:
            pass
        else:
            new_matches.append(x)

    time_value = []
    time_index = []
    for i,x in enumerate(new_matches):
        if ':' in x:
            indx = new_matches.index(x,i,len(new_matches))
            time_index.append(indx)
            time_value.append(x)

    # print(new_matches)
    # print(time_index)
    # print(time_value)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 6:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]

                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[3])
                draw_odd = float(all_info[4])
                away_odd = float(all_info[5])
                bookmaker = 'FRAPAPA'

                data = {
                    'TIME':match_time,
                    'HOME TEAM':home_team,
                    'AWAY TEAM':away_team,

                    'HOME ODD': home_odd,
                    'DRAW ODD':draw_odd,
                    'AWAY ODD':away_odd,
                    'BOOKMAKER':bookmaker
                }
                saving_files(data=[data],path=path)
        except:
            pass
    drop_duplicate(path=path)
frapapa_func()