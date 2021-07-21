from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')

def test_tc_1_registration():

    driver = webdriver.Chrome(chrome_options=options)


    driver.get('http://localhost:1667/')

    input_data = ["Eper", "eper989@sz.com", "Pw123456"]
    sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
    sign_up.click()


    # -----------Sign up----------
    def registration_process():
        sign_up.click()
        for i in range(len(input_data)):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i])
        driver.find_element_by_tag_name("button").click()


    registration_process()

    time.sleep(4)

    # --------Accept of welcome message----------
    assert driver.find_element_by_class_name("swal-text").text == "Your registration was successful!"

    time.sleep(4)

    driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

    time.sleep(1)

    # --------Check of login name---------
    name_after_sign_up = driver.find_element_by_xpath(f"//a[@href='#/@{input_data[0]}/']").text
    print(name_after_sign_up)

    assert name_after_sign_up == input_data[0]

    time.sleep(1)

    driver.close()
