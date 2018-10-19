#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:02:39 2018

@author: susanachicano
"""

def count_tags_by_type(filename, limit=-1):

    # We create dict objects and sums
    sf_tag_count = {}
    sf_tag_keys = {}
    sums = 0

    # We now parse through the elements
    for _, element in ET.iterparse(filename, events=("start",)):
       
        # We add the tag key to sf_tag_keys dict for each tag with the k attribute 
        if element.tag == 'tag' and 'k' in element.attrib:
            add_tag(element.get('k'), sf_tag_keys)


        # It stops if the limit is exceded
        if limit > 0 and sums >= limit:
            break
        sums += 1
    
    sf_tag_keys = sorted(sf_tag_keys.items(), key=operator.itemgetter(1))[::-1]

    # Return the values
    return sf_tag_count, sf_tag_keys

# It adds a tag to sf_tag_count or starts at 0 if does not exist
def add_tag(tag, tag_count):   
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1

# This function prints and store all the tag element with a k attribute in the -tag-keys.json file
def main(limit=-1):
    tags, sf_tag_keys = count_tags_by_type(SAMPLE_FILE, limit)
    json.dump(sf_tag_keys, open(SAMPLE_FILE + '-tag-keys.json', 'w'))
    pprint.pprint(sf_tag_keys)
    return tags, sf_tag_keys
