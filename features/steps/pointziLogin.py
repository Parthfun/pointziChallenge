from behave import *
from selenium import webdriver


@given('launch google chrome')
def launch_browser(context):
    #context.driver = webdriver.Chrome()
    context.driver = webdriver.Firefox()


@when('open pointzi dashboard page')
def step_impl(context):
    context.driver.get("https://dashboard.pointzi.com/login")


@then('Enter email "{user}" and password "{pwd}')
def step_impl(context, user, pwd):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//input[@id='input_1']").send_keys(user)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//input[@id='input_2']").send_keys(pwd)
    context.driver.implicitly_wait(20)


@when('Click on login button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
    #status = context.driver.find_element_by_xpath("//div[@class='md-toast-content']").is_displayed()
    status = context.driver.find_element_by_xpath("//img[@pz-cdn='$ctrl.options.logo']").is_displayed()
    if status:
        assert status is True, "Test Passed"
    else:
        assert status is False, "Test Failed"

