# Lab 05: Logging and Monitoring

## What Students Are Building

Students will define:

- one Resource Group
- one Log Analytics Workspace

## Why It Matters

Observability helps teams answer:

- what happened
- when it happened
- where it happened
- whether systems are healthy

This lab introduces the idea that infrastructure is not complete without monitoring.

## Cost Warning

Monitoring systems can become expensive if they collect too much data. Students should destroy resources after testing and use small starter configurations.

## Commands To Run

```bash
cd labs/lab-05-logging-monitoring
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

- one workspace is planned
- observability is represented as infrastructure
- retention settings affect both value and cost

## How To Destroy Resources

If students later deploy this lab, they should clean up with:

```bash
pulumi destroy
```

## Common Mistakes

- thinking logging is optional
- forgetting that retention settings affect cost
- deploying monitoring too late in a project lifecycle
