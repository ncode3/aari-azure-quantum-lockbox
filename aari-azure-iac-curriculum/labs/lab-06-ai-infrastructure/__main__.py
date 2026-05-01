import hashlib

import pulumi
import pulumi_azure_native as azure_native

location = pulumi.Config("azure-native").get("location") or "eastus"
lab_name = "lab-06-ai-infrastructure"
stack = pulumi.get_stack()
project = pulumi.get_project()

suffix = hashlib.sha1(f"{project}-{stack}-{lab_name}".encode()).hexdigest()[:10]
storage_account_name = f"aari{suffix}"
registry_name = f"aari{suffix[:18]}"
workspace_name = f"aari-law-{suffix[:8]}"

tags = {
    "org": "aari",
    "managed_by": "pulumi",
    "environment": "dev",
    "lab": lab_name,
}

resource_group = azure_native.resources.ResourceGroup(
    f"aari-rg-{stack}",
    resource_group_name=f"aari-{stack}-rg-lab06",
    location=location,
    tags=tags,
)

storage_account = azure_native.storage.StorageAccount(
    "storageaccount",
    resource_group_name=resource_group.name,
    account_name=storage_account_name,
    location=resource_group.location,
    sku=azure_native.storage.SkuArgs(name=azure_native.storage.SkuName.STANDARD_LRS),
    kind=azure_native.storage.Kind.STORAGE_V2,
    tags=tags,
)

registry = azure_native.containerregistry.Registry(
    "containerregistry",
    resource_group_name=resource_group.name,
    registry_name=registry_name,
    location=resource_group.location,
    sku=azure_native.containerregistry.SkuArgs(name="Basic"),
    admin_user_enabled=False,
    tags=tags,
)

workspace = azure_native.operationalinsights.Workspace(
    "loganalytics",
    resource_group_name=resource_group.name,
    workspace_name=workspace_name,
    location=resource_group.location,
    sku=azure_native.operationalinsights.WorkspaceSkuArgs(name="PerGB2018"),
    retention_in_days=30,
    tags=tags,
)

pulumi.export("resource_group_name", resource_group.name)
pulumi.export("storage_account_name", storage_account.name)
pulumi.export("container_registry_name", registry.name)
pulumi.export("log_analytics_workspace_name", workspace.name)
