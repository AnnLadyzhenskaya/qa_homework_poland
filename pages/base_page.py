from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self):
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def is_visible(self, selector):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
        return element

    def is_field_empty(self, selector, selector_type=By.XPATH):
        element = self.driver.find_element(selector_type, selector)
        if element.text == "":
            return True
        else:
            return False

    def check_dynamic_text_on_page(self, selector, text):
        element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, selector), text))
        return element




