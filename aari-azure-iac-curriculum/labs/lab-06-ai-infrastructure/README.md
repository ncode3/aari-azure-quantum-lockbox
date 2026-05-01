# Lab 06: AI Infrastructure Starter Stack

## What Students Are Building

Students will define:

- one Resource Group
- one Azure Container Registry
- one Storage Account
- one Log Analytics Workspace

## Why It Matters

This lab shows how infrastructure supports AI model deployment.

Students will see how these resources map to real workflows:

- Storage Account for datasets and model artifacts
- Container Registry for model-serving images
- Log Analytics for observability
- Resource Group for organization and cleanup

## Cost Warning

This lab can cost more than the earlier labs because it combines several services. Use `pulumi preview` first and destroy resources after testing.

## Commands To Run

```bash
cd labs/lab-06-ai-infrastructure
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

- the stack is larger than earlier labs
- Azure Container Registry supports containerized AI workloads
- storage supports data and artifacts
- logging supports operations and troubleshooting

## How To Destroy Resources

If students later deploy this lab, they should clean up with:

```bash
pulumi destroy
```

## Common Mistakes

- forgetting that registry names must be globally unique
- treating observability as optional
- forgetting that AI infrastructure includes both compute-adjacent and storage-adjacent services
