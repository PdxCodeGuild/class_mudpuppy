import requests
import json

url = 'http://www.worldofballpythons.com/morphs?filter=1'

data = requests.get('http://www.worldofballpythons.com/ajax-files/search.php', params={'q': '', 'p': 130}).content

print(data)



