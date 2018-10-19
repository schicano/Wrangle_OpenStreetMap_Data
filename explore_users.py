#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:11:59 2018

@author: susanachicano
"""

def get_user(element):
    if 'uid' in element.attrib:
        return element.attrib['uid']

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        uid = get_user(element)
        if uid != None:
            users.add(uid)
    return users

users = process_map(SAMPLE_FILE)