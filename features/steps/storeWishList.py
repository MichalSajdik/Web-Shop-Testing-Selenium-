

from behave import *

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



@given('a web page displaying details about product "{url}"')
def step_impl(context,url):

    context.webDriver.get(url)

@when('the user clicks on function Add to Wish List')
def step_impl(context):
    xpath = "// div[ @ id = 'content'] / div / div[2] / div / button"
    context.webDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    context.webDriver.find_element_by_xpath(xpath).click()
    # <selenium.webdriver.remote.webelement.WebElement (session="ed3ea46b-b373-4181-93fa-ef77c2c086fe", element="50061636-0a59-4f0b-a9ba-c0c51cf663ee")>

@then('a message informing of success is displayed')
def step_impl(context):
    # close button in xpath
    xpath = "(//button[@type='button'])[7]"
    try:
        context.webDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        context.webDriver.find_element_by_xpath(xpath).click()
    except Exception:
        assert False is True
    pass


@given('a logout page: "{urlLogoutPage}" is displayed')
def step_impl(context, urlLogoutPage):
    context.webDriver.get(urlLogoutPage)


@step('user went to registration page: "{urlRegisterPage}"')
def step_impl(context, urlRegisterPage):
    context.webDriver.get(urlRegisterPage)



@then('a "{urlAccountPage}" page is displayed')
def step_impl(context, urlAccountPage):
    print("current URL "+context.webDriver.current_url)
    print("should be "+urlAccountPage)
    assert context.webDriver.current_url == urlAccountPage



@when("the user clicks on Wish List")
def step_impl(context):
    xpath = "// a[ @ id = 'wishlist-total'] / i"
    context.webDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    context.webDriver.find_element_by_xpath(xpath).click()

@then('login page: "{url_login_page}" is displayed, because user is not logged in')
def step_impl(context, url_login_page):
    print("current URL " + context.webDriver.current_url)
    print("should be " + url_login_page)

    assert url_login_page == context.webDriver.current_url


# @given('wish list page: "{urlOfWishList}"')
# def step_impl(context, urlOfWishList):
#     context.webDriver.get("http://mys01.fit.vutbr.cz:8064/index.php?route=product/product&product_id=40")
#     xpath = "// div[ @ id = 'content'] / div / div[2] / div / button"
#     context.webDriver.find_element_by_xpath(xpath).click()
#
#     context.webDriver.get(urlOfWishList)
#
#
# @when("the user clicks on first delete button belonging to one of products")
# def step_impl(context):
#
#     model_xpath = "// div[ @ id = 'content'] / div / table / tbody / tr / td[3]"
#     model_data = context.webDriver.find_element_by_xpath(model_xpath)
#     context.model_data = model_data.text
#
#     xpath_delete = "//div[@id='content']/div/table/tbody/tr/td[6]/a/i"
#     context.webDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath_delete)))
#     context.webDriver.find_element_by_xpath(xpath_delete).click()
#     xpath_deleteF = "(//button[@type='button'])[9]"
#     context.webDriverWait.until(EC.element_to_be_clickable((By.XPATH, xpath_deleteF)))
#     context.webDriver.find_element_by_xpath(xpath_deleteF).click()
#
#
# @then("selected product is removed from wish list")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass
#
#
# @step("deleted product is not displayed anymore")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass