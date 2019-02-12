from page.basepage import Base


class HomePage(Base):

    def __init__(self):
        super(HomePage, self).__init__()
        self.driver = self.base_driver

        self.test_field_1 = {'method': 'xpath', 'value': '//XCUIElementTypeTextField[@name="IntegerA"]'}
        self.test_field_2 = {'method': 'accessibility_id', 'value': 'IntegerB'}
        self.compute_sum = {'method': 'accessibility_id', 'value': 'ComputeSumButton'}
        self.answer = {'method': 'accessibility_id', 'value': 'Answer'}

    def check_home_page_is_loaded(self):
        self.wait_for_element_visibility(self.test_field_1)

    def enter_the_value_in_field1(self, data_to_enter):
        self.enter_data_in(self.test_field_1, data_to_enter)

    def enter_the_value_in_field2(self, data_to_enter):
        self.enter_data_in(self.test_field_2, data_to_enter)

    def click_the_compute_sum_button(self):
        self.click_the_element(self.compute_sum)

    def validate_the_value_at_result(self, value_for_validation):
        actual_text = self.get_text(self.answer)
        assert(actual_text, value_for_validation)
