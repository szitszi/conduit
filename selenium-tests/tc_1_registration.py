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

    time.sleep(5)

    input_data = ["".join([random.choice(string.ascii_lowercase) for _ in range(5)]),
                  f"{random.choice(string.ascii_lowercase)}{random.randint(10, 1000)}@mail.hu", "Pw123456"]

    # sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
    # sign_up.click()


    # -----------Sign up----------
    def registration_process():
        sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
        sign_up.click()
        for i in range(len(input_data)):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i])
        driver.find_element_by_tag_name("button").click()


    registration_process()

    time.sleep(2)

    # --------Accept of welcome message----------
    assert driver.find_element_by_class_name("swal-text").text == "Your registration was successful!"

    time.sleep(2)

    driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

    time.sleep(2)

    # --------Check of login name---------
    # name_after_sign_up = driver.find_element_by_xpath(f"//a[@href='#/@{input_data[0]}/']").text
    name_after_sign_up = driver.find_element_by_xpath("//li[@class='nav-item'][4]/a").text
    print(name_after_sign_up)

    assert name_after_sign_up == input_data[0]

    time.sleep(1)

finally:
    driver.close()
