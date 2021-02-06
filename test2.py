#!/usr/bin/env python3

# This is a script to output a clean list of Craigslist building materials for sale
# in Abilene

from lxml import html
import requests



# Request the page from Craigslist
page = requests.get('https://abilene.craigslist.org/d/materials/search/maa')
tree = html.fromstring(page.content)

# XPaths
url = tree.xpath('//p[@class="result-info"]/a/@href') #URLs
dtime = tree.xpath('//p[@class="result-info"]/time/@datetime') #Timestamps
title = tree.xpath('//p[@class="result-info"]/a/text()') #List Titles

# Trying to iterate for each item in the list
for i, (xtitle, xurl, xdtime) in enumerate(zip(title, url, dtime)):
    print(i, xtitle, "\n\t", xurl, xdtime, "\n\t")

