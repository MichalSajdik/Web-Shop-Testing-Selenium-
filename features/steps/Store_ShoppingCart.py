from behave import *
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher("re")


@given("a web browser is displaying details about product")
def step_impl(context):
    url_of_product = "http://mys01.fit.vutbr.cz:8064/index.php?route=product/product&product_id=41"
    context.webDriver.get(url_of_product)
    # pass

@when("the user clicks Add to Cart")
def step_impl(context):
    context.webDriverWait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    context.webDriver.find_element_by_id("button-cart").click()

@then("product is added to cart")
def step_impl(context):
    xpath = "// div[ @ id = 'cart'] / button"
    cart_total = context.webDriver.find_element_by_xpath(xpath).text
    print("HERE>>>> "+ cart_total)
    assert cart_total[0] == "1"
    pass

@step("message informing about successful operation is displayed")
def step_impl(context):
    xpath = "// button[contains(., '×')]"
    try:
        context.webDriver.find_element_by_xpath(xpath).click()
    except ElementNotInteractableException:
        assert False is True
    pass


@given("logged in account")
def step_impl(context):
    context.webDriver.get("http://mys01.fit.vutbr.cz:8064/index.php?route=account/login")
    pass


@step("all required information is filled in")
def step_impl(context):
    context.webDriverWait.until(EC.element_to_be_clickable((By.ID, "input-quantity")))
    context.webDriver.find_element_by_id("input-quantity").send_keys("1")
    pass


@step('Qty value is set to "66666666666666666"')
def step_impl(context):
    context.webDriverWait.until(EC.element_to_be_clickable((By.ID, "input-quantity")))
    context.webDriver.find_element_by_id("input-quantity").send_keys("66666666666666666")
    pass


@then('quantity in shopping cart should be "66666666666666666" or apropriate warning should be showed')
def step_impl(context):
    xpath = "// div[ @ id = 'cart'] / button"
    cart_total = context.webDriver.find_element_by_xpath(xpath).text
    cart_total = cart_total[:17]
    assert cart_total == "66666666666666666"
    pass


@given("a web browser is at the opencart home page")
def step_impl(context):
    context.webDriver.get("http://mys01.fit.vutbr.cz:8064/index.php?route=common/home")
    pass


@step("user added item to shopping cart")
def step_impl(context):
    xpath="//div[@id='content']/div[2]/div[2]/div/div[3]/button/span"
    context.webDriver.find_element_by_xpath(xpath).click()
    pass


@when("the user clicks at cart total")
def step_impl(context):
    xpath = "// div[ @ id = 'cart'] / button"
    context.webDriver.find_element_by_xpath(xpath).click()
    pass


@then("a popup is dispalyed with content of products in shopping cart")
def step_impl(context):
    xpath = "// div[ @ id = 'cart'] / button"
    button_element = context.webDriver.find_element_by_xpath(xpath)
    popup = button_element.get_attribute("aria-expanded")
    assert popup == "true"
    pass



@when('the user clicks at "View cart"')
def step_impl(context):
    context.webDriver.find_element_by_css_selector("a:nth-child(1) > strong").click();
    pass


@then("web page of shopping cart is displayed")
def step_impl(context):
    print(context.webDriver.current_url)
    assert context.webDriver.current_url == "http://mys01.fit.vutbr.cz:8064/index.php?route=checkout/cart"
    pass


@when("the user clicks at shopping cart button")
def step_impl(context):
    context.webDriver.find_element_by_css_selector("a > .fa-shopping-cart").click();
    pass


@step("web page of shopping cart in displayed")
def step_impl(context):
    context.webDriver.get("http://mys01.fit.vutbr.cz:8064/index.php?route=checkout/cart")
    pass


@when("the user clicks at the remove button")
def step_impl(context):
    context.webDriver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click();
    pass


@then("item is removed from shopping card")
def step_impl(context):
    try:
        context.webDriver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click();
        assert False is True
    except Exception:
        assert True is True
    pass

@step('Qty value is set to "not valid value"')
def step_impl(context):
    context.webDriverWait.until(EC.element_to_be_clickable((By.ID, "input-quantity")))
    context.webDriver.find_element_by_id("input-quantity").send_keys("not valid value")
    pass


@then("error message is displayed to user")
def step_impl(context):
    try:
        WebDriverWait(context.webDriver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
        alert = context.webDriver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")
        assert True == False
    pass