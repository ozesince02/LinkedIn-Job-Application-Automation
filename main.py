import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

EMAIL = "santoshvishipulkit@gmail.com"
PASS = "Vishi17#"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-blink-features=AutomationControlled")

chrome_driver_path = "C:\dev\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?alertAction=viewjobs&f_AL=true&f_TPR=a1679930171-&geoId=102713980&keywords=python%20developer&location=India&refresh=true&sortBy=R")

sign_in_url = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
time.sleep(2)
sign_in_url.click()
time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASS)
time.sleep(2)
id_sign_in = driver.find_element(By.CLASS_NAME, "btn__primary--large")
id_sign_in.click()
time.sleep(2)

job_list = driver.find_elements(By.CLASS_NAME, "job-card-container")
for job in job_list:
    job.click()
    time.sleep(2)
    save_job = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_job.click()
    time.sleep(2)
    follow_company = driver.find_element(By.CLASS_NAME, "follow")
    follow_company.click()
    time.sleep(2)
