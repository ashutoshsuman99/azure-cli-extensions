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

from knack.help_files import helps


helps['datamigration get-assessment'] = """
    type: command
    short-summary: Start assessment on SQL Server instance(s).
    examples:
      - name: Run SQL Assessment on given SQL Server using connection string.
        text: |-
               az datamigration get-assessment --connection-string "Data Source=LabServer.database.net;Initial Catalog=master;Integrated Security=False;User Id=User;Password=password" --output-folder "C:\\AssessmentOutput" --overwrite
      - name: Run SQL Assessment on given SQL Server using assessment config file.
        text: |-
               az datamigration get-assessment --config-file-path "C:\\Users\\user\\document\\config.json"
"""

helps['datamigration register-integration-runtime'] = """
    type: command
    short-summary: Register Database Migration Service on Integration Runtime
    examples:
      - name: Register Sql Migration Service on Self Hosted Integration Runtime.
        text: |-
               az datamigration register-integration-runtime --auth-key "IR@00000-0000000-000000-aaaaa-bbbb-cccc"
      - name: Install Integration Runtime and register a Sql Migration Service on it.
        text: |-
               az datamigration register-integration-runtime --auth-key "IR@00000-0000000-000000-aaaaa-bbbb-cccc" --ir-path "C:\\Users\\user\\Downloads\\IntegrationRuntime.msi"
"""

helps['datamigration to-sql-managed-instance create'] = """
    type: command
    short-summary: "Create a new database migration to a given SQL Managed Instance."
    parameters:
      - name: --source-sql-connection
        short-summary: "Source SQL Server connection details."
        long-summary: |
            Usage: --source-sql-connection data-source=XX authentication=XX user-name=XX password=XX \
encrypt-connection=XX trust-server-certificate=XX

            data-source: Data source.
            authentication: Authentication type.
            user-name: User name to connect to source SQL.
            password: Password to connect to source SQL.
            encrypt-connection: Whether to encrypt connection or not.
            trust-server-certificate: Whether to trust server certificate or not.
      - name: --offline-configuration
        short-summary: "Offline configuration."
        long-summary: |
            Usage: --offline-configuration offline=XX last-backup-name=XX

            offline: Offline migration
            last-backup-name: Last backup name for offline migration. This is optional for migrations from file share. \
If it is not provided, then the service will determine the last backup file name based on latest backup files present \
in file share.
      - name: --target-location
        short-summary: "Target location for copying backups."
        long-summary: |
            Usage: --target-location storage-account-resource-id=XX account-key=XX

            storage-account-resource-id: Resource Id of the storage account copying backups.
            account-key: Storage Account Key.
    examples:
      - name: Create or Update Database Migration resource with fileshare as source for backup files.
        text: |-
               az datamigration to-sql-managed-instance create --managed-instance-name "managedInstance1" \
--source-location '{\\"fileShare\\":{\\"path\\":\\"\\\\\\\\SharedBackup\\\\user\\",\\"password\\":\\"placeholder\\",\
\\"username\\":\\"Server\\\\name\\"}}' --target-location account-key="abcd" storage-account-resource-id="account.database.win\
dows.net" --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Micr\
osoft.DataMigration/sqlMigrationServices/testagent" --offline-configuration last-backup-name="last_backup_file_name" \
offline=true --scope "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql\
/managedInstances/instance" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication"\
 data-source="aaa" encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" \
--resource-group "testrg" --target-db-name "db1"
      - name: Create or Update Database Migration resource with Azure Blob storage as source for backup files.
        text: |-
               az datamigration to-sql-managed-instance create --managed-instance-name "managedInstance1" \
--source-location '{\\"AzureBlob\\":{\\"storageAccountResourceId\\":\\"/subscriptions/1111-2222-3333-4444/resourceGroups/RG/prooviders\
/Microsoft.Storage/storageAccounts/MyStorage\\",\\"accountKey\\":\\"======AccountKey====\\",\\"blobContainerName\\":\\"ContainerName\
-X\\"}}' --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Micr\
osoft.DataMigration/sqlMigrationServices/testagent" --offline-configuration last-backup-name="last_backup_file_name" \
offline=true --scope "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql\
/managedInstances/instance" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication"\
 data-source="aaa" encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" \
--resource-group "testrg" --target-db-name "db1"
"""

helps['datamigration to-sql-vm create'] = """
    type: command
    short-summary: "Create a new database migration to a given SQL VM."
    parameters:
      - name: --source-sql-connection
        short-summary: "Source SQL Server connection details."
        long-summary: |
            Usage: --source-sql-connection data-source=XX authentication=XX user-name=XX password=XX \
encrypt-connection=XX trust-server-certificate=XX

            data-source: Data source.
            authentication: Authentication type.
            user-name: User name to connect to source SQL.
            password: Password to connect to source SQL.
            encrypt-connection: Whether to encrypt connection or not.
            trust-server-certificate: Whether to trust server certificate or not.
      - name: --offline-configuration
        short-summary: "Offline configuration."
        long-summary: |
            Usage: --offline-configuration offline=XX last-backup-name=XX

            offline: Offline migration
            last-backup-name: Last backup name for offline migration. This is optional for migrations from file share. \
If it is not provided, then the service will determine the last backup file name based on latest backup files present \
in file share.
      - name: --target-location
        short-summary: "Target location for copying backups."
        long-summary: |
            Usage: --target-location storage-account-resource-id=XX account-key=XX

            storage-account-resource-id: Resource Id of the storage account copying backups.
            account-key: Storage Account Key.
    examples:
      - name: Create or Update Database Migration resource with fileshare as source for backup files.
        text: |-
               az datamigration to-sql-vm create --source-location '{\\"fileShare\\":{\\"path\\":\\"\\\\\\\\SharedBackup\
\\\\user\\",\\"password\\":\\"placeholder\\",\\"username\\":\\"Server\\\\name\\"}}' --target-location account-key="abcd" \
storage-account-resource-id="account.database.windows.net" --migration-service "/subscriptions/00000000-1111-2222-3333-\
444444444444/resourceGroups/testrg/providers/Microsoft.DataMigration/sqlMigrationServices/testagent" \
--offline-configuration last-backup-name="last_backup_file_name" offline=true --scope "/subscriptions/00000000-1111-222\
2-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/testvm" \
--source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication" data-source="aaa" \
encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" --resource-group "testrg" \
--sql-vm-name "testvm" --target-db-name "db1"
      - name: Create or Update Database Migration resource with Azure Blob storage as source for backup files.
        text: |-
               az datamigration to-sql-vm create --source-location '{\\"AzureBlob\\":{\\"storageAccountResourceId\\"\
:\\"/subscriptions/1111-2222-3333-4444/resourceGroups/RG/prooviders/Microsoft.Storage/storageAccounts/MyStorage\\",\
\\"accountKey\\":\\"======AccountKey====\\",\\"blobContainerName\\":\\"ContainerName-X\\"}}' --migration-service "/subscriptions\
/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.DataMigration/sqlMigrationServices/testagent" \
--offline-configuration last-backup-name="last_backup_file_name" offline=true --scope "/subscriptions/00000000-1111-222\
2-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/testvm" \
--source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication" data-source="aaa" \
encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" --resource-group "testrg" \
--sql-vm-name "testvm" --target-db-name "db1"
"""
