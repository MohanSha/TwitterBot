from twitpy import TwitPy

TwitPy(username="smohansha", password="****") \
  .login() \
  .follow_from_recom(amount=250) \
  .unfollow_users(amount=100) \
  .end()