from selenium import webdriver
import time

def test_tc_3_gdpr():

    driver = webdriver.Chrome()

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