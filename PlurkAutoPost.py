#encoding: utf-8

import urllib2, urllib
import time
import getpass
import re
from datetime import datetime

print "Karma up up up !"
print "\r"
user = raw_input("userid: ")
passwd = getpass.getpass()
print "\r"

post = raw_input("post message: ")
print "\r"

print "Time set "
print "(format: HH:MM:SS)"
time = raw_input("Time: ")
print "\r"

res = urllib2.urlopen('http://www.plurk.com/'+user).read()
re = re.findall('"user_id": (\w+)', res)

while 1:
	timenow = str(datetime.now())[11:19]
	if time == timenow:
		cookies = urllib2.HTTPCookieProcessor()
		opener = urllib2.build_opener(cookies)

		data = {  "nick_name": user, "password": passwd, "login_token" : "3b1e3413a45932936432354ab3c062f8@n6t3bj", "logintoken" : "1"}
		request = urllib2.Request(
			url     = 'http://www.plurk.com/Users/login',
			data    = urllib.urlencode(data))
		f = opener.open(request)

		data = {  "qualifier": "says", "content": post, "lang" : "tr_ch", "no_comments" : "0", "uid" : re[0]}
		request = urllib2.Request(
		        url     = 'http://www.plurk.com/TimeLine/addPlurk',
		        data    = urllib.urlencode(data))
		opener.open(request)
		print "Banana Dancing!!"
