from selenium import webdriver
import time
import random

driver = webdriver.Chrome()

driver.get('http://localhost:1667/')

input_data = ["Sz", f"Sz{random.randint(10, 1000)}@sz.hu", "Sz123456"]
data_of_new_article = ["test_title", "test_about", "test_article text", "test_tag"]


# Sign up
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

# -----------Activities of new article-----------

# main_window = driver.window_handles[0]
time.sleep(2)
driver.find_element_by_xpath("//a[@href='#/editor']").click()
time.sleep(2)

def writing_of_new_article_process():
    driver.find_element_by_xpath("//a[@href='#/editor']").click()
    for i in range(len(data_of_new_article)):
        # if i != 2:
        if i < 2:
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(data_of_new_article[i])
            time.sleep(1)
        elif i == 2:
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/textarea").send_keys(data_of_new_article[i])
            time.sleep(1)
        elif i == 3:
            driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input").send_keys(data_of_new_article[i])
            time.sleep(1)
    driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

writing_of_new_article_process()

# -----------Check of appearene of new article-----------
time.sleep(2)
# driver.find_element_by_xpath((f"//a[@href='#/@{input_data[0]}/']")).click()
# time.sleep(5)

driver.close()