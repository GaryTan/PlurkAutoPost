# -*- coding: utf-8 -*-

import requests
import re

# user imformation
user = "myaccount"
passwd = "mypassword"
post = "messages"

# get user id
result = requests.get("http://www.plurk.com/{0}".format(user)).text
userID = re.findall('"user_id": (\w+)', result)[0]

# login
data = {"nick_name": user, "password": passwd, "login-token": "b301c75c5261f80d2d5021a05259a4bd@nommw8", "logintoken": 1}
r = requests.post("https://www.plurk.com/Users/login", data=data)
p_cookie = r.request.headers["Cookie"]
header = {"cookie": p_cookie}

# post
data = {"qualifier": "says", "content": post, "lang" : "tr_ch", "no_comments" : "0", "uid" : userID}
r = requests.post("https://www.plurk.com/TimeLine/addPlurk", data=data, headers=header)
