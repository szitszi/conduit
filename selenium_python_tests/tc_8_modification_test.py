from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

options = Options()
options.headless = True
# options.add_argument('--disable-gpu')

def test_tc_8_modification():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get('http://localhost:1667/')

    # input_data = ["Sz", "Sz4@sz.hu", "Sz123456"]
    input_data = ["Sz", f"Sz{random.randint(10, 1000)}@sz.hu", "Sz123456"]
    test_data_for_modification = "It's a test sentence."

    print(random.randint(10, 1000))


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

    # --------Accept of welcome message----------
    driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

    time.sleep(2)



    # -----------Activities of settings-----------


    driver.find_element_by_xpath("//a[@href='#/settings']").click()
    time.sleep(2.0)
    driver.find_element_by_tag_name("textarea").send_keys(test_data_for_modification)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()
    time.sleep(2.0)
    driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()



    time.sleep(3)



    driver.close()