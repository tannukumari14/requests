# import requests
# cookies=dict(key1="value1")
# res=requests.post("https://httpbin.org/cookies",cookies=cookies)
# print(res.text)

import requests
res=requests.get("https://httpbin.org/headers")
print(res.headers)

# "whois wh word"
# "a question in english introduce by "wh" word that requried information in answer rather than yes or no"