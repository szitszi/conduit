from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

options = Options()
options.headless = True
# options.add_argument('--disable-gpu')

def test_tc_5_pages():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get('http://localhost:1667/')

    input_data = ["Sz", f"Sz{random.randint(10, 1000)}@sz.hu", "Sz123456"]
    number_of_pages = 2


    # ------------------Sign up-----------------
    def registration_process():
        driver.find_element_by_xpath("//a[@href='#/register']").click()
        for i in range(len(input_data)):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i])
        driver.find_element_by_tag_name("button").click()


    registration_process()

    time.sleep(2)

    # --------Accept of welcome message----------
    driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

    time.sleep(2)


    # -----------Pagination-----------


    pagination = driver.find_element_by_xpath("//ul[@class='pagination']")
    pages = driver.find_elements_by_class_name("page-link")
    print(len(pages))

    for page in pages:
        page.click()
        time.sleep(1)

    driver.close()