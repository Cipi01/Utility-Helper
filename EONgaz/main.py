import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def get_data_gaz(username, password):
    options = Options()
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    #options.add_argument('-headless')
    #options.add_argument('window-size=1920x1080')
    #options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')

    driver = webdriver.Firefox(options)
    driver.implicitly_wait(10)
    driver.get('https://www.eon.ro/myline/login')
    driver.implicitly_wait(10)
    # driver.find_element(By.CLASS_NAME, "sc-dcJsrY.fYDKfz").click()

    #time.sleep(3)
    driver.find_element(By.ID, 'userName').send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/form/div[3]/div/div/button").click()

    driver.implicitly_wait(10)
    time.sleep(5)
    if driver.current_url != 'https://www.eon.ro/myline/login':
        scroll_pixels = 500
        driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
        time.sleep(5)
        driver.refresh()
        driver.implicitly_wait(100)
        title_elements = driver.find_elements(By.CSS_SELECTOR, 'p.title')

        data_list_raw = [i.text for i in title_elements]
        temp_var = data_list_raw[0].split('\n')
        temp_var.extend(data_list_raw[1:])
        data_list = temp_var
        if len(data_list) != 5:
            print('not ok')
            print(data_list)
        else:
            return data_list
    else:
        return "Incorrect credentials."
    driver.quit()


if __name__ == "__main__":
    print(4)