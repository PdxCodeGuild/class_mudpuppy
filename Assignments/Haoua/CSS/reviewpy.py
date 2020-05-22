import django
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")
print(django.get_version())

results= requests.get("https://www.google.com/")
# results= requests.get()"https://www.google.com/")
print(results)