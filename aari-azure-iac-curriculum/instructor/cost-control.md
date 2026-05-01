# Cost Control

## Core Rule

Students must not leave resources running after a lab.

## Why This Matters

Cloud billing is real. Even beginner labs can produce charges if students forget cleanup.

## Teaching Guidance

- require `pulumi preview` before any deployment
- use small SKUs
- use one region: `eastus`
- avoid premium options in beginner labs
- review destroy steps before students start

## Resource Notes

- Resource Groups are organizational, but the resources inside them can cost money
- Storage Accounts can accumulate cost through data and transactions
- Key Vault can cost money through operations
- Log Analytics can cost money through ingestion and retention
- Container Registry can cost money depending on tier and usage

## Recommended Student Policy

- if you deploy it, you destroy it
- if you do not understand the cost, stop before deployment
- take screenshots of previews instead of deploying by default
