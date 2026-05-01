# Lab 02: First Pulumi Resource Group

## What Students Are Building

Students will use Pulumi Python to define one Azure Resource Group.

## Why It Matters

This is the simplest possible Infrastructure-as-Code example:

- one file
- one Azure resource
- one safe preview flow

It teaches the basic Pulumi cycle:

- write code
- configure a stack
- preview changes
- understand what will happen before deployment

## Cost Warning

A Resource Group by itself has little or no direct cost, but students should still follow cleanup discipline.

## Commands To Run

```bash
cd labs/lab-02-first-pulumi-resource-group
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

- Pulumi reads `Pulumi.yaml` and `__main__.py`
- the preview shows one Resource Group to create
- tags appear in the preview
- the stack configuration sets the default region to `eastus`

## How To Destroy Resources

If students later deploy this lab, they should clean up with:

```bash
pulumi destroy
```

## Common Mistakes

- running commands outside the lab folder
- forgetting to activate the Python environment
- forgetting `az login`
- forgetting `pulumi login`
- editing tags incorrectly
