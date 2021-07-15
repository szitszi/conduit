from selenium import webdriver
import time
import random

driver = webdriver.Chrome()

driver.get('http://localhost:1667/')

input_data = ["Sz", f"Sz{random.randint(10, 1000)}@sz.hu", "Sz123456"]
number_of_pages = 6


# ------------------Sign up-----------------
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
    for i in range(len(input_data) - 1):
        driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i + 1])
        time.sleep(1)
    driver.find_element_by_tag_name("button").click()


login_process()

# -----------Pagination-----------

time.sleep(5)

pagination = driver.find_element_by_xpath("//ul[@class='pagination']")
pages = driver.find_elements_by_class_name("page-link")
print(len(pages))

for page in pages:
    page.click()
    time.sleep(1)

driver.close()
