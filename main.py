import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
import numpy as np

from config import DEFAULT_PARAMS
from ui.input_panel import create_input_panel
from ui.sliders import create_sliders
from ui.visualization import setup_figure
from simulator.core import box_wavefunction, box_energy, transition_probability


class QuantumBoxSimulator:
    def __init__(self, root):
        self.root = root
        root.title('Quantum Box Simulator')

        self.entries = create_input_panel(root, DEFAULT_PARAMS, self.run_simulation)
        self.fig, self.ax1, self.ax2, self.ax3, self.ax4, self.canvas = setup_figure(root)
        self.slider = create_sliders(root, DEFAULT_PARAMS['max_time'], self.update_visuals)

    def get_params(self):
        return {k: float(entry.get()) for k, entry in self.entries.items()}

    def run_simulation(self):
        params = self.get_params()
        L = params['box_size']
        nx, ny, nz = int(params['nx']), int(params['ny']), int(params['nz'])

        x = y = z = np.linspace(0, L, 100)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
        wavefunc = box_wavefunction(L, nx, ny, nz, X, Y, Z)
        energy = box_energy(L, nx, ny, nz)

        self.current_state = {
            'wavefunction': wavefunc,
            'energy': energy,
            'params': params,
            'X': X,
            'Y': Y,
            'Z': Z
        }

        self.update_visuals(None)

    def update_visuals(self, _):
        if not hasattr(self, 'current_state'):
            return

        wf = self.current_state['wavefunction']
        prob_density = np.abs(wf) ** 2

        self.ax1.clear()
        self.ax1.set_title('Wavefunction |Ψ(x,y,z)|')
        self.ax1.plot_surface(self.current_state['X'][:, :, 0], self.current_state['Y'][:, :, 0],
                              prob_density[:, :, 0], cmap='viridis')

        self.ax2.clear()
        self.ax2.set_title('Probability Density Slice (z=0)')
        self.ax2.imshow(prob_density[:, :, 0], extent=[0, 1, 0, 1], origin='lower', cmap='inferno')

        self.ax3.clear()
        self.ax3.set_title('1D Projection along x (z=0)')
        self.ax3.plot(prob_density[:, 50, 0])

        self.ax4.clear()
        self.ax4.set_title('3D View')
        self.ax4.plot_surface(self.current_state['X'][:, :, 0], self.current_state['Y'][:, :, 0],
                              prob_density[:, :, 0], cmap='coolwarm')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumBoxSimulator(root)
    root.mainloop()
