from behave import *
from selenium import webdriver


@given('launch google chrome')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open pointzi dashboard page')
def step_impl(context):
    context.driver.get("https://dashboard.pointzi.com/login")


@then('Enter email "{user}" and password "{pwd}')
def step_impl(context, user, pwd):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//input[@id='input_1']").send_keys(user)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//input[@id='input_2']").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()


@then('user must sucessfully login the dashboard page')
def step_impl(context):
    context.driver.implicitly_wait(20)
    status = context.driver.find_element_by_xpath("//img[@pz-cdn='$ctrl.options.logo']").is_displayed()
    assert status is True, "Test Passed"
