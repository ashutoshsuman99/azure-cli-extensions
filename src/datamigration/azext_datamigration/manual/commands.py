# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=line-too-long


def load_command_table(self, _):

    with self.command_group(
        'datamigration get-assessment'
    ) as g:
        g.custom_command('', 'datamigration_assessment')

    with self.command_group(
        'datamigration performance-data-collection'
    ) as g:
        g.custom_command('', 'datamigration_performance_data_collection')

    with self.command_group(
        'datamigration get-sku-recommendation'
    ) as g:
        g.custom_command('', 'datamigration_get_sku_recommendation')

    with self.command_group(
        'datamigration register-integration-runtime'
    ) as g:
        g.custom_command('', 'datamigration_register_ir')
