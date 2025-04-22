import numpy as np
from config import HBAR, MASS

def box_wavefunction(L, nx, ny, nz, x, y, z):
    norm = np.sqrt(8 / (L ** 3))
    return norm * np.sin(nx * np.pi * x / L) * np.sin(ny * np.pi * y / L) * np.sin(nz * np.pi * z / L)

def box_energy(L, nx, ny, nz):
    return (np.pi ** 2 * HBAR ** 2 / (2 * MASS * L ** 2)) * (nx ** 2 + ny ** 2 + nz ** 2)

def transition_probability(initial, final, V0, a, t):
    omega = np.abs(final['energy'] - initial['energy']) / HBAR
    overlap = np.sum(initial['wavefunction'] * final['wavefunction'])
    return (V0 ** 2 * overlap ** 2 * np.sin(omega * t / 2) ** 2) / (omega ** 2)
