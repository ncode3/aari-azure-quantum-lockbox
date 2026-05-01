# Lab 03: Storage Pipeline

## What Students Are Building

Students will define:

- one Resource Group
- one Storage Account
- three blob containers:
  - `raw-data`
  - `processed-data`
  - `model-artifacts`

## Why It Matters

AI systems and robotics pipelines depend on storage for:

- incoming data
- cleaned or transformed data
- saved models and artifacts

This lab shows how infrastructure supports a data pipeline.

## Cost Warning

Storage costs can grow when files accumulate. Use this lab carefully and destroy resources after testing.

## Commands To Run

```bash
cd labs/lab-03-storage-pipeline
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

- one Resource Group is planned
- one Storage Account is planned
- three separate blob containers are planned
- the container names reflect stages in a data workflow

## How To Destroy Resources

If students later deploy this lab, they should clean up with:

```bash
pulumi destroy
```

## Common Mistakes

- using invalid Storage Account naming rules
- forgetting that Storage Account names must be globally unique
- confusing containers with folders
- forgetting to destroy the stack after testing
