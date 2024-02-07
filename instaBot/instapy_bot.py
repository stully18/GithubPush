from instapy import InstaPy
import importlib

# Initialize InstaPy session
session = InstaPy(username="mofot70899@namewok.com", password="easypie1234",want_check_browser=False,headless_browser=False)

# Login to Instagram
session.login()

