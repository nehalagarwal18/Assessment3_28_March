"""
Practical Exercise 1
Title
Automate Product Selection and Delivery Check on ShoppersStack

#Description
Open the ShoppersStack website using Selenium WebDriver (https://www.shoppersstack.com/).

Automate the process of selecting a product category and verifying delivery availability using a pincode.

Perform the following steps:
- Launch the browser and open the ShoppersStack website
- Maximize the browser window
- Click on the **"APPLE"** product category
- Locate the delivery input field and enter the pincode
- Click on the **"Check"** button

Use appropriate locator strategies such as **XPath / ID / CSS Selectors** for identifying elements.
Implement synchronization using both **Implicit Wait** and **Explicit Wait**.

Students should ensure that:
- The website loads successfully
- The **APPLE** category is clicked correctly
- The pincode is entered in the delivery field
- Explicit wait is properly implemented
- The script runs without timing issues or exceptions
- Proper locator strategies are used

Expected Outcome
- The browser launches and opens the ShoppersStack website
- The **APPLE** category page is displayed
- The pincode  is entered successfully
- The **Check** button is clicked after becoming clickable
- Delivery check process is triggered
- Script executes smoothly without errors
"""
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait

# Browser setup
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

# open the Shopperstack website
driver.get("https://www.shoppersstack.com/")

# maximize the window
driver.maximize_window()

# # implicit wait
driver.implicitly_wait(100)
#
# # Opening shopper stack website
driver.get('https://www.shoppersstack.com/')

#  # Maximize the browser
driver.maximize_window()

# Creating an object for action chains
actions = ActionChains(driver)

# Creating an element for the Apple product
ele = driver.find_element(By.XPATH,'//img[@alt="iphone"]')

# scrolling and clicking the element
actions.scroll_to_element(ele).pause(2).click(ele).perform()

# Locate the delivery input field and entering the pincode
driver.find_element(By.XPATH,'//input[@id="Check Delivery"]').send_keys('305001')
sleep(2)

 # Clicking on submit
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(2)

#  Closing the browser
driver.close()

