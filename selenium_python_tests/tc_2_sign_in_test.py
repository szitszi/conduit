from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = True
# options.add_argument('--disable-gpu')

def test_tc_2_sign_in():


    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get('http://localhost:1667/')

    input_data = ["Sz", "Sz43@sz.hu", "Sz123456"]


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

    # # --------Check of login name---------
    # name_after_sign_in = driver.find_element_by_xpath(f"//a[@href='#/@{input_data[0]}/']").text
    # # name_after_sign_in = driver.find_element_by_xpath("//a[@href='#/@Sz/']").text
    # print(name_after_sign_in)

    # assert name_after_sign_in == input_data[0]

    time.sleep(2)

    driver.close()