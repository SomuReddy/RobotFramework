from selenium import webdriver
import pytest
import time


class Amazon(object):

    @pytest.fixture(scope="session")
    def search(self):
        baseurl = "https://www.amazon.in"
        #driver = webdriver.Firefox()
        #driver = webdriver.Chrome()
        #driver = webdriver.Ie()
        driver = webdriver.Edge()
        driver.get(baseurl)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_id("twotabsearchtextbox").send_keys("iPhone 8")
        #driver.find_element_by_xpath("//span[@id='nav-search-submit-text']").click()
        driver.find_element_by_xpath("//input[@type='submit' and @value='Go']").click()
        parent_handle=driver.current_window_handle
        time.sleep(2)
        driver.find_element_by_xpath("//h2[text()='Apple iPhone 8 (Space Grey, 64GB)']").click()
        time.sleep(3)
        handles = driver.window_handles
        for handle in handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_id("add-to-cart-button").click()
                time.sleep(5)
                break
        driver.switch_to.window(parent_handle)
        driver.close()


out = Amazon()
out.search()