# aari-azure-quantum-lockbox

Students use Q# to generate a quantum random key, then use Python to lock and unlock a short secret message.

The demo is simple on purpose:

`quantum physics -> random bits -> secret key -> encrypted message`

**Student Takeaway:**
*Quantum computing is not just theory. It can produce real entropy for real security workflows.*

## What Students Build

- A single-qubit random bit generator in Q#.
- An 8-bit quantum key generator in Q#.
- A Python workflow that turns those bits into a key.
- A tiny XOR lockbox that encrypts and decrypts a message.
- An optional Azure Quantum submission using `qdk[azure]`.

## Repo Layout

```text
aari-azure-quantum-lockbox/
├── .devcontainer/
├── docs/
│   └── TEACHER_GUIDE.md
├── notebooks/
│   └── quantum_lockbox.ipynb
├── scripts/
│   ├── quantum_lockbox.py
│   └── submit_to_azure.py
├── src/
│   └── QuantumLockbox.qs
├── qsharp.json
├── README.md
└── requirements.txt
```

## 5-Minute Quickstart

1. Create and activate a Python environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the workshop tools.

```bash
python -m pip install --upgrade "qdk[azure]" ipykernel
python -m pip install -r requirements.txt
```

3. Run the local demo.

```bash
python scripts/quantum_lockbox.py
```

4. Open the notebook if you want the step-by-step version.

```bash
jupyter notebook notebooks/quantum_lockbox.ipynb
```

## Setup

### Python Install

This workshop is designed for Python 3.10+.

Install the main dependencies with:

```bash
python -m pip install --upgrade "qdk[azure]" ipykernel
```

Then install the workshop extras:

```bash
python -m pip install -r requirements.txt
```

### Azure CLI Extension

If you want the optional Azure Quantum part, install the Azure Quantum CLI extension:

```bash
az extension add --upgrade -n quantum
```

## Azure Login Steps

1. Log in:

```bash
az login
```

2. Select your subscription:

```bash
az account set --subscription <SUBSCRIPTION_ID_OR_NAME>
```

3. Point Azure CLI at your quantum workspace:

```bash
az quantum workspace set \
  --resource-group <RESOURCE_GROUP> \
  --workspace-name <WORKSPACE_NAME> \
  --location <LOCATION>
```

The Azure Quantum docs note that `--location` is deprecated and scheduled for removal in May 2026, but it is still accepted today in the CLI workflow.

## How To Set `AZURE_QUANTUM_RESOURCE_ID`

You need your Azure Quantum workspace resource ID for the Python submission helper.

### Option 1: Copy it from the Azure portal

Open your Azure Quantum workspace and copy the **Resource ID** from the **Overview** page.

### Option 2: Read it from Azure CLI

```bash
az quantum workspace show \
  --resource-group <RESOURCE_GROUP> \
  --workspace-name <WORKSPACE_NAME> \
  --query id -o tsv
```

### Set the environment variable

```bash
export AZURE_QUANTUM_RESOURCE_ID="/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Quantum/Workspaces/<WORKSPACE_NAME>"
```

Optional target override:

```bash
export AZURE_QUANTUM_TARGET="rigetti.sim.qvm"
```

Optional shot count:

```bash
export AZURE_QUANTUM_SHOTS="10"
```

## How To Run Locally

### Fastest path

```bash
python scripts/quantum_lockbox.py
```

You should see:

- 8 quantum-generated bits
- the integer key
- the original message
- the encrypted bytes
- the decrypted message

### Notebook path

Open:

`notebooks/quantum_lockbox.ipynb`

The notebook walks students through the same flow one step at a time.

## How The Local Demo Works

1. Q# puts a qubit into superposition with `H`.
2. Measurement turns that into a random classical bit.
3. The program does that 8 times.
4. Python converts those 8 bits into one byte.
5. That byte is used as a secret XOR key.
6. The same key decrypts the message back to plain text.

The story students should remember is:

`We used quantum physics to create a secret key.`

