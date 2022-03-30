#!/usr/bin/python3

import requests
import sys

r = requests.get("http://127.0.0.1:8080/"+sys.argv[1])
print("status code : "+ str(r.status_code))
if r.status_code == 200 :
	print("Json : ")
	print(r.json)
	print("Content : ")
	print(r.text)
elif r.status_code != 200:
	print("Something went wrong")
	print(r.headers["www-authenticate"])
	print("response: ",str(r.text))
