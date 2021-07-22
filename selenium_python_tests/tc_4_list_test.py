from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

options = Options()
options.headless = True
# options.add_argument('--disable-gpu')

def test_tc_4_list():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_rect(800, 100, 600, 800)

    driver.get('http://localhost:1667/')

    input_data = ["Sz", f"Sz{random.randint(10, 1000)}@sz.hu", "Sz123456"]
    data_of_new_article = ["test_title", "test_about", f"test_article text{random.randint(10, 1000)}", "test_tag"]


    # --------Sign up----------
    def registration_process():
        driver.find_element_by_xpath("//a[@href='#/register']").click()
        # time.sleep(2)
        for i in range(len(input_data)):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i])
            # time.sleep(2)
        driver.find_element_by_tag_name("button").click()

    registration_process()

    time.sleep(4)

    # --------Accept of welcome message----------
    driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

    time.sleep(2)

    # -----------Export activities-----------

    article_title_list = driver.find_elements_by_xpath("//div[@class='article-preview']/a/h1")
    for item in article_title_list:
        print(item.text)

    time.sleep(2)

    driver.close()