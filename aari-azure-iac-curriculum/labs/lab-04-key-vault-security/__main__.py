import hashlib

import pulumi
import pulumi_azure_native as azure_native

location = pulumi.Config("azure-native").get("location") or "eastus"
lab_name = "lab-04-key-vault-security"
stack = pulumi.get_stack()
project = pulumi.get_project()

client_config = azure_native.authorization.get_client_config_output()
suffix = hashlib.sha1(f"{project}-{stack}-{lab_name}".encode()).hexdigest()[:10]
vault_name = f"aari-kv-{suffix}"

tags = {
    "org": "aari",
    "managed_by": "pulumi",
    "environment": "dev",
    "lab": lab_name,
}

resource_group = azure_native.resources.ResourceGroup(
    f"aari-rg-{stack}",
    resource_group_name=f"aari-{stack}-rg-lab04",
    location=location,
    tags=tags,
)

vault = azure_native.keyvault.Vault(
    "keyvault",
    resource_group_name=resource_group.name,
    vault_name=vault_name,
    location=resource_group.location,
    properties=azure_native.keyvault.VaultPropertiesArgs(
        tenant_id=client_config.tenant_id,
        sku=azure_native.keyvault.SkuArgs(
            family=azure_native.keyvault.SkuFamily.A,
            name=azure_native.keyvault.SkuName.STANDARD,
        ),
        access_policies=[],
        enable_rbac_authorization=True,
        enable_soft_delete=True,
        public_network_access="Enabled",
    ),
    tags=tags,
)

pulumi.export("resource_group_name", resource_group.name)
pulumi.export("key_vault_name", vault.name)
