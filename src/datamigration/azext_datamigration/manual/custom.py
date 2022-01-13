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

import ctypes
import json
import os
import platform
import subprocess
import time
import urllib.request
from zipfile import ZipFile
from knack.util import CLIError


# -----------------------------------------------------------------------------------------------------------------
# Common helper function to validate if the commands are running on Windows.
# -----------------------------------------------------------------------------------------------------------------
def validate_os_env():

    if not platform.system().__contains__('Windows'):
        raise CLIError("This command cannot be run in non-windows environment. Please run this command in Windows environment")


# -----------------------------------------------------------------------------------------------------------------
# Assessment Command Implementation.
# -----------------------------------------------------------------------------------------------------------------
def datamigration_assessment(connection_string=None,
                             output_folder=None,
                             overwrite=False,
                             config_file_path=None):

    try:

        validate_os_env()

        defaultOutputFolder = get_default_output_folder()

        # Assigning base folder path
        baseFolder = os.path.join(defaultOutputFolder, "Downloads")
        exePath = os.path.join(baseFolder, "SqlAssessment.Console.csproj", "SqlAssessment.exe")

        # Creating base folder structure
        if not os.path.exists(baseFolder):
            os.makedirs(baseFolder)

        testPath = os.path.exists(exePath)

        # Downloading console app zip and extracting it
        if not testPath:
            zipSource = "https://sqlassess.blob.core.windows.net/app/SqlAssessment.zip"
            zipDestination = os.path.join(baseFolder, "SqlAssessment.zip")

            urllib.request.urlretrieve(zipSource, filename=zipDestination)
            with ZipFile(zipDestination, 'r') as zipFile:
                zipFile.extractall(path=baseFolder)

        if connection_string is not None:
            connection_string = ", ".join(f"\"{i}\"" for i in connection_string)
            cmd = f'{exePath} Assess --sqlConnectionStrings {connection_string} ' if output_folder is None else f'{exePath} Assess --sqlConnectionStrings {connection_string} --outputFolder "{output_folder}" '
            cmd += '--overwrite False' if overwrite is False else ''
            subprocess.call(cmd, shell=False)
        elif config_file_path is not None:
            validate_config_file_path(config_file_path)
            cmd = f'{exePath} --configFile "{config_file_path}"'
            subprocess.call(cmd, shell=False)
        else:
            raise CLIError('No valid parameter set used. Please provide any one of the these prameters: connection_string, config_file_path')

        # Printing log file path
        logFilePath = os.path.join(defaultOutputFolder, "Logs")
        print(f"Event and Error Logs Folder Path: {logFilePath}")

    except Exception as e:
        raise e


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to test whether the given cofig_file_path is valid and has valid action specified.
# -----------------------------------------------------------------------------------------------------------------
def validate_config_file_path(path):

    if not os.path.exists(path):
        raise CLIError(f'Invalid config file path: {path}. Please provide a valid config file path.')

    # JSON file
    with open(path, "r", encoding=None) as f:
        configJson = json.loads(f.read())
    try:
        if not configJson['action'].lower() == "assess":
            raise CLIError("The desired action in config file was invalid. Please use \"Assess\" for action property in config file")
    except KeyError as e:
        raise CLIError("Invalid schema of config file. Please ensure that this is a properly formatted config file.") from e


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to return the default output folder path depending on OS environment.
# -----------------------------------------------------------------------------------------------------------------
def get_default_output_folder():

    osPlatform = platform.system()

    if osPlatform.__contains__('Linux'):
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), ".config", "Microsoft", "SqlAssessment")
    elif osPlatform.__contains__('Darwin'):
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), "Library", "Application Support", "Microsoft", "SqlAssessment")
    else:
        defaultOutputPath = os.path.join(os.getenv('LOCALAPPDATA'), "Microsoft", "SqlAssessment")

    return defaultOutputPath


