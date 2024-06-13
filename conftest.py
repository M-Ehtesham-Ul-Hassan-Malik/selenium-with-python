import pytest
from selenium import webdriver


@pytest.fixture(scope="session")

# Scopes Types
# "session" will run all test and launch browser once,
# "function" will run test case one by one & re launch browser for every test case,
# "class" will launch browser for each class
# "module" will launch browser for each module

def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
