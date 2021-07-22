from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = True
# options.add_argument('--disable-gpu')

def test_tc_3_gdpr():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get('http://localhost:1667/')

    time.sleep(2)

    # ----------Accept cookies---------
    #
    # driver.find_element_by_xpath("//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--accept']").click()
    #
    # time.sleep(2)

    # driver.close()


    # -----------Decline cookies---------

    driver.find_element_by_xpath("//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--decline']").click()

    time.sleep(2)

    driver.close()