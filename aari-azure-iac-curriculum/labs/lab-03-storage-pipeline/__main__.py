import hashlib

import pulumi
import pulumi_azure_native as azure_native

location = pulumi.Config("azure-native").get("location") or "eastus"
lab_name = "lab-03-storage-pipeline"
stack = pulumi.get_stack()
project = pulumi.get_project()

suffix = hashlib.sha1(f"{project}-{stack}-{lab_name}".encode()).hexdigest()[:10]
storage_account_name = f"aari{suffix}"

tags = {
    "org": "aari",
    "managed_by": "pulumi",
    "environment": "dev",
    "lab": lab_name,
}

resource_group = azure_native.resources.ResourceGroup(
    f"aari-rg-{stack}",
    resource_group_name=f"aari-{stack}-rg-lab03",
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

container_names = ["raw-data", "processed-data", "model-artifacts"]
containers = []
for container_name in container_names:
    containers.append(
        azure_native.storage.BlobContainer(
            container_name,
            resource_group_name=resource_group.name,
            account_name=storage_account.name,
            container_name=container_name,
            public_access=azure_native.storage.PublicAccess.NONE,
        )
    )

pulumi.export("resource_group_name", resource_group.name)
pulumi.export("storage_account_name", storage_account.name)
pulumi.export("container_names", [container.name for container in containers])
