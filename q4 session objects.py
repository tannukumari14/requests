import requests
s=requests.session()
s.get("https://httpbin.org/cookies/set/sessioncookies/123456789")
r=s.get("https://httpbin.org/cookies")
print(r.text)

