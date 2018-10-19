#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:20:06 2018

@author: susanachicano
"""

def all_postcode(osmfile):
    osm_file = open(osmfile, "r")
    valid = []
    invalid = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == 'node':
            for tag in elem.iter('tag'):
                k = tag.get('k')
                if k == "addr:postcode":
                    v = tag.get('v')
                    if (VALID_CODE.match(v) and v[0:2] == "94"):
                        if v not in valid:
                            valid.append(v)
                    else:
                        if v not in invalid:
                            invalid.append(v)                    
               
    return valid, invalid

# Now we print valid and invalid postcodes, and the total number for each

def test():
    valid, invalid = all_postcode(SAMPLE_FILE)
    print ("valid postcodes:")
    pprint.pprint(valid)
    print ("Number of valid postcodes:", len(valid))
    print ("invalid postcodes:")
    pprint.pprint(invalid)
    print ("Number of invalid postcodes:", len(invalid))