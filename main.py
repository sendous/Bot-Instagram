from instagrapi import Client
from html2image import Html2Image
import schedule
import time

# تنظیمات حساب کاربری اینستاگرام
USERNAME = "takhminzan"
PASSWORD = "32&w!6E%)2UPP3="

# آدرس صفحه وب
URL = "https://app.takhminzan.com/socials"
IMAGE_PATH = "prices-post.png"
CAPTION = "قیمت امروز طلا: \n طلای ۱۸ عیار \n انس طلای جهانی \n سکه امامی \n سکه بهار آزادی \n نیم سکه \n ربع سکه \n سکه گرمی \n . \n . \n #طلا #قیمتطلا #قیمتـطلا #طلایـ۱۸ـعیار #سکه #قیمتـسکه #انسـطلا #انس"

CHROME_PATH = "chrome.msi"

def take_screenshot():
    hti = Html2Image(size=(430, 513), browser_executable=CHROME_PATH)
    time.sleep(10)
    hti.screenshot(url=URL, save_as=IMAGE_PATH)

def upload_to_instagram():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    cl.photo_upload(IMAGE_PATH, CAPTION)

def job():
    take_screenshot()
    upload_to_instagram()

# زمان‌بندی برای اجرا در هر روز ساعت ۸:۳۰ شب
schedule.every().day.at("20:59").do(job)
# job()

while True:
    schedule.run_pending()
    time.sleep(1)
