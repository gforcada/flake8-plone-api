# -*- coding: utf-8 -*-
from collections import defaultdict

import re


class PloneAPIChecker(object):
    name = 'flake8_plone_api'
    version = '0.1'
    message = 'P001 found "{0}" consider replacing it with: {1}'

    character = re.compile(r'\w')

    def __init__(self, tree, filename):
        self.filename = filename
        self.mapping = PloneAPIChecker._get_mapping()

    def run(self):
        with open(self.filename) as f:
            lines = f.readlines()

            for lineno, line in enumerate(lines, start=1):
                for old_approach in self.mapping:
                    found = self.check_line(line, old_approach)
                    if found != -1:
                        msg = self.message.format(
                            old_approach,
                            ' or '.join(self.mapping[old_approach])
                        )
                        yield lineno, found, msg, type(self)

    def check_line(self, line, old_approach):
        found = line.find(old_approach)
        if found == -1:
            return found

        # Check if our found term is already at the end of the line.
        # Then further checks are not necessary
        next_character_position = found + len(old_approach) + 1
        if next_character_position >= len(line):
            return found

        # check that the method is not a substring of another
        # method, i.e getSite and getSiteManager
        next_character = line[next_character_position]
        if self.character.search(next_character) is not None:
            return -1

        return found

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

        for api_method in DATA:
            method_call = 'plone.api.{0}'.format(api_method)
            for old_approach in DATA[api_method]:
                # do not add the empty entries
                if old_approach is None:
                    continue
                mapping[old_approach].append(method_call)

        return mapping


DATA = {
    'content.create': [
        'invokeFactory',
        'createObject',
        'createContentInContainer',
    ],
    'content.get': [
        'restrictedTraverse',
    ],
    'content.move': [
        'manage_cutObjects',
        'manage_pasteObjects',
    ],
    'content.rename': [
        'manage_renameObject',
    ],
    'content.copy': [
        'manage_copyObjects',
    ],
    'content.delete': [
        'manage_delObjects',
    ],
    'content.get_state': [
        'getInfoFor',
    ],
    'content.transition': [
        'doActionFor',
    ],
    'content.get_view': [
        None,
    ],
    'content.get_uuid': [
        'IUUID',
    ],
    'content.find': [
        '.catalog',
        'searchResults',
        None,
    ],
    'user.create': [
        'addMember',
    ],
    'user.get': [
        'getMemberById',
        'get_member_by_login_name',
    ],
    'user.get_current': [
        'getAuthenticatedMember',
    ],
    'user.get_users': [
        'listMembers',
        'getGroupMembers',
    ],
    'user.delete': [
        'deleteMembers',
    ],
    'user.is_anonymous': [
        'isAnonymousUser',
    ],
    'user.get_roles': [
        'getRolesInContext',
        'getRoles',
        'get_local_roles_for_userid',
    ],
    'user.get_permissions': [
        'checkPermission',
    ],
    'user.has_permission': [
        'checkPermission',
    ],
    'user.grant_roles': [
        'setSecurityProfile',
        'manage_setLocalRoles',
    ],
    'user.revoke_roles': [
        'setSecurityProfile',
        'manage_setLocalRoles',
        'manage_delLocalRoles',
    ],
    'group.create': [
        'addGroup',
    ],
    'group.get': [
        'getGroupById',
    ],
    'group.get_groups': [
        'getGroupsForPrincipal',
        'listGroups',
    ],
    'group.delete': [
        'removeGroup',
    ],
    'group.add_user': [
        'addPrincipalToGroup',
    ],
    'group.remove_user': [
        'removePrincipalFromGroup',
    ],
    'group.get_roles': [
        'getRoles',
        'getRolesInContext',
    ],
    'group.grant_roles': [
        'setRolesForGroup',
        'manage_setLocalRoles',
    ],
    'group.revoke_roles': [
        'setRolesForGroup',
        'manage_setLocalRoles',
        'manage_delLocalRoles',
    ],
    'portal.get': [
        'getSite',
    ],
    'portal.get_navigation_root': [
        'getNavigationRootObject',
    ],
    'portal.get_tool': [
        'getToolByName',
    ],
    'portal.send_email': [
        None,
    ],
    'portal.get_localized_time': [
        'ulocalized_time',
    ],
    'portal.show_message': [
        'IStatusMessage',
    ],
    'portal.get_registry_record': [
        'IRegistry',
    ],
    'portal.set_registry_record': [
        'IRegistry',
    ],
    'env.adopt_user': [
        'setSecurityManager',
        'getSecurityManager',
        'newSecurityManager',
    ],
    'env.adopt_roles': [
        'getSecurityManager',
    ],
    'env.debug_mode': [
        'DevelopmentMode',
    ],
    'env.test_mode': [
        None,
    ],
    'env.plone_version': [
        None,
    ],
    'env.zope_version': [
        None,
    ],
}
