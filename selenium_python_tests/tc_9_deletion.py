from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://localhost:1667/')

input_data = ["Sz", "Sz48@sz.hu", "Sz123456"]
test_data_for_modification = "It's a test sentence."


# -----------Sign up----------
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

time.sleep(2)

# -----------Activities of settings-----------

main_window = driver.window_handles[0]
driver.find_element_by_xpath(f"//a[@href='#/@{input_data[0]}/']").click()



# # settings_window = driver.switch_to.window("settings")
# own_window = driver.window_handles[1]
# driver.switch_to.window(own_window)







time.sleep(3)



driver.close()