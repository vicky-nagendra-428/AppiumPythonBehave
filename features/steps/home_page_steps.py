
from behave import *
from page.home_page import HomePage


home_page = None


@given(u'I am on the app home page of the app')
def step_impl(context):
    global home_page
    home_page = HomePage()
    home_page.check_home_page_is_loaded()


@when(u'I enter the value "{1}" in text field 1')
def step_impl(context, value_to_enter):
    home_page.enter_the_value_in_field1(value_to_enter)


@when(u'I enter the value "{2}" in text field 2')
def step_impl(context, data_to_enter):
    home_page.enter_the_value_in_field2(data_to_enter)


@then(u'I click on the calculate sum')
def step_impl(context):
    home_page.click_the_compute_sum_button()


@then(u'I validate the sum is "{3}"')
def step_impl(context, value_to_check):
    home_page.validate_the_value_at_result(value_to_check)
