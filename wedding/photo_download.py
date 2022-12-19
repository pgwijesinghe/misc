from PIL import Image
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver = webdriver.Edge()
photo_id = 'HEWA7842'
url= f"https://www.dropbox.com/sh/agqgnnprdk6qz8v/AAAF8jO0xuN8kyYZgoi_mnIva/1?dl=0&preview={photo_id}.jpg&subfolder_nav_tracking=1"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
element = soup.findAll("img",{"class":"_smallImg_1anuf_15"})
image_url = element[0]['src']

img = Image.open(requests.get(image_url, stream = True).raw)
img.save(f'./wedding/image_{photo_id}.jpg')

driver.quit()

"""
This program failed because it took a long time to load the actual image having loaded the page (due to dropbox refreshing the page continously).
Moving on to a different program where I can load the image with the url realtime.
Update: Infact doing this locally would be better.
Check image_viewer.py
"""