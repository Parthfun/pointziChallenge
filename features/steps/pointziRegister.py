from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select


@then('open pointzi dashboard page')
def step_impl(context):
    context.driver.get("https://dashboard.pointzi.com/")


@then('click on register')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_xpath("//button[normalize-space()='Register']").click()


@then('Enter email "{email}" password "{passs}" and confirm password "{confirmpass}"')
def step_impl(context, email, passs, confirmpass):
    context.driver.find_element_by_xpath("//input[@id='input_5']").send_keys(email)
    context.driver.find_element_by_xpath("//input[@id='input_6']").send_keys(passs)
    context.driver.find_element_by_xpath("//input[@id='input_7']").send_keys(confirmpass)


@then('click next')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_xpath("//button[normalize-space()='Next']").click()


@then('select role and No. of app users')
def step_impl(context):
    context.driver.implicitly_wait(20)
    (context.driver.find_element_by_xpath("//md-select[@id='select_8']").click())
    context.driver.find_element_by_xpath("//md-option[@id='select_option_16']").click()
    context.driver.find_element_by_xpath("//md-select[@id='select_10']").click()
    context.driver.find_element_by_xpath("//md-option[@id='select_option_22']").click()


@then('Enter First name "{firstname}" Lastname "{lastname}" Company name "{cname}" and phone number ""')
def step_impl(context, lastname, firstname, cname):
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_xpath("//input[@id='input_12']").send_keys(firstname)
    context.driver.find_element_by_xpath("//input[@id='input_13']").send_keys(lastname)
    context.driver.find_element_by_xpath("//input[@id='input_14']").send_keys(cname)
    context.driver.find_element_by_xpath("//md-checkbox[@name='terms']").click()

@then(u'click sign up')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()


@then('wait')
def step_impl(context):
    context.driver.implicitly_wait(50)
    context.driver.find_element_by_xpath("//md-select[@id='select_12']")


@then('user is successfully signed up')
def step_impl(context):
    context.driver.implicitly_wait(20)
    status = context.driver.find_element_by_xpath("//img[@pz-cdn='$ctrl.options.logo']").is_displayed()
    assert status is True, "Test Passed"
