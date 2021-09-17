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
import os,re
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
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

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
    print(f"[*] Zevoy Tiktok Bot Automation\n[*] Author: RJD")
    try:
        menu()
    except Exception as e:
        print(f"[*] Error: {e}")
        browser.save_screenshot("ERROR_ZEFOY.png")
        try:
            browser.quit()
        except:
            pass

def reload():
    browser.get("https://zefoy.com")
    print(f"[*] Reload!")
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
    wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class,"btn btn-primary rounded-0 menu")]')))
    buttons = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class,"btn btn-primary rounded-0 menu")]')))
    input_videos = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '(//input[@placeholder="Enter Video URL"])')))
  
    try:
        click = buttons[choice].click()
        input_videos[choice].send_keys(vid_obj)
        input_videos[choice].send_keys(Keys.ENTER)
    except Exception as e:
        print(e)
def menu():
    global buttons
    global choice
    global input_videos
    global click
    global vid_obj


    browser.get("https://zefoy.com")
    
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
    sleep(5)
    tittles = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//h5[@class="card-title"]')))
    updates = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//small[contains(@class,"badge badge-round badge-")]')))
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
    input_videos[choice].send_keys(Keys.ENTER)
    sleep(2)
    for i in range(0, loop):
        input_videos[choice].send_keys(Keys.ENTER)
        
        print(f"[*] Submit {j}")
        j = j+1
        sleep(1)
        try:
            wait(browser,15).until(EC.presence_of_element_located((By.XPATH,'//button[contains(@class,"wbutton")]'))).click()
        except:
            pass
        try:
            wait(browser,1).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[5]/div/div/div[1]/div/form/button'))).click()
        except:
            pass
        try:
            notif = wait(browser,1).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Session Expired. Please Re Login! ')]")))
            print(f"[*] Session Expired, wait re-log!")

            reload()
            browser.save_screenshot("ZEFOY-1.png")
            
        except:
            pass
        try:
            loves = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div[4]/div/div/form/ul/li/div/button')))
            usernames = wait(browser,15).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"font-weight-bold d-inline-flex kadi-rengi")]')))
            for i in range(0,len(usernames)):
                print(f"[*] {i}. {usernames[i].text}")
            choice_love = int(input("[*] Input (Number):"))
            loves[choice_love].click()
            sleep(0.5)
            browser.save_screenshot("LOVES.png")
       
        except:
            pass

        sleep(0.5)
        # browser.save_screenshot("ZEFOY.png")
       
        get_delay = wait(browser,35).until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Please wait')]"))).text
        clear_time = re.findall(r'\b\d+\b', str(get_delay))
        print(f"[*] Submit Done, Please wait {clear_time[0]} minutes {clear_time[1]}s")
        minutes = int(clear_time[0])*60
        second = clear_time[1]
        delay = int(minutes)+int(second)
       
        sleep(delay)
    print("[*] Done, Finish Submit!")
    browser.quit()
    
open_browser()
