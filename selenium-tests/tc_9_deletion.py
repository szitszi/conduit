from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
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
    data_of_first_article = [f"1_title_{random.randint(10, 1000)}", "1_about", "1_text", "1_tag"]
    data_of_second_article = [f"2_title_{random.randint(10, 1000)}", "2_about", "2_text", "2_tag"]


    # -----------Sign up----------
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


    # -----------First article-----------

    # driver.find_element_by_xpath("//a[@href='#/editor']").click()
    # time.sleep(2)

    # def writing_of_new_article_process():
    #     driver.find_element_by_xpath("//a[@href='#/editor']").click()
    #     for i in range(len(data_of_new_article)):
    #         if i < 2:
    #             driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(data_of_new_article[i])
    #             time.sleep(1)
    #         elif i == 2:
    #             driver.find_element_by_xpath(f"//fieldset[{i + 1}]/textarea").send_keys(data_of_new_article[i])
    #             time.sleep(1)
    #         elif i == 3:
    #             driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input").send_keys(data_of_new_article[i])
    #             time.sleep(1)
    #
    #     driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()


    def writing_of_new_article_process(input_title, input_about, input_text, input_tag):
        driver.find_element_by_xpath("//a[@href='#/editor']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys(input_title)
        driver.find_element_by_xpath("//input[starts-with(@placeholder,'What')]").send_keys(input_about)
        driver.find_element_by_xpath("//textarea[starts-with(@placeholder,'Write')]").send_keys(input_text)
        driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys(input_tag)
        driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

    writing_of_new_article_process(data_of_first_article[0], data_of_first_article[1], data_of_first_article[2], data_of_first_article[3])
    time.sleep(2)

    # -----------Check of appearance of first article-----------

    print(driver.find_element_by_tag_name("h1").text)
    assert driver.find_element_by_tag_name("h1").text == data_of_first_article[0]
    time.sleep(3)
    user = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
    user.click()
    time.sleep(3)
    assert len(driver.find_elements_by_xpath("//h1")) == 1
    time.sleep(3)
    # -----------Second article-----------

    writing_of_new_article_process(data_of_second_article[0], data_of_second_article[1], data_of_second_article[2], data_of_second_article[3])
    time.sleep(3)

    # -----------Check of appearance of second article-----------

    print(driver.find_element_by_tag_name("h1").text)
    assert driver.find_element_by_tag_name("h1").text == data_of_second_article[0]
    user.click()
    time.sleep(2)
    assert len(driver.find_elements_by_xpath("//h1")) == 2
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/a/h1").click()
    time.sleep(2)

    # -----------Deletion of article-----------
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/span/button").click()
    time.sleep(2)
    user.click()
    time.sleep(2)

    assert len(driver.find_elements_by_xpath("//h1")) == 1
    time.sleep(2)


finally:
    driver.close()