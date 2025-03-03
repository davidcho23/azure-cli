# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from ._client_factory import cf_container_groups, cf_container, cf_container_group_profiles, cf_container_group_profile
from ._format import (transform_container_group_list, transform_container_group,
                      transform_container_group_profile_list, transform_container_group_profile)


container_group_sdk = CliCommandType(
    operations_tmpl='azure.mgmt.containerinstance.operations#ContainerGroupsOperations.{}',
    client_factory=cf_container_groups
)


def load_command_table(self, _):
    with self.command_group('container', client_factory=cf_container_groups) as g:
        g.custom_command('list', 'list_containers', table_transformer=transform_container_group_list)
        g.custom_command('create', 'create_container', supports_no_wait=True,
                         table_transformer=transform_container_group)
        g.custom_show_command('show', 'get_container', table_transformer=transform_container_group)
        g.custom_command('delete', 'delete_container', confirmation=True)
        g.custom_command('logs', 'container_logs', client_factory=cf_container)
        g.custom_command('exec', 'container_exec')
        g.custom_command('export', 'container_export')
        g.custom_command('attach', 'attach_to_container')

    with self.command_group('container', container_group_sdk) as g:
        g.command('restart', 'begin_restart', supports_no_wait=True)
        g.command('stop', 'stop')
        g.command('start', 'begin_start', supports_no_wait=True)

    with self.command_group('container container-group-profile',
                            client_factory=cf_container_group_profiles) as g:
        g.custom_command('list', 'list_container_group_profiles',
                         table_transformer=transform_container_group_profile_list)
        g.custom_command('create', 'create_container_group_profile',
                         supports_no_wait=True, table_transformer=transform_container_group_profile)
        g.custom_show_command('show', 'get_container_group_profile',
                              table_transformer=transform_container_group_profile)
        g.custom_command('delete', 'delete_container_group_profile', confirmation=True)

    with self.command_group('container container-group-profile', client_factory=cf_container_group_profile) as g:
        g.custom_command('list-revisions', 'list_container_group_profile_revisions',
                         table_transformer=transform_container_group_profile_list)
        g.custom_show_command('show-revision', 'get_container_group_profile_revision',
                              table_transformer=transform_container_group_profile)
