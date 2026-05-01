import hashlib

import pulumi
import pulumi_azure_native as azure_native

location = pulumi.Config("azure-native").get("location") or "eastus"
lab_name = "lab-05-logging-monitoring"
stack = pulumi.get_stack()
project = pulumi.get_project()

suffix = hashlib.sha1(f"{project}-{stack}-{lab_name}".encode()).hexdigest()[:8]
workspace_name = f"aari-law-{suffix}"

tags = {
    "org": "aari",
    "managed_by": "pulumi",
    "environment": "dev",
    "lab": lab_name,
}

resource_group = azure_native.resources.ResourceGroup(
    f"aari-rg-{stack}",
    resource_group_name=f"aari-{stack}-rg-lab05",
    location=location,
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
pulumi.export("log_analytics_workspace_name", workspace.name)