# -----------------------------------------------------------------------------------------------------------------
# Register Sql Migration Service on IR command Implementation.
# -----------------------------------------------------------------------------------------------------------------
def datamigration_register_ir(auth_key,
                              ir_path=None):

    validate_os_env()

    if not is_user_admin():
        raise CLIError("Failed: You do not have Administrator rights to run this command. Please re-run this command as an Administrator!")
    validate_input(auth_key)
    if ir_path is not None:
        if not os.path.exists(ir_path):
            raise CLIError(f"Invalid Integration Runtime MSI path : {ir_path}. Please provide a valid Integration Runtime MSI path")
        install_gateway(ir_path)

    register_ir(auth_key)


# -----------------------------------------------------------------------------------------------------------------
# Helper function to check whether the command is run as admin.
# -----------------------------------------------------------------------------------------------------------------
def is_user_admin():

    try:
        isAdmin = os.getuid() == 0
    except AttributeError:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return isAdmin


# -----------------------------------------------------------------------------------------------------------------
# Helper function to validate key input. More checks to be added here using regex.
# -----------------------------------------------------------------------------------------------------------------
def validate_input(key):
    if key == "":
        raise CLIError("Failed: IR Auth key is empty. Please provide a valid auth key.")


# -----------------------------------------------------------------------------------------------------------------
# Helper function to check whether SHIR is installed or not.
# -----------------------------------------------------------------------------------------------------------------
def check_whether_gateway_installed(name):

    import winreg
    # Connecting to key in registry
    accessRegistry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    # Get the path of Installed softwares
    accessKey = winreg.OpenKey(accessRegistry, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    for i in range(0, winreg.QueryInfoKey(accessKey)[0]):
        installedSoftware = winreg.EnumKey(accessKey, i)
        installedSoftwareKey = winreg.OpenKey(accessKey, installedSoftware)
        try:
            displayName = winreg.QueryValueEx(installedSoftwareKey, r"DisplayName")[0]
            if name in displayName:
                return True
        except FileNotFoundError:
            pass

    return False


# -----------------------------------------------------------------------------------------------------------------
# Helper function to install SHIR
# -----------------------------------------------------------------------------------------------------------------
def install_gateway(path):

    if check_whether_gateway_installed("Microsoft Integration Runtime"):
        print("Microsoft Integration Runtime is already installed")
        return

    print("Start Integration Runtime installation")

    installCmd = f'msiexec.exe /i "{path}" /quiet /passive'
    subprocess.call(installCmd, shell=False)
    time.sleep(30)

    print("Integration Runtime installation is complete")


# -----------------------------------------------------------------------------------------------------------------
# Helper function to register Sql Migration Service on IR
# -----------------------------------------------------------------------------------------------------------------
def register_ir(key):
    print(f"Start to register IR with key: {key}")

    cmdFilePath = get_cmd_file_path()

    directoryPath = os.path.dirname(cmdFilePath)
    parentDirPath = os.path.dirname(directoryPath)

    dmgCmdPath = os.path.join(directoryPath, "dmgcmd.exe")
    regIRScriptPath = os.path.join(parentDirPath, "PowerShellScript", "RegisterIntegrationRuntime.ps1")

    portCmd = f'{dmgCmdPath} -EnableRemoteAccess 8060'
    irCmd = f'powershell -command "& \'{regIRScriptPath}\' -gatewayKey {key}"'

    subprocess.call(portCmd, shell=False)
    subprocess.call(irCmd, shell=False)


# -----------------------------------------------------------------------------------------------------------------
# Helper function to get SHIR script path
# -----------------------------------------------------------------------------------------------------------------
def get_cmd_file_path():

    import winreg
    try:
        # Connecting to key in registry
        accessRegistry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        # Get the path of Integration Runtime
        accessKey = winreg.OpenKey(accessRegistry, r"SOFTWARE\Microsoft\DataTransfer\DataManagementGateway\ConfigurationManager")
        accessValue = winreg.QueryValueEx(accessKey, r"DiacmdPath")[0]

        return accessValue
    except FileNotFoundError as e:
        raise CLIError("Failed: No installed IR found. Please install Integration Runtime and re-run this command") from e
