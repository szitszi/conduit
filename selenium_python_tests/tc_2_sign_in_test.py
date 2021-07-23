from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True


# options.add_argument('--disable-gpu')

def test_tc_2_sign_in():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    input_data = ["testuser1", "testuser1@example.com", "Abcd123$"]

    # ------Sign in---------
    def login_process():
        driver.find_element_by_xpath("//a[@href='#/login']").click()
        for i in range(len(input_data) - 1):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i + 1])
            time.sleep(1)
        driver.find_element_by_tag_name("button").click()

    login_process()

    time.sleep(1)

    # --------Check of login name---------

    name_after_sign_up = driver.find_element_by_xpath("//li[@class='nav-item'][4]/a").text

    assert name_after_sign_up == input_data[0]

    time.sleep(2)

    driver.close()
