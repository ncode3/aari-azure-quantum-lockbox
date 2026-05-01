# AARI Azure Infrastructure-as-Code Curriculum

This repo teaches Azure infrastructure from scratch using Pulumi and Python.

The goal is to help students understand how cloud infrastructure supports AI systems, robotics platforms, storage pipelines, observability, and deployment workflows.

## Course Objective

By the end of this curriculum, students should be able to:

- explain what Infrastructure as Code means
- use Pulumi with Python to describe Azure resources
- preview changes safely before deployment
- understand how tagging, cleanup, and cost control work
- connect infrastructure design to AI and robotics workloads

## Audience

- college students learning cloud computing
- students learning AI infrastructure
- students learning DevOps
- students learning robotics infrastructure

## Prerequisites

- basic Python familiarity
- terminal familiarity
- an Azure account with permission to create resources
- Azure CLI installed
- Pulumi CLI installed

## Setup Instructions

1. Install Azure CLI.
2. Install Pulumi CLI.
3. Log in to Azure:

```bash
az login
```

4. Log in to Pulumi:

```bash
pulumi login
```

5. For any Pulumi lab, create and activate a Python environment inside the lab directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

6. Preview changes safely:

```bash
pulumi preview
```

This curriculum does not require `pulumi up` as part of the teaching flow.

## Weekly Schedule

- Week 1: Lab 01 and Lab 02
- Week 2: Lab 03
- Week 3: Lab 04
- Week 4: Lab 05
- Week 5: Lab 06
- Week 6: Final project planning and review

## Student Rules

- do not hardcode secrets
- use `eastus` as the default region
- read the cost warning before every lab
- use `pulumi preview` before any deployment
- destroy resources after testing
- keep tags on every resource

## Cost-Control Rules

- do not leave resources running after a lab
- use the smallest SKU in beginner labs
- avoid premium services unless instructed
- clean up the whole stack when done
- if you are unsure about cost, stop and ask before deploying

Read:

- [`instructor/cost-control.md`](instructor/cost-control.md)

## Labs

- [`labs/lab-01-azure-portal/README.md`](labs/lab-01-azure-portal/README.md)
- [`labs/lab-02-first-pulumi-resource-group/README.md`](labs/lab-02-first-pulumi-resource-group/README.md)
- [`labs/lab-03-storage-pipeline/README.md`](labs/lab-03-storage-pipeline/README.md)
- [`labs/lab-04-key-vault-security/README.md`](labs/lab-04-key-vault-security/README.md)
- [`labs/lab-05-logging-monitoring/README.md`](labs/lab-05-logging-monitoring/README.md)
- [`labs/lab-06-ai-infrastructure/README.md`](labs/lab-06-ai-infrastructure/README.md)

## Final Project Idea

Build an AI robotics infrastructure starter stack in Azure using Pulumi Python.

Suggested components:

- Resource Group
- Storage Account for datasets and artifacts
- Azure Container Registry for model images
- Log Analytics Workspace for observability
- Key Vault for secret handling design

Students should explain:

- what each resource does
- why it belongs in the stack
- what the cost risks are
- how they would clean it up
