from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

email_data = pd.read_excel("email_data.xlsx")

# Replace with gmail credentials
email_id = list(email_data["sender_email"])
password = list(email_data["password"])

# Replace with email recipients
to_email = list(email_data["recipient_email"])

# Count of sent email
sent_email = []
sent_email_records = []

# Launch chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Loop through each gmail account
for x in range(len(email_id)):
    email_ids = email_id[x]
    passwords = password[x]

    sent_email_records.extend(sent_email)
    sent_email.clear()

    # Navigate to Gmail website
    driver.get('https://www.gmail.com')
    time.sleep(10)

    # Delete all cookies
    driver.delete_all_cookies

    # Refresh webpage to clear any cached data
    driver.refresh()
    time.sleep(10)
    
    # Enter email id and click next
    driver.find_element(By.XPATH, '//input[@id="identifierId"]').send_keys(email_ids)
    driver.find_element(By.XPATH, '//span[contains(text(), "Next")]').click()
    time.sleep(10)

    # Enter password and click next
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(passwords)
    driver.find_element(By.XPATH, '//span[contains(text(), "Next")]').click()
    time.sleep(10)

    # Loop through recipient email_id
    for i in range(len(to_email)):
        # Get the current chunk of 5 elements
        to = to_email[i]
        if to not in sent_email_records:
            # Compose email
            driver.find_element(By.XPATH, '//div[@class="T-I T-I L3"]').click()
            time.sleep(10)

            # Enter recipients, subject, and body of email
            driver.find_element(By.XPATH, '//input[@class="agP aFw"]').send_keys(to)
            time.sleep(10)
            driver.find_element(By.XPATH, '//input[@name="subjectbox"]').send_keys("Subject of the email")
            time.sleep(10)
            driver.find_element(By.XPATH, '//div[@aria-label="Message Body"]').send_keys("Body of the email")

            # Send the email
            driver.find_element(By.XPATH, '//div[@class="T-I J-35-Ji aoO v7 T-I-atl L3"]').click()
            time.sleep(10)

            print("Email sent to : ", to)
            sent_email.append(to)

            if len(sent_email) >= 2:
                print("Logging of Current Email")
                break
            else:
                continue

    # Logging out of Gmail
    driver.get("https://accounts.google.com/Logout?hl=en")
    time.sleep(10)