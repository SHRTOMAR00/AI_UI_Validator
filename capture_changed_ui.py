from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)
# Enter incorrect username & password
driver.find_element("id", "user-name").send_keys("standard_user")
driver.find_element("id", "password").send_keys("secret_sauce")
driver.find_element("id", "login-button").click()
time.sleep(2)
# Add a product to the cart
driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
# Open the cart page
driver.find_element("class name", "shopping_cart_link").click()
time.sleep(2)

# Take new screenshot
screenshot_path = r"C:\Users\SHRTOMAR\OneDrive - Capgemini\Desktop\Python\AI_UI_Validator\saucedemo_changed.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved: {screenshot_path}")
driver.quit()