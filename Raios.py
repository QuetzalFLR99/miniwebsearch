import requests

r = requests.get("https://www.recursospython.com/2")

print(r.reason)

x = str(r.reason)


print(x)

print(type(x))
