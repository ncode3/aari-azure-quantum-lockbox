from pathlib import Path

import qsharp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MESSAGE = "MOREHOUSE"


def result_to_bit(result) -> int:
    return 1 if result == qsharp.Result.One else 0


def bits_to_int(bits: list[int]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def xor_with_key(data: bytes, key: int) -> bytes:
    return bytes(byte ^ key for byte in data)


def main() -> None:
    qsharp.init(project_root=str(PROJECT_ROOT))

    raw_results = qsharp.eval("QuantumLockbox.RandomKey8()")
    bits = [result_to_bit(result) for result in raw_results]
    key = bits_to_int(bits)
    key_binary = "".join(str(bit) for bit in bits)

    plaintext = MESSAGE.encode("utf-8")
    ciphertext = xor_with_key(plaintext, key)
    recovered = xor_with_key(ciphertext, key).decode("utf-8")

    print(f"Original Message: {MESSAGE}")
    print(f"Quantum Key: {key_binary}")
    print(f"Encrypted Bytes: {ciphertext.hex(' ')}")
    print(f"Decrypted Message: {recovered}")


if __name__ == "__main__":
    main()
