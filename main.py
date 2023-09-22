import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = "andreeamarian24@yahoo.it"
password = "Baritiu109a"
driver = webdriver.Firefox()

driver.get('https://www.eon.ro/myline/login')

driver.find_element(By.ID, 'userName').send_keys(username)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

# Get the HTML of the page after successful login
driver.implicitly_wait(10)

time.sleep(5)
driver.implicitly_wait(10)

scroll_pixels = 500
driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")

title_elements = driver.find_elements(By.CSS_SELECTOR, 'p.title')

data_list_raw = [i.text for i in title_elements]
temp_var = data_list_raw[0].split('\n')
temp_var.extend(data_list_raw[1:])
data_list = temp_var
if len(data_list) != 5:
    print('not ok')
    print(data_list)
else:
    index_date = data_list[3]
    print(f"index period: {index_date}")
    print(data_list)
driver.quit()
