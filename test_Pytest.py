import time
import pytest
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class TestPytest:

    @pytest.mark.google
    def test_navigate_google(self, browser):
        browser.get("https://www.google.com")
        time.sleep(4)

    @pytest.mark.unittest
    def test_selenium_displayed(self, browser):
        browser.get("https://demoqa.com/buttons")
        browser.maximize_window()

        try:
            # Wait for the button to be clickable
            clickButton = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button"))
            )
            # Scroll to the button
            browser.execute_script("arguments[0].scrollIntoView(true);", clickButton)
            time.sleep(1)  # Allow time for any transitions to finish
            # Click the button
            clickButton.click()

            # Wait for the dynamic message to be displayed
            dynamicMessage = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.ID, "dynamicClickMessage"))
            )

            expectedResult = "You have done a dynamic click"
            actualResult = dynamicMessage.text
            assert expectedResult == actualResult, f"Expected '{expectedResult}', but got '{actualResult}'"

        except ElementClickInterceptedException as e:
            pytest.fail(f"ElementClickInterceptedException: {e}")
        finally:
            time.sleep(8)

    time.sleep(3)
if __name__ == '__main__':
    pytest.main()
