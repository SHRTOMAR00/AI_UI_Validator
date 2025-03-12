import time
from selenium import webdriver
# Initialize WebDriver
driver = webdriver.Chrome()
# Open the SauceDemo website
driver.get("https://www.saucedemo.com/")
time.sleep(2)  # Wait for the page to load
# Take a baseline screenshot
screenshot_path = r"C:\Users\SHRTOMAR\OneDrive - Capgemini\Desktop\Python\AI_UI_Validator\saucedemo_baseline.png"
driver.save_screenshot(screenshot_path)
print(f"Baseline screenshot saved: {screenshot_path}")
# Close the browser
driver.quit()