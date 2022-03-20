
import time
from turtle import pos
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
})

driver = webdriver.Chrome(chrome_options=chrome_options,)
driver.implicitly_wait(15)


# You can change your post message below
message = "Aracınızın 100 km'de yakıt tüketimini kolayca hesaplayan uygulama\n* Aşağıdaki Görsele tıklayarak indirebilirsiniz: https://play.google.com/store/apps/details?id=com.yakit.yakit_hesabi&gl=TR"
e = 'example@gmail.com' #this here email
pas = 'password' #this here password
url = 'https://www.facebook.com/login'

# Groups Links
groupsCar = [
    # You have to facebook groups link with ID
    'https://www.facebook.com/groups/example',
    ]


# Facebok Login
driver.get(url)
email = driver.find_element_by_id('email')
email.send_keys(e)
password = email = driver.find_element_by_id('pass')
email.send_keys(pas)
time.sleep(2)
loginButton = email = driver.find_element_by_id('loginbutton')
loginButton.click()

# Send Post
time.sleep(5)
for i in groupsCar:
    driver.get(i)
    time.sleep(7)
    post_box = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span")
    post_box.click()
    post = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]")
    post.click()
    elemInput = driver.switch_to.active_element
    elemInput.send_keys(message)
    time.sleep(5)
    button = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div")
    button.click()
    time.sleep(5)
