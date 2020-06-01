from selenium import webdriver                          #to import selenium for web automation
from selenium.webdriver.common.keys import Keys         #for auto typing
from time import sleep                                  #sleep is used to provide delay
import urllib.request

driver = webdriver.Chrome(r'C:\Users\Vidhi Sejpal\Desktop\Selenium\chromedriver.exe')  #to load chrome 

driver.get('https://www.instagram.com/accounts/login/')   #to load instagram on chrome

sleep(2)                                               # used to give delay

username = 'boo__its__me__2'
password = 'username2831'

#for closing chrome
def chrome_close():
    driver.close()            #to close the browser automatically

#TO login to instagram
def login(username, password):
    
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

    sleep(2)

    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    sleep(2)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

#to go to some user_id
def get_user_id(user_id):

    driver.get('https://www.instagram.com/'  + user_id)             #for going to user id of alia bhatt
    sleep(1)
    driver.find_elements_by_class_name('eLAPa')[0].click()          

    count =0
    for i in range(0,5):
        sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()

        if driver.find_elements_by_class_name('KL4Bh'):
            print('Image')
        
            img_to_download = driver.find_elements_by_class_name('FFVAD')[i] 
            url_to_download = img_to_download.get_property('src')

            try:
                count += 1
                urllib.request.urlretrieve(url_to_download,'alia_bhat_{}.jpg'.format(count))
                print('Image sucessfully downloaded !!!!')
                sleep(2)
                

            except:
                print('Image cannot be downloaded')\
                
#to open stories
def open_Stories():
    driver.find_element_by_class_name('OE3OK ').click()

#to like users post
def like_post(username):
    driver.get('https://www.instagram.com/'  + username)            
    sleep(1)
    driver.find_elements_by_class_name('eLAPa')[0].click() 
    sleep(2)

    for i in range(0,5):

        if (driver.find_elements_by_class_name('_8-yf5 ')[7].get_attribute('aria-label')) == "Like":
        
            driver.find_elements_by_class_name('wpO6b ')[1].click()
            sleep(1)
            driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
            sleep(1)
        
        else:
            sleep(2)
            driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()

#to follow user
def follow_user(userid):
    driver.get('https://www.instagram.com/'  + userid)            
    sleep(1)
    driver.find_element_by_xpath("//button[contains(text(),'Follow')]" ).click()
    


        
login('boo__its__me__2','username2831')
#follow_user('beachtribes')
like_post('beachtribes')
#get_user_id('aliaabhatt')
#open_Stories()



