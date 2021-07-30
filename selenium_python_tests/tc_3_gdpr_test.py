from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True
# options.add_argument('--disable-gpu')

def test_tc_3_gdpr():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    time.sleep(2)

    accept_button = driver.find_element_by_xpath('/html/body/div/footer/div/div/div/div[2]/button[2]/div')
    decline_button = driver.find_element_by_xpath('/html/body/div/footer/div/div/div/div[2]/button[1]/div')

    assert accept_button.is_enabled()
    assert decline_button.is_enabled()

    decline_button.click()

    time.sleep(2)

    # driver.refresh()
    driver.close()
    # driver.quit()

    time.sleep(2)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.set_window_rect(1200, 400, 1300, 1000)
    driver.get('http://localhost:1667/')
    time.sleep(1)

    accept_button = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
    decline_button = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div')

    assert not accept_button.is_enabled()
    assert not decline_button.is_enabled()

    driver.close()
