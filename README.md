# TwitPy
<img src="http://theinspirationroom.com/daily/design/2012/6/new_twitter_logo.jpg" align="right" width=100>

### Quick and dirty follow/unfollow automation for Twitter.

[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/MohanSha/TwitterBot/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-red.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-green.svg)](https://www.python.org/)

#### Getting started
```bash
git clone https://github.com/MohanSha/TwitterBot.git
cd TwitPy
pip install .
# or depending on your system
python setup.py install
```

Make sure to get the right `chromedrive` for your system [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Just put it in /assets.

Now edit the `quickstart.py` file to your needs.

#### API
```python
from twitpy import TwitPy

# if you want to run it on a server simply set nogui=True

TwitPy(username="****", password="****",nogui=False) \
  .login() \
  # follows up to 250 accounts from your recommendations
  .follow_from_recom(amount=250) \ 
  # unfollows 100 accounts from your following list
  .unfollow_users(amount=100) \ 
  .end()
```
