from ase.io import read
import numpy as np

frames = read('vasprun.xml', index=':')

with open('vaspxml.xyz', 'w') as f:
    for i, atoms in enumerate(frames):
        natoms = len(atoms)
        positions = atoms.get_positions()
        forces = atoms.get_forces()
        cell = atoms.get_cell()
        energy = atoms.get_potential_energy()

        lattice_flat = cell.array.reshape(-1)
        lattice_str = ' '.join(f'{x:.6f}' for x in lattice_flat)

        f.write(f"{natoms}\n")
        f.write(f'Lattice="{lattice_str}" Properties=species:S:1:pos:R:3:forces:R:3 energy={energy:.15f}\n')

        for symbol, pos, force in zip(atoms.get_chemical_symbols(), positions, forces):
            f.write(f"{symbol} {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f} "
                    f"{force[0]:.6f} {force[1]:.6f} {force[2]:.6f}\n")
