from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True


# options.add_argument('--disable-gpu')

def test_tc_4_list():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    driver.get('http://localhost:1667/')

    input_data = ["testuser2", "testuser2@example.com", "Abcd123$"]

    # ------Sign in---------
    def login_process():
        driver.find_element_by_xpath("//a[@href='#/login']").click()
        for i in range(len(input_data) - 1):
            driver.find_element_by_xpath(f"//fieldset[{i + 1}]/input").send_keys(input_data[i + 1])
            time.sleep(1)
        driver.find_element_by_tag_name("button").click()

    login_process()

    time.sleep(2)

    # -----------Making list-----------
    global_feed = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a')
    global_feed.click()
    time.sleep(5)
    article_title_list = driver.find_elements_by_xpath("//a/h1")
    for item in article_title_list:
        print(item.text)

    print(len(article_title_list))
    assert len(article_title_list) == 11

    time.sleep(2)

    driver.close()
