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

    input_data = ["".join([random.choice(string.ascii_lowercase) for _ in range(5)]),
                  f"{random.choice(string.ascii_lowercase)}{random.randint(10, 1000)}@mail.hu", "Pw123456"]
    test_data_for_modification = "It's a test sentence."


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

    time.sleep(2)

    # -----------Activities of settings-----------
    driver.find_element_by_xpath("//a[@href='#/settings']").click()
    time.sleep(2.0)
    driver.find_element_by_tag_name("textarea").send_keys(test_data_for_modification)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()
    time.sleep(2.0)
    driver.find_element_by_xpath("//button[@class='swal-button swal-button--confirm']").click()

    assert driver.find_element_by_tag_name("textarea").get_attribute("value") == test_data_for_modification
    print(f"Text of bio: {driver.find_element_by_tag_name('textarea').get_attribute('value')}")

    time.sleep(3)

finally:
    driver.close()
