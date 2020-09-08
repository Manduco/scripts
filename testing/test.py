import json

config = require('vars.json')



with open('var.json') as f:
  data = json.load(f)

hostname = input("enter host name :")

if( hostname == 'cisco28'):
    print(data["vpnSubnet"]["cisco28"])
else:
    print("this host name does not exist would like to create one?")
