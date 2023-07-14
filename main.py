
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

# Define the available fields to test
fields_to_test = [
    {"selector": "input#fname", "name": "Yash Raj"},
    {"selector": "input#lname", "name": "Singh"},
    {"selector": "input#email", "name": "abc@gmail.com"},
    {"selector": "input#dob", "name": "1990-01-01"},
    {"selector": "input.btn.btn-default", "name": "File"},
    {"selector": "input#mobile", "name": "8081767472"},
]


# -------------------------FORM---------------------------------
for field in fields_to_test:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, field["selector"])))
    if field["name"] == "File":
        element.send_keys("D:/Internship Assign/Selenium/New folder/file.txt")
    else:
        input_text =field["name"]
        element.send_keys(input_text)

try:
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Agree")))
    checkbox.click()

except TimeoutException:
    print("Checkbox not found within the specified timeout.")

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()

output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
output_text = output_element.text

# Print 
print("Output Message:", output_text)




# -------------------------IFrame without ID---------------------------------
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src='/Home/IFrame']")))
driver.switch_to.frame(iframe)


for field in fields_to_test:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, field["selector"])))
    
    if field["name"] == "File":
        element.send_keys("D:/Internship Assign/Selenium/New folder/file.txt")
    else:
        input_text =field["name"]
        element.send_keys(input_text)

try:
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Agree")))
    checkbox.click()

except TimeoutException:
    print("Checkbox not found within the specified timeout.")

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()

output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
output_text = output_element.text

# Print the output message 
print("Output Message:", output_text)

# -------------------------IFrame with ID---------------------------------

driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

iframe_id = "iframeId"
iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, iframe_id)))
driver.switch_to.frame(iframe)

for field in fields_to_test:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, field["selector"])))
    if field["name"] == "File":
        element.send_keys("D:/Internship Assign/Selenium/New folder/file.txt")
    else:
        input_text =field["name"]
        element.send_keys(input_text)

try:
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Agree")))
    checkbox.click()

except TimeoutException:
    print("Checkbox not found within the specified timeout.")

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()

output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
output_text = output_element.text

# Print the output message 
print("Output Message:", output_text)




# --------------------Shadow DOM--------------------


driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")


for field in fields_to_test:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form#shadowdomautomationtestform" + field["selector"])))

    if field["name"] == "File":
        element.send_keys("D:/Internship Assign/Selenium/New folder/file.txt")
    else:
        input_text =field["name"]
        element.send_keys(input_text)

try:
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Agree")))
    checkbox.click()

except TimeoutException:
    print("Checkbox not found within the specified timeout.")

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()

output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
output_text = output_element.text

# Print the output message
print("Output Message:", output_text)


driver.quit()