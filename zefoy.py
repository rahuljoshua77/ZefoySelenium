import undetected_chromedriver as uc
from time import sleep
uc.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
cwd = os.getcwd()

opts = Options()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
#opts.add_experimental_option('excludeSwitches', ['enable-logging'])

def get_captcha_text(png):
    file_list_akun = "api_key.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    get_api_key = akun.split("\n")
    api_key = get_api_key[0]
    captcha_fp = open(f"{cwd}\captcha_image.png", 'rb')
   
    client = AnticaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task)
    job.join()
     
    return job.get_captcha_text()

def open_browser():
    global browser
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
    menu()

def menu():
    browser.get("https://zefoy.com")
    print(f"[*] Open Zefoy")
    #check captcha
    sleep(3)
    try:
        img_captcha = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//img[@class="img-thumbnail card-img-top"]')))
        sleep(0.5)
        captcha_image = img_captcha.screenshot("captcha_image.png")
        print(f"[*] Solving Captcha")
        captcha_text = get_captcha_text(captcha_image)
        print(f"[*] Captcha Solved: {captcha_text} ")
        captcha_fill = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter the word"]')))
        captcha_fill.send_keys(captcha_text) 
        captcha_fill.send_keys(Keys.ENTER)
        
        #tittle service
    except:
        pass
    sleep(2)
    tittles = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//h5[@class="card-title"]')))
    updates = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class="badge badge-round badge-warning d-sm-inline-block"]')))
    buttons = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class,"btn btn-primary rounded-0 menu")]')))
    input_videos = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '(//input[@placeholder="Enter Video URL"])')))
  
    print("[*] Menu: ")
    for i in range(0,len(tittles)):
        print(f"[*] {i}. {tittles[i].text}: {updates[i].text}")
    choice = int(input("[*] Input Choice (Number): "))
    click = buttons[choice].click()
    vid_obj = input("[*] Input Link: ")
    loop = int(input("[*] How Many (Number): "))
    j = 1
    input_videos[choice].send_keys(vid_obj)
    for i in range(0, loop):
        input_videos[choice].send_keys(Keys.ENTER)
        print(f"[*] Submit {j}")
        sleep(1)
        try:
            wait(browser,15).until(EC.presence_of_element_located((By.XPATH,'//button[@class,"abjdt wbutton oalenus btn srthjv btn-dark jmw rounded-0 egbv font-weight-bold oxip p-2 vcndajshxpbw"]'))).click()
        except:
            pass
        try:
            notif = wait(browser,1).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Session Expired. Please Re Login! ')]")))
            print(f"[*] Session Expired, Back to main menu!")
            menu()
            break
        except:
            pass
        sleep(0.5)
        #browser.save_screenshot("ZEFOY.png")
        print(f"[*] Please wait 2 minutes")
        sleep(120)
        input_choice = input("[*] Back to Menu? Y/n (n = end/close)")
        input_choice = input_choice.lower()
        if input_choice == "y":
            menu()
        else:
            browser.quit()
        print(f"[*] Please wait 2 minutes")
        
        menu()


    
open_browser()
