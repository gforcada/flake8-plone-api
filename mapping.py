# -*- coding: utf-8 -*-
from collections import defaultdict

import json


def get_mapping():
    """Create a mapping between old usages that can be replaced by plone.api

    It basically reverses mapping.json so that each old approach will be a
    key in the resulting dictionary and all plone.api method calls that can
    be a potential replacement are listed as its value.
    i.e.

        {'getToolByName': ['plone.api.portal.get_tool']

    The JSON file is meant to be an easy way to add replacements.
    The output of this function is meant to be an easy way to find those
    replacements.
    """
    mapping = defaultdict(list)
    json_data = json.load(open('mapping.json'))

    for module in json_data:
        for api_method in json_data[module]:
            method_call = '{0}.{1}'.format(module, api_method)
            for old_approach in json_data[module][api_method]:
                mapping[old_approach].append(method_call)

    return mapping
