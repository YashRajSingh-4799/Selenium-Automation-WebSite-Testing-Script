import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Set up Selenium WebDriver (assuming you have installed the necessary drivers)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

# Define the available fields to test
fields = [
    {"selector": "input#fname", "name": "Yash Raj"},
    {"selector": "input#lname", "name": "Singh"},
    {"selector": "input#email", "name": "abc@gmail.com"},
    # {"selector": "select#experience", "name": "Experience"},
    {"selector": "input#dob", "name": "1990-01-01"},
    {"selector": "input.btn.btn-default", "name": "File"},
    {"selector": "input#mobile", "name": "8081767472"},
    # {"selector": "textarea#address", "name": "Address"},
]

# Randomly select three fields to test
# fields_to_test = random.sample(fields, 3)
fields_to_test = fields
# Test each field
for field in fields_to_test:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, field["selector"])))
    # Perform action on the field
    if field["name"] == "File":
        # For file input field, upload a sample file (change the file path accordingly)
        element.send_keys("D:/Internship Assign/Selenium/New folder/file.txt")
    else:
        # For other fields, enter random text
        input_text =field["name"]
        element.send_keys(input_text)

try:
    # Wait for the checkbox to be present
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Agree")))

    # Tick mark the checkbox
    checkbox.click()

except TimeoutException:
    print("Checkbox not found within the specified timeout.")

# Click on the submit button
# submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#submit")))
# submit_button = driver.find_element_by_xpath("//button[contains(text(), 'Submit')]")
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()


# Wait for the output message
output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))

output_text = output_element.text

# Print the output message
print("Output Message:", output_text)


# driver.quit()