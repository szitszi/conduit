from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
# import random

options = Options()
options.headless = True
# options.add_argument('--disable-gpu')

def test_tc_11_log_out():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get('http://localhost:1667/')

    input_data = ["Sz", "Sz55@sz.hu", "Sz123456"]


    # -----------Sign up----------
    def registration_process():
        driver.find_element_by_xpath("//a[@href='#/register']").click()
        # time.sleep(2)
        for i in range(len(input_data)):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i])
            # time.sleep(2)
        driver.find_element_by_tag_name("button").click()

    registration_process()

    time.sleep(2)

    # Accept of welcome message
    driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

    time.sleep(2)

    navbar_item_2_logged_in = driver.find_element_by_xpath("//ul[@class='nav navbar-nav pull-xs-right']/li[2]/a/i").text
    print(navbar_item_2_logged_in)
    number_of_items_logged_in = len(driver.find_elements_by_xpath("//ul[@class='nav navbar-nav pull-xs-right']/li"))
    print(number_of_items_logged_in)
    # Log out
    driver.find_element_by_xpath("//a[@active-class='active']").click()

    # navbar_item_2_logged_out = ("//a[@href='#/editor']/i").text
    navbar_item_2_logged_out = driver.find_element_by_xpath("//ul[@class='nav navbar-nav pull-xs-right']/li[2]/a/i").text
    print(navbar_item_2_logged_out)
    number_of_items_logged_out = len(driver.find_elements_by_xpath("//ul[@class='nav navbar-nav pull-xs-right']/li"))
    print(number_of_items_logged_out)


    time.sleep(2)

    ### navbar_item_2_logged_in and navbar_item_2_logged_out are empty because of before/after, selenium does not work, we need css!?!

    driver.close()