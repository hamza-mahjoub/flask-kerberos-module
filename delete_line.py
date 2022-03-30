#!/usr/bin/python3

import requests
import kerberos
import sys

try:
	_, krb_context = kerberos.authGSSClientInit("host@server.example.tn")
	print("step : "+str(kerberos.authGSSClientStep(krb_context, "")))

	print("Creating auth header......")
	negotiate_details = kerberos.authGSSClientResponse(krb_context)
	headers = {"Authorization": "Negotiate "+ negotiate_details, 'Content-Type':'application/json'}

	data = {'line':int(sys.argv[2]) }
	print(data)

	r = requests.post("http://127.0.0.1:8080/deleteline/"+sys.argv[1],json = data, headers=headers)

	print("Status : "+str(r.status_code))
	print("Json : ")
	print(r.json)
	print("Content : ")
	print(r.text)
except Exception as err:
	print(type(err))
	print(err)
	print('Something went wrong, check your ticket....')
