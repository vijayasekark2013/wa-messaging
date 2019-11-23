from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



# Replace below path with the absolute path
# to chromedriver in your computer
#driver = webdriver.Chrome('chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
#target = '"🏫 பள்ளி நண்பர்கள்👭👬👫"'
target = '"US Group"'

# Replace the below string with your own message
string = " Good Morning from Nitika :-) "

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
print(target)