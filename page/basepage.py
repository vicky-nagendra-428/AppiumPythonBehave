from commonFunctions.config import ConfigSetup as Config
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:

    def __init__(self):
        config = Config()
        config.launch_app()
        self.base_driver = config.get_driver()

    def generate_element_identification_method(self, element_identifier_type):
        if element_identifier_type == 'id':
            return MobileBy.ID
        elif element_identifier_type == 'name':
            return MobileBy.NAME
        elif element_identifier_type == 'xpath':
            return MobileBy.XPATH
        elif element_identifier_type == 'class name':
            return MobileBy.CLASS_NAME
        elif element_identifier_type == 'accessibility_id':
            return MobileBy.ACCESSIBILITY_ID

    # this method accepts element dictionary with element identification method and its value
    def get_element(self, element):
        element_identification_method = self.generate_element_identification_method(element['method'])
        return self.base_driver.find_element(element_identification_method, element['value'])

    def get_elements(self, element):
        element_identification_method = self.generate_element_identification_method(element['method'])
        return self.base_driver.find_elements(element_identification_method, element['value'])

    def wait_for_element_visibility(self, element):
        element_identifier_type = element['method']
        element_identifier_value = element['value']
        WebDriverWait(self.base_driver, 20).until(
            ec.visibility_of_element_located((self.generate_element_identification_method(element_identifier_type),
                                             element_identifier_value)))

    def wait_for_element_clickable(self, element):
        element_identifier_type = element['method']
        element_identifier_value = element['value']
        return WebDriverWait(self.base_driver, 20).until(
            ec.element_to_be_clickable(
                (self.generate_element_identification_method(element_identifier_type), element_identifier_value)))

    def enter_data_in(self, element, data_to_enter):
        self.get_element(element).send_keys(data_to_enter)

    def click_the_element(self, element):
        captured_element = self.wait_for_element_clickable(element)
        captured_element.click()

    def get_text(self, element):
        return self.get_element(element).text
