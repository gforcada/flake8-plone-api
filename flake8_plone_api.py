# -*- coding: utf-8 -*-
from collections import defaultdict

import json


class PloneAPIChecker(object):
    name = 'flake8_plone_api'
    version = '0.1'
    message = 'P001 found "{0}" consider replacing it with: {1}'

    def __init__(self, tree, filename):
        self.filename = filename
        self.mapping = PloneAPIChecker._get_mapping()

    def run(self):
        with open(self.filename) as f:
            lines = f.readlines()

            for lineno, line in enumerate(lines, start=1):
                for old_approach in self.mapping:
                    found = line.find(old_approach)
                    if found != -1:
                        msg = self.message.format(
                            old_approach,
                            ' or '.join(self.mapping[old_approach])
                        )
                        yield lineno, found, msg, type(self)


    @staticmethod
    def _get_mapping():
        """Create a mapping between old usages that can be replaced by plone.api

        It basically reverses DATA (see below) so that each old approach will
        be a key in the resulting dictionary and all plone.api method calls
        that can be a potential replacement are listed as its value. i.e.

            {'getToolByName': ['plone.api.portal.get_tool']

        DATA variable is meant to be an easy way to add replacements.
        The output of this function is meant to be an easy way to find those
        replacements.
        """
        mapping = defaultdict(list)
        json_data = json.loads(DATA)

        for module in json_data:
            for api_method in json_data[module]:
                method_call = '{0}.{1}'.format(module, api_method)
                for old_approach in json_data[module][api_method]:
                    # do not add the XXX entries
                    if old_approach == 'XXX':
                        continue
                    mapping[old_approach].append(method_call)

        return mapping


# note: XXX entries are mostly so that all Plone API methods could be listed,
# or to note that there has to be more old usages, suggestions welcome.
DATA = """
{
  "plone.api.content": {
    "create": ["invokeFactory", "createObject", "createContentInContainer"],
    "get": ["restrictedTraverse"],
    "move": ["manage_cutObjects", "manage_pasteObjects"],
    "rename": ["manage_renameObject"],
    "copy": ["manage_copyObjects"],
    "delete": ["manage_delObjects"],
    "get_state": ["getInfoFor"],
    "transition": ["doActionFor"],
    "get_view": ["XXX"],
    "get_uuid": ["IUUID"],
    "find": ["catalog", "searchResults" ]
  },
  "plone.api.user": {
    "create": ["addMember"],
    "get": ["getMemberById", "get_member_by_login_name"],
    "get_current": ["getAuthenticatedMember"],
    "get_users": ["listMembers", "getGroupMembers"],
    "delete": ["deleteMembers"],
    "is_anonymous": ["isAnonymousUser"],
    "get_roles": ["getRolesInContext", "getRoles", "get_local_roles_for_userid" ],
    "get_permissions": ["checkPermission"],
    "has_permission": ["checkPermission"],
    "grant_roles": ["setSecurityProfile", "manage_setLocalRoles"],
    "revoke_roles": ["setSecurityProfile", "manage_setLocalRoles", "manage_delLocalRoles"]
  },
  "plone.api.group": {
    "create": ["addGroup"],
    "get": ["getGroupById"],
    "get_groups": ["getGroupsForPrincipal", "listGroups"],
    "delete": ["removeGroup"],
    "add_user": ["addPrincipalToGroup"],
    "remove_user": ["removePrincipalFromGroup"],
    "get_roles": ["getRoles", "getRolesInContext"],
    "grant_roles": ["setRolesForGroup", "manage_setLocalRoles" ],
    "revoke_roles": ["setRolesForGroup", "manage_setLocalRoles", "manage_delLocalRoles"]
  },
  "plone.api.portal": {
    "get": ["getSite"],
    "get_navigation_root": ["getNavigationRootObject"],
    "get_tool": ["getToolByName"],
    "send_email": ["XXX"],
    "get_localized_time": ["ulocalized_time"],
    "show_message": ["IStatusMessage"],
    "get_registry_record": ["IRegistry"],
    "set_registry_record": ["IRegistry"]
  },
  "plone.api.env": {
    "adopt_user": ["setSecurityManager", "getSecurityManager","newSecurityManager"],
    "adopt_roles": ["getSecurityManager"],
    "debug_mode": ["DevelopmentMode"],
    "test_mode": ["XXX"],
    "plone_version": ["XXX"],
    "zope_version": ["XXX"]
  }
}
"""
