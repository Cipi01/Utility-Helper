import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def get_data_el(username, password):
    options = Options()
    options.add_argument('-headless')

    driver = webdriver.Firefox(options)

    driver.get('https://myelectrica.ro/index.php?pagina=login')

    driver.find_element(By.ID, 'myelectrica_utilizator').send_keys(username)
    password_field = driver.find_element(By.ID, 'myelectrica_pass')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)

    time.sleep(3.5)
    driver.implicitly_wait(10)

    # scroll_pixels = 500
    # driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")

    title_elements = driver.find_elements(By.CLASS_NAME, 'amount')

    data_list_raw = [i.text for i in title_elements]
    try:
        if data_list_raw[2] == '1 neachitata':
            driver.get("https://myelectrica.ro/index.php?pagina=facturile-mele")
            values_raw = driver.find_elements(By.XPATH, ".//tr")
            for row in values_raw:
                if row.get_attribute('class').startswith('warning'):
                    td_elem = row.find_elements(By.XPATH, './/td')
                    values_bill_list = [i.text for i in td_elem]
                    data_list_raw.append(values_bill_list[5])
        # temp_var = data_list_raw[0].split('\n')
        # temp_var.extend(data_list_raw[1:])
        # data_list = temp_var
    except IndexError:
        return "Incorrect credentials"
    driver.quit()
    return data_list_raw


if __name__ == '__main__':
    print(4)
