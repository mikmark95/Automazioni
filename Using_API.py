import requests

apiKey='c6af87825ab24dcdb913f52fc291c06d'

r= requests.get(f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-06-11&to=2023-06-03&sortBy=popularity&language=en&apiKey={apiKey}")
content = r.json()

print(content['articles'][0]['title'])