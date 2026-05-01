import pulumi
import pulumi_azure_native as azure_native

location = pulumi.Config("azure-native").get("location") or "eastus"
lab_name = "lab-02-first-pulumi-resource-group"
stack = pulumi.get_stack()

tags = {
    "org": "aari",
    "managed_by": "pulumi",
    "environment": "dev",
    "lab": lab_name,
}

resource_group = azure_native.resources.ResourceGroup(
    f"aari-rg-{stack}",
    resource_group_name=f"aari-{stack}-rg-lab02",
    location=location,
    tags=tags,
)

pulumi.export("resource_group_name", resource_group.name)
pulumi.export("location", resource_group.location)
