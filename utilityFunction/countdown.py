from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.timeanddate.com/countdown/create")
# https://www.timeanddate.com/countdown/generic?iso=20200302T00&p0=1440&msg=Test+Event&font=cursive&csz=1 << stop at zero
# https://www.timeanddate.com/countdown/generic?iso=20200302T00&p0=1440&msg=Test+Event&font=cursive

data = r.text

soup = BeautifulSoup(data, 'html.parser')

# Get the list of all available themes
type_objs = soup.find(id="cd-templates")
theme_list = [];
for link in soup.find_all('article'):
    theme_list.append(link.get('data-theme'))

print("\n***THEMES***")
for theme in theme_list:
    if not theme == None:
        print(theme)

font_list = [];
font_objs = soup.find(id="font")
for fntlink in soup.find_all('option'):
    font_list.append(fntlink.get('value'))

print("\n***FONTS***")
for font in font_list:
    if not font == None:
        print(font)

event_name_input = input("Enter an Event Name...")
date_input = input("Enter Event Date...")

# Display theme options

# Display font options

print("\n" + event_name_input + " will occur on " + date_input)
