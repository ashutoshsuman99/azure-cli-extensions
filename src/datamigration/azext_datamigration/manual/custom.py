# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument
# pylint: disable=line-too-long

import os
import subprocess
from azure.cli.core.azclierror import MutuallyExclusiveArgumentError
from azure.cli.core.azclierror import RequiredArgumentMissingError
from azure.cli.core.azclierror import UnclassifiedUserFault
from azext_datamigration.manual import helper


# -----------------------------------------------------------------------------------------------------------------
# Assessment Command Implementation.
# -----------------------------------------------------------------------------------------------------------------
def datamigration_assessment(connection_string=None,
                             output_folder=None,
                             overwrite=False,
                             config_file_path=None):

    try:

        defaultOutputFolder, exePath = helper.console_app_setup()

        if connection_string is not None and config_file_path is not None:
            raise MutuallyExclusiveArgumentError("Both connection_string and config_file_path are mutually exclusive arguments. Please provide only one of these arguments.")

        if connection_string is not None:
            connection_string = " ".join(f"\"{i}\"" for i in connection_string)
            cmd = f'{exePath} Assess --sqlConnectionStrings {connection_string} ' if output_folder is None else f'{exePath} Assess --sqlConnectionStrings {connection_string} --outputFolder "{output_folder}" '
            cmd += '--overwrite False' if overwrite is False else ''
            subprocess.call(cmd, shell=False)
        elif config_file_path is not None:
            helper.validate_config_file_path(config_file_path, "assess")
            cmd = f'{exePath} --configFile "{config_file_path}"'
            subprocess.call(cmd, shell=False)
        else:
            raise RequiredArgumentMissingError('No valid parameter set used. Please provide any one of the these prameters: connection_string, config_file_path')

        # Printing log file path
        logFilePath = os.path.join(defaultOutputFolder, "Logs")
        print(f"Event and Error Logs Folder Path: {logFilePath}")

    except Exception as e:
        raise e


# -----------------------------------------------------------------------------------------------------------------
# Performance Data Collection Command Implementation.
# -----------------------------------------------------------------------------------------------------------------
def datamigration_performance_data_collection(connection_string=None,
                                              output_folder=None,
                                              perf_query_interval=None,
                                              static_query_interval=None,
                                              number_of_interation=None,
                                              config_file_path=None):

    try:

        defaultOutputFolder, exePath = helper.console_app_setup()

        if connection_string is not None and config_file_path is not None:
            raise MutuallyExclusiveArgumentError("Both sql_connection_string and config_file_path are mutually exclusive arguments. Please provide only one of these arguments.")

        if connection_string is not None:
            connection_string = " ".join(f"\"{i}\"" for i in connection_string)
            parameterList = {
                "--outputFolder": output_folder,
                "--perfQueryIntervalInSec": perf_query_interval,
                "--staticQueryIntervalInSec": static_query_interval,
                "--numberOfIterations": number_of_interation
            }
            cmd = f'{exePath} PerfDataCollection --sqlConnectionStrings {connection_string}'
            for param in parameterList:
                if parameterList[param] is not None:
                    cmd += f' {param} "{parameterList[param]}"'
            subprocess.call(cmd, shell=False)
        elif config_file_path is not None:
            helper.validate_config_file_path(config_file_path, "perfdatacollection")
            cmd = f'{exePath} --configFile "{config_file_path}"'
            subprocess.call(cmd, shell=False)
        else:
            raise RequiredArgumentMissingError('No valid parameter set used. Please provide any one of the these prameters: sql_connection_string, config_file_path')

        # Printing log file path
        logFilePath = os.path.join(defaultOutputFolder, "Logs")
        print(f"Event and Error Logs Folder Path: {logFilePath}")

    except Exception as e:
        raise e


# -----------------------------------------------------------------------------------------------------------------
#  Get SKU Recommendation Command Implementation.
# -----------------------------------------------------------------------------------------------------------------
def datamigration_get_sku_recommendation(output_folder=None,
                                         target_platform=None,
                                         target_sql_instance=None,
                                         target_percentile=None,
                                         scaling_factor=None,
                                         start_time=None,
                                         end_time=None,
                                         overwrite=False,
                                         display_result=False,
                                         elastic_strategy=False,
                                         database_allow_list=None,
                                         database_deny_list=None,
                                         config_file_path=None):

    try:
        defaultOutputFolder, exePath = helper.console_app_setup()

        if output_folder is not None and config_file_path is not None:
            raise MutuallyExclusiveArgumentError("Both output_folder and config_file_path are mutually exclusive arguments. Please provide only one of these arguments.")

        if config_file_path is not None:
            helper.validate_config_file_path(config_file_path, "getskurecommendation")
            cmd = f'{exePath} --configFile "{config_file_path}"'
            subprocess.call(cmd, shell=False)
        else:
            parameterList = {
                "--outputFolder": output_folder,
                "--targetPlatform": target_platform,
                "--targetSqlInstance": target_sql_instance,
                "--scalingFactor": scaling_factor,
                "--targetPercentile": target_percentile,
                "--startTime": start_time,
                "--endTime": end_time,
                "--overwrite": overwrite,
                "--displayResult": display_result,
                "--elasticStrategy": elastic_strategy,
                "--databaseAllowList": database_allow_list,
                "--databaseDenyList": database_deny_list
            }
            cmd = f'{exePath} GetSkuRecommendation'
            for param in parameterList:
                if parameterList[param] is not None and not param.__contains__("List"):
                    cmd += f' {param} "{parameterList[param]}"'
                elif param.__contains__("List") and parameterList[param] is not None:
                    parameterList[param] = " ".join(f"\"{i}\"" for i in parameterList[param])
                    cmd += f' {param} {parameterList[param]}'
            subprocess.call(cmd, shell=False)

        # Printing log file path
        logFilePath = os.path.join(defaultOutputFolder, "Logs")
        print(f"Event and Error Logs Folder Path: {logFilePath}")

    except Exception as e:
        raise e


# -----------------------------------------------------------------------------------------------------------------
# Register Sql Migration Service on IR command Implementation.
# -----------------------------------------------------------------------------------------------------------------
def datamigration_register_ir(auth_key,
                              ir_path=None):

    helper.validate_os_env()

    if not helper.is_user_admin():
        raise UnclassifiedUserFault("Failed: You do not have Administrator rights to run this command. Please re-run this command as an Administrator!")
    helper.validate_input(auth_key)
    if ir_path is not None:
        helper.install_gateway(ir_path)

    helper.register_ir(auth_key)
