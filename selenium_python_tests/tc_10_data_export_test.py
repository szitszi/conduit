from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import os
import string

opt = Options()
opt.headless = True
# options.add_argument('--disable-gpu')


def test_tc_10_data_export():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    input_data = ["".join([random.choice(string.ascii_lowercase) for _ in range(5)]), f"{random.choice(string.ascii_lowercase)}{random.randint(10, 1000)}@mail.hu", "Pw123456"]


    # -----------Sign up----------
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


    # -----------Export activities / all articles-----------

    time.sleep(2)

    if os.path.exists("all_articles_content.txt"):
        os.remove("all_articles_content.txt")
    else:
        pass

    article_title_list = driver.find_elements_by_xpath("//div[@class='article-preview']/a/h1")

    for i in range(len(article_title_list)):
        article_title_list[i].click()
        time.sleep(2)
        serial_number = i + 1
        title = driver.find_element_by_tag_name("h1").text
        article_text = driver.find_element_by_tag_name("p").text
        with open("all_articles_content.txt", "a") as file:
            file.write(str(serial_number) + ". : " + title + "\n" + article_text + "\n\n")
        driver.back()
        time.sleep(2)
        article_title_list = driver.find_elements_by_xpath("//div[@class='article-preview']/a/h1")

    driver.close()
