from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

opt = Options()
opt.headless = True


# options.add_argument('--disable-gpu')

def test_tc_6_new_article():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    input_data = ["testuser4", "testuser4@example.com", "Abcd123$"]
    data_of_new_article = [f"test_title{random.randint(10, 1000)}", "test_about", "test_article text", "test_tag"]

    # ------------Sign in--------------
    def login_process():
        driver.find_element_by_xpath("//a[@href='#/login']").click()
        for i in range(len(input_data) - 1):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i + 1])
            time.sleep(1)
        driver.find_element_by_tag_name("button").click()

    login_process()

    time.sleep(2)

    # -----------Activities of new article-----------

    def writing_of_new_article_process():
        driver.find_element_by_xpath("//a[@href='#/editor']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys(data_of_new_article[0])
        driver.find_element_by_xpath("//input[starts-with(@placeholder,'What')]").send_keys(data_of_new_article[1])
        driver.find_element_by_xpath("//textarea[starts-with(@placeholder,'Write')]").send_keys(data_of_new_article[2])
        driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys(data_of_new_article[3])
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

    writing_of_new_article_process()

    time.sleep(2)

    # -----------Check of appearene of new article-----------

    print(driver.find_element_by_tag_name("h1").text)
    assert driver.find_element_by_tag_name("h1").text == data_of_new_article[0]

    driver.close()
