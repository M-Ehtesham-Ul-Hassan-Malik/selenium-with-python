import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException



class MySetup(unittest.TestCase):

    def shortDescription(self):
        return "This is loggin function"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/buttons")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

# @unittest.skip("wont acccept ")
class MyTestCase(MySetup):


#    @unittest.skip("update comming")  #this syntax is used to skip the test
    def test_selenium_displayed(self):
        shortDiscription = self.shortDescription()
        print("Short description: ", shortDiscription)
        driver = self.driver
        try:
            # Wait for the button to be clickable
            clickButton = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button"))
            )
            # Scroll to the button
            driver.execute_script("arguments[0].scrollIntoView(true);", clickButton)
            time.sleep(1)  # Allow time for any transitions to finish
            # Click the button
            clickButton.click()

            # Wait for the dynamic message to be displayed
            dynamicMessage = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "dynamicClickMessage"))
            )

            expectedResult = "You have done a dynamic click"
            actualResult = dynamicMessage.text
            self.assertEqual(expectedResult, actualResult)

        except ElementClickInterceptedException as e:
            self.fail(f"ElementClickInterceptedException: {e}")
        finally:
            time.sleep(8)


    def test2(self):
        pass

    def test3(self):
        pass


if __name__ == '__main__':
    unittest.main()
