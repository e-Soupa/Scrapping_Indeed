import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import pickle


options = uc.ChromeOptions()
# stealth arguments
options.add_argument('--disable-blink-features=AutomationControlled')
#path to your chrome profile to save & load cookies
options.add_argument('--user-data-dir=/home/sou/.config/chromium/Default') 

driver = uc.Chrome(options=options, version_main=142)
driver.get("https://fr.indeed.com")
time.sleep(10)

#FIRST PAGE INDEED
#fill job title

job_input = driver.find_element(By.NAME,"q")
job_text = "preparateur"
for character in job_text:
    job_input.send_keys(character)
    time.sleep(random.uniform(0.1, 0.3))
time.sleep(1)

'''
#fill location
location_input = driver.find_element(By.NAME, "l")
#clear location input
location_input.send_keys(Keys.CONTROL + "a")
time.sleep(2)
location_input.send_keys(Keys.DELETE)
location_input.clear()
location_text = "mulhouse"
for character in location_text:
    location_input.send_keys(character)
    time.sleep(random.uniform(0.1, 0.3))
time.sleep(2)
'''

# click search button
search_button = driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
search_button.click()
time.sleep(2)

'''SECOND PAGE INDEED'''
# Switch to job offer tab and Click apply button 

job_cards = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
# Open the first 3 Jobs
max_jobs = min(10, len(job_cards))
for i in range(max_jobs):
    job_cards[i].click()
    time.sleep(5)

    try:
        # Click only on jobs with "Easily apply" filter
        easily_apply = driver.find_element(By. CLASS_NAME, "iaIcon")        
        if "Candidature simplifiée" in easily_apply.text:
            # re-find apply button AFTER the job details panel updates
            apply_button = driver.find_element(
                By.CLASS_NAME, "jobsearch-IndeedApplyButton-contentWrapper"
            )
            apply_button.click()
            time.sleep(4)
        else: 
             continue
    except NoSuchElementException:
            continue
        
# Save & load cookies
cookies = driver.get_cookies()
with open("indeed_cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
time.sleep(3)
# After opening all 5 jobs/apply buttons
expected_tabs = 3
# Wait until all tabs are actually open
while len(driver.window_handles) < expected_tabs:
    time.sleep(2)
time.sleep(2)

#Build the tabs list
switch_tabs = driver.window_handles

# Start from 1 if tab[0] is the search/results page
for switch in switch_tabs[1:]:
    driver.switch_to.window(switch) 
    time.sleep(4)

    '''
    # Wait for postal code input to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "location-postal-code"))
    )
    '''
    while True:
            try:
                continuer_button = driver.find_elements(By.TAG_NAME, "button")
                no_continuer = None
                for button in continuer_button:
                    if "Continuer" in button.text:
                        no_continuer = button
                        break
                if no_continuer is None:
                    break
                no_continuer.click()
                time.sleep(2.5)
            except NoSuchElementException:
                break   

    # Wait for postuler button code to load
    time.sleep(5)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "submit-application"))
        )

    Postuler_button = driver.find_element(By.NAME, "submit-application")
    Postuler_button.click()
    time.sleep(5)

time.sleep(500)
driver.quit
