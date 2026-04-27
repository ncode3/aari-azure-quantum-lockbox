# Facilitator Checklist

## Before Students Arrive

- Open the repo: `/Users/atlanta_ai_robotics/aari-azure-quantum-lockbox`
- Confirm the local demo runs:
  - `python3 scripts/quantum_lockbox.py`
- Confirm the cloud demo runs:
  - `python3 scripts/submit_to_azure.py`
- Confirm `AZURE_QUANTUM_RESOURCE_ID` is set in the shell
- Confirm the student handout is ready:
  - `docs/STUDENT_HANDOUT.md`
- Confirm the roster sheet is ready:
  - `docs/student_roster_checkin.csv`

## Opening Script

Say:

“We created quantum random bits with Q#. Those bits become a key. That key encrypts and decrypts a message. Locally, it runs on the simulator. In Azure, it submits through Azure Quantum. Same concept, cloud-backed quantum workflow.”

## Live Session Flow

### 1. Introduce the goal

- Students will generate quantum random bits.
- Students will turn those bits into a key.
- Students will encrypt and decrypt a message.

### 2. Local demo first

Have students run:

```bash
python3 scripts/quantum_lockbox.py
```

Checkpoint:

- They see the original message.
- They see the quantum key.
- They see encrypted bytes.
- They see the decrypted message.

### 3. Show the code at a high level

- `src/QuantumLockbox.qs`
- `scripts/quantum_lockbox.py`

Keep it short:

- Q# makes the random bits.
- Python uses the bits as a key.

### 4. Cloud demo second

Have students run:

```bash
python3 scripts/submit_to_azure.py
```

Checkpoint:

- Students understand this is the same workflow, but cloud-backed.

### 5. End with challenge

- move from 8-bit to 16-bit
- run 100 times
- graph `0`s and `1`s
- discuss whether it looks random

## Troubleshooting

- If local demo fails, fix Python environment first.
- If cloud demo fails because `AZURE_QUANTUM_RESOURCE_ID` is unset, the repo is fine and the shell just needs the environment variable.
- If Azure is slow, do not let the cloud path block the workshop.

## After Session

- Mark local and cloud completion in the roster sheet.
- Give students the 48-hour challenge.
- Save any student notes in the `notes` column of the roster CSV.
