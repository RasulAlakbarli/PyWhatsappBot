from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

def WhatsapBot(contacts_file, message, image_text):
    driver = webdriver.Chrome()
    baseurl = "https://web.whatsapp.com/"
    driver.get(baseurl)
    time.sleep(10)

    with open(contacts_file) as f:
        contacts = f.read().splitlines()

    for contact in contacts:
        sameTab = (baseurl + "send?phone=" + str(contact))
        driver.get(sameTab)
        time.sleep(4)

        content = driver.switch_to.active_element

        if message:
            content.send_keys(message)
            content.send_keys(Keys.RETURN)
            time.sleep(1)

        # Send this image
        content.send_keys(Keys.COMMAND + "v")
        time.sleep(1)
        image_window = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        image_window.send_keys(image_text)
        image_window.send_keys(Keys.RETURN)
        time.sleep(1)



if __name__ == "__main__":
    contacts_file = "contacts.txt"
    message = "Hello, this is the final test message"
    # copy image to clipboard and run the script
    image_text = "Iphone 15 green only 1400 manat!"

    WhatsapBot(contacts_file, message, image_text)