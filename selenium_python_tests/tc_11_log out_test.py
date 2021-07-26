from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

opt = Options()
opt.headless = True


# options.add_argument('--disable-gpu')

def test_tc_11_log_out():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    time.sleep(2)

    input_data = ["".join([random.choice(string.ascii_lowercase) for _ in range(5)]),
                  f"{random.choice(string.ascii_lowercase)}{random.randint(10, 1000)}@mail.hu", "Pw123456"]

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

    # --------Check of login name---------
    login_name = driver.find_element_by_xpath("//li[@class='nav-item'][4]/a")
    print(login_name.text)
    assert login_name.text == input_data[0]

    # --------Log out process---------
    """check navbar items before log out"""
    navbar_elements_before = driver.find_elements_by_xpath("//*[@id='app']/nav/div/ul/li/a")
    # print(len(navbar_elements_before))
    for element in navbar_elements_before:
        print(element.text)
    assert navbar_elements_before[3].text == input_data[0]

    log_out_link = driver.find_element_by_xpath("//a[@active-class='active']")
    log_out_link.click()

    # if log_out_link.is_enabled():
    #     print("log out was clicked")
    #     log_out_link.click()
    # else:
    #     print("error")

    """check navbar items after log out"""
    navbar_elements_after = driver.find_elements_by_xpath("//*[@id='app']/nav/div/ul/li/a")
    # print(len(navbar_elements_after))
    for element in navbar_elements_after:
        print(element.text)
    assert navbar_elements_after[2].text == "Sign up"

    time.sleep(2)

    driver.close()
