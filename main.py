from instagrapi import Client
from html2image import Html2Image
from bs4 import BeautifulSoup
import requests
import schedule
import time

# تنظیمات اینستاگرام
USERNAME = "takhminzan"
PASSWORD = "32&w!6E%)2UPP3="
IMAGE_PATH = "prices-post.jpg"
CAPTION = "قیمت امروز طلا: \n طلای ۱۸ عیار \n انس طلای جهانی \n سکه امامی \n سکه بهار آزادی \n نیم سکه \n ربع سکه \n سکه گرمی \n . \n . \n #طلا #قیمتطلا #قیمتـطلا #طلایـ۱۸ـعیار #سکه #قیمتـسکه #انسـطلا #انس"

def take_screenshot():
    # درخواست برای دریافت محتوای صفحه وب
    url = "https://app.takhminzan.com/socials"
    response = requests.get(url)

    # تاخیر برای اطمینان از لود کامل صفحه
    time.sleep(20)

    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)

    # یافتن المنت با id=root و دریافت محتوای HTML آن
    root_element = soup.find(id="root")

    print(root_element)

    if root_element:
        html_content = str(root_element)

        # گرفتن اسکرین شات از محتوای HTML
        hti = Html2Image()
        hti.screenshot(html_str=html_content, save_as=IMAGE_PATH)

        print(f"Screenshot saved as {IMAGE_PATH}")
    else:
        print("Element with id='root' not found!")

def upload_to_instagram():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    cl.photo_upload(IMAGE_PATH, CAPTION)
    print("Photo uploaded to Instagram.")

def job():
    take_screenshot()
    upload_to_instagram()

# برنامه‌ریزی اجرای کد هر روز ساعت ۸ و نیم شب
schedule.every().day.at("02:48").do(job)

print("Scheduled job started. Waiting for the next scheduled time...")

# اجرای مداوم برنامه برای چک کردن زمان‌های برنامه‌ریزی شده
while True:
    schedule.run_pending()
    time.sleep(1)
