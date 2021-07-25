from selenium import webdriver
import time
import random
import csv


driver = webdriver.Chrome()

driver.get('http://localhost:1667/')
driver.set_window_rect(800, 100, 600, 800)

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

time.sleep(3)

# --------Accept of welcome message----------
driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

time.sleep(2)

# -----------Import input data-----------

def writing_of_new_article_process(input_title, input_about, input_text, input_tag):
    driver.find_element_by_xpath("//a[@href='#/editor']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys(input_title)
    driver.find_element_by_xpath("//input[starts-with(@placeholder,'What')]").send_keys(input_about)
    driver.find_element_by_xpath("//textarea[starts-with(@placeholder,'Write')]").send_keys(input_text)
    driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys(input_tag)
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()
    time.sleep(1)


with open('import_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        writing_of_new_article_process(row[0], row[1], row[2], row[3])


time.sleep(1)


driver.close()