"""
Practical Exercise 2

Title
Automate Myntra Product Selection

Description
Open the Myntra website using Selenium WebDriver (https://www.myntra.com/).

Automate the process of navigating categories, selecting a product, applying filters, sorting products and adding to bag.

Perform the following steps:
- Launch the browser and open the Myntra website
- Maximize the browser window
- Hover over the Gen-z category
- Click on **"Jackets Under ₹899"**
- Select any 2 filter under the product filters (e.g., brand, size, or color)
- Click on the **Sort By** 'Popularity'
- Click on the any one product
- Select size (if mentioned)
- Add to bag
Use appropriate locator strategies such as **XPath / CSS Selectors** and implement **ActionChains** for hovering and clicking.

Students should ensure that:
- The website opens successfully
- The hover over the Gen-z category works correctly
- The correct subcategory is clicked
- Filters and sorting are applied successfully
- The specific product is selected and added to bag without errors

### Expected Outcome
- The browser launches and opens Myntra website
- Hovering over Gen-z displays the subcategory
- **Jackets Under ₹899 is clicked successfully
- 2 filter checkbox is selected
- Products are sorted according to the chosen option
- The specified product is clicked and displayed
- The product is added to bag
- Script executes smoothly without error
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Setup browser
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#Maximize the window
driver.maximize_window()

#implicit wait
wait = WebDriverWait(driver, 30)

#opening the myntra website
driver.get("https://www.myntra.com/")
sleep(2)

#1. Hover on GENZ (or Men if GENZ not visible)
genz = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Genz']")))
ActionChains(driver).move_to_element(genz).perform()

# 2. Click "Jackets Under ₹899"
Jackets = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Jackets Under')]")))
Jackets.click()

# 3. Apply Filters (Select any 2 safely)
Filters = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "common-customCheckbox")))
Filters[0].click()
Filters[1].click()

# 4. Sort by Popularity
Sort = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sort by')]")))
Sort.click()

Popularity = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Popularity')]")))
Popularity.click()

# 5. Click first product
Product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-base")))
Product.click()

# 6. Switch to new tab
driver.switch_to.window(driver.window_handles[1])

# 7. Select size if available
Size = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "size-buttons-size-button")))
Size.click()

# 8. Add to bag
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='ADD TO BAG']"))).click()

# Sleep to observe results and then quit the browser window.
sleep(30)
driver.quit()
