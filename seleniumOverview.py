import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


# def browser(): Ensure you have the ChromeDriver executable in your PATH or specify the path explicitly
# chrome_driver = webdriver.Chrome()  # If necessary, provide the path to ChromeDriver executable: webdriver.Chrome(
# executable_path='/path/to/chromedriver') edge_driver = webdriver.Edge() chrome_driver.get(
# "https://www.selenium.dev/") print("Chrome initiated") chrome_driver.quit()  # It's good practice to quit the
# browser after use

# if __name__ == '__main__':
#    browser()


# def selenium_textbox():
#     driver = webdriver.Chrome()
#     driver.get("https://facebook.com/")
#     firstname = driver.find_element(By.ID, "email")
#     firstname.send_keys("john")
#     time.sleep(5)
#     firstname.clear()
#     time.sleep(5)
#     #get tag name
#     print(firstname.tag_name)



# if __name__ == '__main__':
#
#     selenium_textbox()





def selenium_displayed():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/buttons")
    driver.maximize_window()

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

        if dynamicMessage.is_displayed():
            print("Element displayed")
        else:
            print("Element not displayed")

        expectedResult = "You have done a dynamic click"
        actualResult = dynamicMessage.text
        assert expectedResult == actualResult
        time.sleep(8)

    except ElementClickInterceptedException as e:
        print(f"ElementClickInterceptedException: {e}")
    finally:
        driver.quit()


if __name__ == '__main__':
    selenium_displayed()
