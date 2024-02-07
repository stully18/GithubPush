from instapy import InstaPy

# Initialize InstaPy session
session = InstaPy(username="mofot70899@namewok.com", password="easypie1234",want_check_browser=False,headless_browser=False)

# Login to Instagram
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
