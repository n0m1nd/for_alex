#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:14:15 2020

@author: nomind
"""

# Libraries import
import requests
from bs4 import BeautifulSoup

# Setting the URL
url = 'https://www.newsnow.co.uk/h/'

# Connect to the URL and get response
response = requests.get(url)

# If server response is 200 then proceed
if response.status_code == requests.codes.ok:
    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    # Get a list of titles and write to file
    # Open file for writing
    with open('titles_list.txt', 'w', encoding='utf-8') as titles_list:   
        # Get elements with 'a class="hll"' where titles are
        for element in soup.find_all('a', class_='hll'):
            # Write every title to file
            titles_list.write(element.text + '\n') 
    # Close file        
    titles_list.close()
# If server response is not OK - contact script developer
else:
    print ("Server response is not 200. Please contact John Smith for script fix")
