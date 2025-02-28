# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.resourcemover import ResourceMoverServiceAPI

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resourcemover
# USAGE
    python unresolved_dependencies_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ResourceMoverServiceAPI(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.unresolved_dependencies.get(
        resource_group_name="rg1",
        move_collection_name="movecollection1",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/resourcemover/resource-manager/Microsoft.Migrate/stable/2021-08-01/examples/UnresolvedDependencies_Get.json
if __name__ == "__main__":
    main()
