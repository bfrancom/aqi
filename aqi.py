#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import xmltodict
import pprint


r = requests.get("https://air.utah.gov/xmlFeed.php?id=slc")

slc_content = xmltodict.parse(r.content)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(slc_content)
pp.pprint(slc_content.keys())

#for field in top_level_dict["fields"]:
#    if field["name"] = "col_1":
#            print(field["amount"])
#                    break
#print (slc_content)

