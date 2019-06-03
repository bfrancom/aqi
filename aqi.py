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
###for child in root[1][2]:
#    print (child.tag, child.attrib)
#print (root[1][2][7]).attrib
for data in root.findall('./site/data'):
    for child in data:
        tag = child.tag
        value = child.text
        #this will print out all the tags and their value
        #print (tag, value)
        if tag == "ozone" or tag == "temperature":
            print (tag, value)


pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(slc_content)
#pp.pprint(slc_content.keys())

#for field in top_level_dict["fields"]:
#    if field["name"] = "col_1":
#            print(field["amount"])
#                    break
#print (slc_content)

