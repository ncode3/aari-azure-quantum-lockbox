# Student Handout

## Goal

Today you will use Q# to create quantum random bits, turn those bits into a key, and use that key to encrypt and decrypt a short message in Python.

The idea to remember:

`quantum randomness -> secret key -> encrypted message`

## What You Will Run

First run the local demo:

```bash
python3 scripts/quantum_lockbox.py
```

Then run the cloud version:

```bash
python3 scripts/submit_to_azure.py
```

## Setup

Open the repo folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade "qdk[azure]" ipykernel
python3 -m pip install -r requirements.txt
```

## What To Look For

When you run the local demo, you should see:

- `Original Message`
- `Quantum Key`
- `Encrypted Bytes`
- `Decrypted Message`

If the decrypted message matches the original message, your lockbox worked.

## What The Code Does

### In Q#

- `RandomBit()` creates one random bit from a qubit measurement.
- `RandomKey8()` creates 8 random bits.
- `RandomKey16()` is the extension challenge.

### In Python

- call the Q# operation
- collect the measured bits
- turn those bits into a number
- use that number as a key
- XOR-encrypt a message
- XOR-decrypt the message back

## Student Takeaway

Quantum computing is not just theory. It can produce real entropy for real security workflows.

## 48-Hour Challenge

1. Modify the lockbox from 8-bit to 16-bit.
2. Run it 100 times.
3. Graph the number of `0`s and `1`s.
4. Explain whether the output looks random.
