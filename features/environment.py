
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver


def before_all(context):
    __TIMEOUT = 15
    dp = {'browserName': 'firefox', 'marionette': 'true',
          'javascriptEnabled': 'true'}
    browser = webdriver.Remote(
        command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
        desired_capabilities=dp)
    context.webDriver = browser
    context.webDriverWait = WebDriverWait(browser, __TIMEOUT)