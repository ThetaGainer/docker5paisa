#!/usr/bin/python

from py5paisa import FivePaisaClient

lcred={
    "APP_NAME":"",
    "APP_SOURCE":"",
    "USER_ID":"",
    "PASSWORD":"",
    "USER_KEY":"",
    "ENCRYPTION_KEY":""
    }

cemail=""
cpasswd=""
cdob=""

client = FivePaisaClient(email=cemail, passwd=cpasswd, dob=cdob, cred=lcred)
