#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    content = json.load(file)
    interfaces = (content['ietf-interfaces:interfaces']['interface'])

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
for i in interfaces:
    #print(i)
    print('Interface: ' + i['name'] + '\t IP: ' + i['ietf-ip:ipv4']['address'][0]['ip'] + '\t Netmask: ' + i['ietf-ip:ipv4']['address'][0]['netmask'] + '\n')