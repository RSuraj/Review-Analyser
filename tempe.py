from urllib.parse import urlencode 
from urllib.request import Request, urlopen 
import pprint
url = 'http://sentiment.vivekn.com/api/text/'  
post_fields = {'txt': "good"} 
request = Request(url, urlencode(post_fields).encode()) 
#print(urlopen(request).read())
json = urlopen(request).read().decode() 
i=50


 
r=json[66]
#.replace('\n','')
if(r=="u"):
 print("hai")
print(r)
print("rdtr")
print(r)

#pp=pprint.PrettyPrinter(indent=4)
#pp.pprint(stuff['result']['sentiment'])

