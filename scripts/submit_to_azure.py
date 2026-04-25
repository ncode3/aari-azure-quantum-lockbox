import os
from pathlib import Path

import qsharp
from qdk.azure import Workspace


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    resource_id = os.environ["AZURE_QUANTUM_RESOURCE_ID"]
    target_name = os.getenv("AZURE_QUANTUM_TARGET", "rigetti.sim.qvm")
    shots = int(os.getenv("AZURE_QUANTUM_SHOTS", "10"))

    qsharp.init(
        project_root=str(PROJECT_ROOT),
        target_profile=qsharp.TargetProfile.Base,
    )

    program = qsharp.compile("QuantumLockbox.RandomKey8()")
    workspace = Workspace(resource_id=resource_id)
    target = workspace.get_targets(target_name)

    print(f"Submitting QuantumLockbox.RandomKey8() to {target_name}...")
    job = target.submit(program, "quantum-lockbox-random-key", shots=shots)
    results = job.get_results()

    print("Azure Quantum results:")
    print(results)


if __name__ == "__main__":
    main()
