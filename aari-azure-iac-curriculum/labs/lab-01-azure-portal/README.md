# Lab 01: Azure Portal Basics

## What Students Are Building

Students will manually create:

- one Resource Group
- one Storage Account

Then they will delete both.

## Why It Matters

Before using Infrastructure as Code, students should understand what Azure resources look like in the portal.

This lab gives them a visual model for:

- grouping resources
- naming resources
- setting tags
- cleaning up cloud infrastructure

## Cost Warning

Even simple Azure resources can cost money if left running. Delete everything at the end of this lab.

## Commands To Run

This is a portal-first lab, so there are no required terminal commands.

Optional login command:

```bash
az login
```

## Portal Steps

1. Sign in to the Azure portal.
2. Create a Resource Group in `eastus`.
3. Add these tags to the Resource Group:
   - `org: aari`
   - `managed_by: pulumi`
   - `environment: dev`
   - `lab: lab-01-azure-portal`
4. Create a Storage Account inside that Resource Group.
5. Add the same tags to the Storage Account.
6. Review the overview pages for both resources.
7. Delete the Storage Account.
8. Delete the Resource Group.

## What To Observe

- Resource Groups organize related resources
- tags help identify ownership and purpose
- the Storage Account name must be globally unique
- deleting the Resource Group is the fastest cleanup path

## How To Destroy Resources

Delete the Storage Account and then delete the Resource Group in the Azure portal.

## Common Mistakes

- forgetting to set the region to `eastus`
- forgetting tags
- choosing a Storage Account name that is already taken
- leaving the Resource Group undeleted after the lab
