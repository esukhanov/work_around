import requests

data='text=%D1%84%D0%B0%D0%B1%D0%B5%D1%80%D0%BB%D0%B8%D0%BA&lr=213'
req=requests.get('https://yandex.ru/search/?text=%D1%84%D0%B0%D0%B1%D0%B5%D1%80%D0%BB%D0%B8%D0%BA&lr=213')
print (req)
print (req.headers)
#print (req.history)
for i in req.text.split(' '):
    print (i)