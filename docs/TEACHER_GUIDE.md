# Teacher / Facilitator Guide

## Workshop Goal

Students run a tiny Q# program that uses quantum measurement to create random bits, then use those bits as a secret key to encrypt and decrypt a message in Python.

Keep the framing simple:

`We used quantum physics to create a secret key.`

## Audience

- High school students
- Early college students
- First-time quantum learners

## Time

30 minutes

## What Students Need

- VS Code or a browser-based coding environment
- Python 3.10+
- Internet access for package install
- Optional Azure subscription and Azure Quantum workspace

## Facilitator Prep

Before class, confirm:

1. `python -m pip install --upgrade "qdk[azure]" ipykernel` works on your machines.
2. `az extension add --upgrade -n quantum` works on your machines if doing the cloud section.
3. The local script runs:

```bash
python scripts/quantum_lockbox.py
```

4. If using Azure Quantum live, set up one working resource ID and one simulator target in advance.

## 30-Minute Run Of Show

### 0:00-0:03 | Hook

Say:

- Today we are going to make a secret key using quantum physics.
- Then we will use that key to lock and unlock a message.

Show the repo tree quickly and point to:

- `src/QuantumLockbox.qs`
- `scripts/quantum_lockbox.py`
- `notebooks/quantum_lockbox.ipynb`

### 0:03-0:08 | Local Setup

Students run:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade "qdk[azure]" ipykernel
python -m pip install -r requirements.txt
```

Checkpoint:

- Everyone has an activated environment.
- Package install finishes without errors.

### 0:08-0:13 | Show The Q# Random Bit

Open `src/QuantumLockbox.qs`.

Explain only this:

1. `H(q)` puts the qubit into a quantum superposition.
2. `M(q)` measures it and gives a random classical result.
3. `Reset(q)` cleans up the qubit.

Avoid going deep into amplitudes or linear algebra.

### 0:13-0:18 | Run The Lockbox Demo

Students run:

```bash
python scripts/quantum_lockbox.py
```

Ask them to identify:

- the 8 random bits
- the integer key
- the encrypted output
- the decrypted message

Checkpoint:

- Students can explain that the same key encrypts and decrypts the message.

### 0:18-0:23 | Notebook Walkthrough

Open `notebooks/quantum_lockbox.ipynb`.

Use the notebook if students need a slower, cell-by-cell version.

Suggested talking points:

- Q# generates the bits.
- Python turns bits into a byte.
- XOR is a simple way to show locking and unlocking.

### 0:23-0:27 | Optional Azure Quantum Step

If time and credentials allow:

1. Run `az login`
2. Set the workspace with Azure CLI
3. Export `AZURE_QUANTUM_RESOURCE_ID`
4. Run:

```bash
python scripts/submit_to_azure.py
```

Use a simulator target first.

If there is queue time, explain that cloud quantum systems can take longer than the local simulator.

### 0:27-0:30 | Challenge + Wrap-Up

Offer one challenge:

- Change the message
- Use the 16-bit key
- Run the program several times and compare keys

Wrap with:

- Q# made the random bits.
- Python used those bits as a key.
- That is the core idea behind quantum-generated secrets.

Suggested closing slide footer:

**Student Takeaway:**
*Quantum computing is not just theory. It can produce real entropy for real security workflows.*

## Common Troubleshooting

### `ModuleNotFoundError: No module named 'qsharp'`

Fix:

```bash
python -m pip install --upgrade "qdk[azure]" ipykernel
```

### Notebook kernel is wrong

Have students select the environment kernel in VS Code or rerun:

```bash
python -m ipykernel install --user --name quantum-lockbox --display-name "Python (Quantum Lockbox)"
```

### Azure CLI does not know `quantum`

Fix:

```bash
az extension add --upgrade -n quantum
```

### Azure submission fails because no workspace is configured

Check:

- `az login`
- `az account set --subscription ...`
- `AZURE_QUANTUM_RESOURCE_ID` is set correctly

Fallback note:
The Azure Quantum CLI extension is optional for this workshop. If `az quantum` fails to install or run, do not block the workshop. The preferred path is Python/QDK direct submission using:

```bash
export AZURE_QUANTUM_RESOURCE_ID="/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Quantum/Workspaces/<WORKSPACE_NAME>"
python3 scripts/submit_to_azure.py
```

Troubleshooting note:
If submission fails because `AZURE_QUANTUM_RESOURCE_ID` is unset, the repo is working. The Azure workspace just has not been configured in the shell yet.

### Students get a key of `0`

That is rare but valid. If the demo feels boring, rerun the script once.

## Facilitation Tips

- Keep the energy on the story, not the math.
- Say “random quantum key” more often than “superposition.”
- Let students edit the message early so the demo feels personal.
- If cloud submission is slow, do not let it block the workshop goal.

## Success Criteria

Students can say all three:

1. A qubit measurement can produce a random bit.
2. Eight random bits can become a secret key.
3. The same key can lock and unlock a message.
