from instagrapi import Client

cl = Client()
cl.login("takhminzan", "32&w!6E%)2UPP3=")

media = cl.photo_upload(path="image.png", caption="test")