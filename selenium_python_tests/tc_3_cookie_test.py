from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True


# options.add_argument('--disable-gpu')

def test_tc_3_cookies():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    time.sleep(2)

    accept_button = driver.find_element_by_xpath('/html/body/div/footer/div/div/div/div[2]/button[2]/div')
    decline_button = driver.find_element_by_xpath('/html/body/div/footer/div/div/div/div[2]/button[1]/div')
    cookie_buttons = driver.find_elements_by_xpath('/html/body/div/footer/div/div/div/div/button')
    # print(len(cookie_buttons))

    assert len(cookie_buttons) == 2
    assert accept_button.is_enabled()
    assert decline_button.is_enabled()

    accept_button.click()

    time.sleep(2)

    driver.refresh()

    driver.get('http://localhost:1667/')
    time.sleep(1)

    cookie_buttons = driver.find_elements_by_xpath('/html/body/div/footer/div/div/div/div/button')
    # print(len(cookie_buttons))

    assert len(cookie_buttons) == 0

    driver.close()