## How To Submit To Azure Quantum

This repo includes an optional helper:

```bash
python scripts/submit_to_azure.py
```

The script does three things:

1. Loads the Q# project with `qsharp.init(project_root=..., target_profile=qsharp.TargetProfile.Base)`.
2. Compiles `QuantumLockbox.RandomKey8()` for Azure submission.
3. Connects to your workspace with `from qdk.azure import Workspace` and submits to the target in `AZURE_QUANTUM_TARGET`.

### Recommended first target

Use a simulator first before trying hardware. For example:

```bash
export AZURE_QUANTUM_TARGET="rigetti.sim.qvm"
python scripts/submit_to_azure.py
```

### Optional hardware step

If your workspace has access to hardware targets, set `AZURE_QUANTUM_TARGET` to a hardware target name and submit again.

Example:

```bash
export AZURE_QUANTUM_TARGET="<YOUR_HARDWARE_TARGET>"
python scripts/submit_to_azure.py
```

### What to expect

- Simulators usually return faster.
- Hardware jobs may queue.
- Azure results are returned as job output, not as the local Python XOR demo.

Do not submit repeated Azure Quantum jobs without instructor approval. Local simulator is free. Hardware/provider jobs may consume Azure credits.

Fallback note:
The Azure Quantum CLI extension is optional for this workshop. If `az quantum` fails to install or run, do not block the workshop. The preferred path is Python/QDK direct submission using:

```bash
export AZURE_QUANTUM_RESOURCE_ID="/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Quantum/Workspaces/<WORKSPACE_NAME>"
python3 scripts/submit_to_azure.py
```

Troubleshooting note:
If submission fails because `AZURE_QUANTUM_RESOURCE_ID` is unset, the repo is working. The Azure workspace just has not been configured in the shell yet.

The encryption demo is intentionally local so students can focus on the secret-key story without waiting on cloud jobs.

## Student Challenge

Try one or more of these:

1. Replace the message with your own secret sentence.
2. Upgrade the demo from an 8-bit key to the 16-bit challenge key.
3. Run the generator several times and compare the keys.
4. Count how many `0`s and `1`s appear over many runs.
5. Submit the 8-bit generator to Azure Quantum and compare the cloud output with the local simulator.

### 16-bit extension challenge

The Q# file already includes `RandomKey16()`.

Challenge students to:

- collect 16 bits instead of 8
- build a bigger integer key
- adapt the XOR helper to use two key bytes instead of one

## Teacher / Facilitator Guide

Use:

[`docs/TEACHER_GUIDE.md`](docs/TEACHER_GUIDE.md)

It includes a 30-minute run of show, pacing, checkpoints, and common troubleshooting notes.

## Cleanup Instructions

### Local cleanup

Deactivate the environment:

```bash
deactivate
```

Remove the virtual environment if you want:

```bash
rm -rf .venv
```

Unset workshop environment variables:

```bash
unset AZURE_QUANTUM_RESOURCE_ID
unset AZURE_QUANTUM_TARGET
unset AZURE_QUANTUM_SHOTS
```

### Azure cleanup

If you created a workspace only for this workshop, remove it from the Azure portal or delete its resource group when you are done.

Optional logout:

```bash
az logout
```

## Official References

This repo follows the current Microsoft QDK / Azure Quantum project pattern:

- Q# projects use `qsharp.json` plus a `src/` folder.
- Python and notebooks load the project with `qsharp.init(project_root=...)`.
- Azure workspace connections use `from qdk.azure import Workspace`.

Sources:

- Microsoft Learn: https://learn.microsoft.com/en-us/azure/quantum/how-to-work-with-qsharp-projects
- Microsoft Learn: https://learn.microsoft.com/en-us/azure/quantum/how-to-connect-workspace
- Microsoft Learn: https://learn.microsoft.com/en-us/azure/quantum/quickstart-microsoft-provider-format
- QDK wiki: https://github.com/microsoft/qsharp/wiki/Working-with-Jupyter-Notebooks
