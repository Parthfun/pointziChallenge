from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


@then('open pointzi dashboard page')
def step_impl(context):
    context.driver.get("https://dashboard.pointzi.com/")


@then('click on register')
def step_impl(context):
    context.driver.implicitly_wait(1000)
    register = WebDriverWait(context.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                            "normalize-space("
                                                                                            ")='Register']")))
    register.click()
    #context.driver.find_element_by_xpath("//button[normalize-space()='Register']").click()


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
    element = context.driver.find_element_by_xpath("//md-checkbox[@name='terms']")
    action = ActionChains(context.driver)
    action.click(on_element=element)
    action.perform()


@then('click sign up')
def step_impl(context):
    context.driver.implicitly_wait(10000)
    context.driver.find_element_by_class_name("ng-scope material-icons").click()
    element = WebDriverWait(context.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                                                            "normalize-space()='Sign "
                                                                                            "up']")))
    element.click()
    status = context.driver.find_element_by_xpath("//div[@class='logo-wrapper']").is_displayed()
    if status:
        assert status is False, "Test Failed"
    else:
        assert status is True, "Test Passed"


@then('user is successfully signed up')
def step_impl(context):
    context.driver.implicitly_wait(20)
    status = context.driver.find_element_by_xpath("//img[@pz-cdn='$ctrl.options.logo']").is_displayed()
    assert status is True, "Test Passed"
