# Lab 04: Key Vault Security

## What Students Are Building

Students will define:

- one Resource Group
- one Key Vault

No secrets will be added in this lab.

## Why It Matters

Students need to understand a core rule of cloud engineering:

secrets do not belong in source code.

Key Vault exists to separate:

- application code
- infrastructure code
- secret storage

## Cost Warning

Key Vault is not usually expensive at small scale, but it still must be cleaned up after testing.

## Commands To Run

```bash
cd labs/lab-04-key-vault-security
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
az login
pulumi login
pulumi stack select dev
pulumi config set azure-native:location eastus
pulumi preview
```

## What To Observe

- the vault is created without hardcoded secrets
- the code uses Azure identity information instead of embedding credentials
- tags are applied to both resources
- the vault is configured as infrastructure, not as a secret dump inside code

## How To Destroy Resources

If students later deploy this lab, they should clean up with:

```bash
pulumi destroy
```

## Common Mistakes

- trying to store secrets directly in `__main__.py`
- confusing Key Vault creation with secret creation
- forgetting that production secrets should come from secure identity and policy workflows
