from selenium import webdriver
from selenium.webdriver.common.by import By
import time

site="https://www.adamchoi.co.uk/teamgoals/detailed"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

browser=driver.get(site)

all_matches=driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches.click()

rows=driver.find_elements(By.TAG_NAME,"tr")

date=[]
team1=[]
result=[]
team2=[]

for ele in rows:
    date.append(ele.find_element(By.XPATH,"./td[1]").text)
    team1.append(ele.find_element(By.XPATH,"./td[2]").text)
    result.append(ele.find_element(By.XPATH,"./td[3]").text)
    team2.append(ele.find_element(By.XPATH,"./td[4]").text)

time.sleep(5)
driver.quit()

import pandas as pd
df=pd.DataFrame({"DATE":date,"TEAM 1":team1,"RESULT":result,"TEAM 2":team2})
df.to_csv("Football_data.csv",index=False)