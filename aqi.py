#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import xmltodict
import pprint
from xml.etree import ElementTree as ET


r = requests.get("https://air.utah.gov/xmlFeed.php?id=slc")

#slc_content = xmltodict.parse(r.content)
#print(slc_content)

root = ET.fromstring(r.content)
#print (root.tag)
#    print (child.tag, child.attrib)
#only get 1st element returned. For most recent data from URL
for data in root.findall('./site/data[1]'):
    for child in data:
        tag = child.tag
        value = child.text
        #this will print out all the tags and their value
#        print (tag, value)
        if tag == "temperature":
            print (value,"F°")
        #if tag == "ozone":
        #    print (tag, value)
