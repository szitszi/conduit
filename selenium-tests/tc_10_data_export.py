from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import os
import string

opt = Options()
opt.headless = False
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)
try:
    driver.get('http://localhost:1667/')

    time.sleep(2)

    input_data = ["".join([random.choice(string.ascii_lowercase) for _ in range(5)]), f"{random.choice(string.ascii_lowercase)}{random.randint(10, 1000)}@mail.hu", "Pw123456"]
    data_of_new_article = ["test_title", "test_about", f"test_article text{random.randint(10, 1000)}", "test_tag"]


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

    # ---------Log out-----------
    driver.find_element_by_xpath("//a[@active-class='active']").click()


    time.sleep(2)


    # ------Sign in---------
    def login_process():
        driver.find_element_by_xpath("//a[@href='#/login']").click()
        for i in range(len(input_data)-1):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i+1])
            time.sleep(1)
        driver.find_element_by_tag_name("button").click()

    login_process()

    time.sleep(2)

    # # -----------Export activities / first article-----------
    #
    # time.sleep(2)
    #
    # article_title_list = driver.find_elements_by_xpath("//div[@class='article-preview']/a/h1")
    # article_title_list[0].click()
    #
    # time.sleep(2)
    #
    # title = driver.find_element_by_tag_name("h1").text
    # article_text = driver.find_element_by_tag_name("p").text

    # *******1.version******
    # file_output_string = title + "\n" + article_text
    # # print(file_output_string)
    #
    # with open("article_content.txt", "w") as file:
    #     file.write(file_output_string)

    # *******2.version******
    # with open("article_content.txt", "w") as file:
    #     file.write(title + "\n" + article_text)
    #
    # driver.back()

    # -----------Export activities / all articles-----------

    if os.path.exists("../selenium_python_tests/all_articles_content.txt"):
        os.remove("../selenium_python_tests/all_articles_content.txt")
    else:
        pass

    article_title_list = driver.find_elements_by_xpath("//div[@class='article-preview']/a/h1")

    # for element in article_title_list: # így azért nem megy, mert a hiába menyünk vissza back-kelvagy a Home-mal az eredeti oldalra az ""article_title_list"" kikeresésünk nem működik
    #     print(len(article_title_list))
    #     element.click()
    #     time.sleep(2)
    #     title = driver.find_element_by_tag_name("h1").text
    #     article_text = driver.find_element_by_tag_name("p").text
    #     with open("all_articles_content.txt", "a") as file:
    #         file.write(title + "\n" + article_text + "\n\n")
    #     #driver.back()
    #     driver.find_element_by_xpath("//a[@href='#/']").click()
    #     time.sleep(3)

    for i in range(len(article_title_list)):
        article_title_list[i].click()
        time.sleep(2)
        serial_number = i + 1
        title = driver.find_element_by_tag_name("h1").text
        article_text = driver.find_element_by_tag_name("p").text
        with open("../selenium_python_tests/all_articles_content.txt", "a") as file:
            file.write(str(serial_number) + ". : " + title + "\n" + article_text + "\n\n")
        driver.back()
        time.sleep(2)
        article_title_list = driver.find_elements_by_xpath("//div[@class='article-preview']/a/h1")

finally:
    driver.close()



