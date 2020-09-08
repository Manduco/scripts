import json

with open('var.json') as f:
  data = json.load(f)

print("---creating cisco config file---")
print("Version: "+ str(data["code"]["version"]))

hostname = input("enter host name :")

# if( hostname == 'cisco28'):
#     print(data["vpnSubnet"]["cisco28"])
# else:
#     print("this host name does not exist would like to create one?")

if hostname in data["host"]:
    print("hostname found")
    print("Would like to create script with current settings?")
else:
    print("hostname was not found")
