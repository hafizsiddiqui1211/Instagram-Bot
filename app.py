import instaloader
insta = instaloader.Instaloader()
acc = "username"  # replace "username" with real username.

insta.download_profile(acc, profile_pic_only=False)
