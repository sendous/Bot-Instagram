from selenium import webdriver
from selenium.webdriver.common.by import By
from instagrapi import Client
import os
from dotenv import load_dotenv
import schedule
import time

# Load environment variables
load_dotenv()
command_executor = os.getenv("COMMAND_EXECUTOR") + "/webdriver"
browserless_token = os.getenv("BBROWSERLESS_TOKEN")
instagram_username = os.getenv("INSTAGRAM_USERNAME")
instagram_password = os.getenv("INSTAGRAM_PASSWORD")

# Selenium setup
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', browserless_token)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=500,1080")  # Set window size to 1920x1080
chrome_options.add_argument("--force-device-scale-factor=2")  # Scale factor for higher DPI

# Check if logged in to Instagram
def is_logged_in(client):
    try:
        client.account_info()
        return True
    except Exception:
        return False

def take_screenshot_and_post():
    # Create a new WebDriver instance
    driver = webdriver.Remote(
        command_executor=command_executor,
        options=chrome_options
    )

    try:
        # Navigate to the page
        driver.get("https://app.takhminzan.com/socials")

        # Wait for the element to load and take a screenshot
        driver.implicitly_wait(30)
        element = driver.find_element(By.ID, "root")
        element.screenshot("prices-post.png")
    finally:
        # Quit the WebDriver instance
        driver.quit()

    # Instagram setup
    cl = Client()
    if not is_logged_in(cl):
        cl.login(instagram_username, instagram_password)

    # Upload the screenshot to Instagram
    title = os.getenv("TITLE")
    caption = os.getenv("CAPTION")
    hashtags = os.getenv("HASHTAG")
    post_text = f"{title}\n{caption}\n{hashtags}"
    
    cl.photo_upload("prices-post.png", post_text)

# Schedule the task
# schedule.every().day.at("20:30").do(take_screenshot_and_post)
take_screenshot_and_post()

while True:
    schedule.run_pending()
    time.sleep(1)
