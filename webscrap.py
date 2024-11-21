#import package
import requests

#url
url = 'http://www.datacamp.com/teach/documentation'

#package the request, send the request and catch the response
r = requests.get(url)

#extract the response: text
text = r.text

# Print the html
print(text)