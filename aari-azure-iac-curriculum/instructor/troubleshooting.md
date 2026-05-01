# Troubleshooting

## Common Setup Issues

### Azure login problems

Fix:

```bash
az login
```

### Pulumi login problems

Fix:

```bash
pulumi login
```

### Python package install problems

Fix:

```bash
python3 -m pip install -r requirements.txt
```

### Wrong directory

Students often run commands from the repo root instead of the lab folder.

Fix:

```bash
cd labs/<lab-folder>
```

## Common Pulumi Issues

### Stack not selected

Fix:

```bash
pulumi stack select dev
```

### Region not configured

Fix:

```bash
pulumi config set azure-native:location eastus
```

### Preview fails due to Azure permissions

Cause:

- student is logged into the wrong account
- student does not have resource creation permissions

## Naming Issues

### Storage Account names must be globally unique

Students should understand that Azure has naming rules that are stricter than a local project folder.

### Registry names must be globally unique

This is expected behavior in Azure.

## Teaching Advice

- fix environment issues before debugging code
- keep students on `pulumi preview` first
- do not let one student’s permissions issue block the whole class
