from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://localhost:1667/')

input_data = ["Eper", "eper989@sz.com", "Pw123456"]
sign_up = driver.find_element_by_xpath("//a[@href='#/register']")
sign_up.click()

# -----------Sign up----------
def registration_process():
    sign_up.click()
    # time.sleep(2)
    for i in range(len(input_data)):
        driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i])
        # time.sleep(2)
    driver.find_element_by_tag_name("button").click()


registration_process()

time.sleep(1)


# --------Accept of welcome message----------
assert driver.find_element_by_class_name("swal-text").text == "Your registration was successful!"

time.sleep(1)

# driver.find_element_by_xpath("//div[@class='swal-overlay swal-overlay--show-modal']/div/div[4]/div/button").click()
driver.find_element_by_xpath("//div[@tabindex='-1']/div/div[4]/div/button").click()

time.sleep(1)

# name_after_sign_up = driver.find_element_by_xpath("//ul[class='nav navbar-nav pull-xs-right']//li[4]/a").text
# name_after_sign_up = driver.find_element_by_xpath(f"//a[text()=' {input_data[0]}']")
# //*[@id="app"]/nav/div/ul/li[4]/a
# name_after_sign_up = driver.find_element_by_xpath("//*[@id="app"]/nav/div/ul/li[4]/a").text
# name_after_sign_up = driver.find_element_by_xpath("//div[@class='container']//ul/li[4]").text

# --------Check of login name---------
name_after_sign_up = driver.find_element_by_xpath(f"//a[@href='#/@{input_data[0]}/']").text
print(name_after_sign_up)

assert name_after_sign_up == input_data[0]

time.sleep(1)
#
driver.close()

# div/button
# class => swal-button swal-button--confirm, text: OK

# input_field_username = driver.find_element_by_xpath("//fieldset[1]/input")
# input_field_username.send_keys("mita")
#
# input_field_email = driver.find_element_by_xpath("//fieldset[2]/input")
# input_field_email.send_keys("mita")
#
# input_field_password = driver.find_element_by_xpath("//fieldset[3]/input")
# input_field_password.send_keys("mita")
#
#
# driver.find_element_by_tag_name("button").click()
