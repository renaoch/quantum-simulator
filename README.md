# 3D Quantum Box Simulator

This project is a graphical user interface (GUI) based simulation of a quantum particle in a 3D box using the Tkinter library in Python. The simulator allows users to visualize quantum wavefunctions, energy levels, transition probabilities, and the effects of perturbations in the system. 

## Features
- Visualize wavefunctions in a 3D box with isosurfaces.
- View energy levels and transition probabilities between quantum states.
- Adjust simulation parameters such as box size, quantum numbers, and potential perturbations.
- Interactive sliders for real-time control over simulation parameters.

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/renaoch/quantum-simulator.git
    cd quantum-box-simulator
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```

## Usage

- Use the input fields to adjust the simulation parameters such as the size of the quantum box, quantum numbers, and perturbation strengths.
- After setting the parameters, click the "Run Simulation" button to generate the visualization.
- Use the sliders to interactively adjust the parameters and observe how the system evolves.

### Input Parameters
- **Box size (L):** The size of the 3D box in which the particle is confined.
- **Max quantum number:** The maximum quantum number for the simulation.
- **Initial nx, ny, nz:** The initial quantum numbers for the wavefunction.
- **Perturbation strength:** The strength of the perturbation applied to the system.
- **Perturbation x, y, z position:** The position of the perturbation in the 3D box.
- **Max time:** The maximum time for the simulation.

### Controls
- **Run Simulation:** Starts the simulation and generates the visualizations.
- **Interactive Sliders:** Adjust quantum numbers, time, and perturbation strength in real-time.

## Libraries Used

- **NumPy:** For numerical operations, especially handling arrays and mathematical functions.
- **Matplotlib:** For plotting the wavefunctions, energy levels, and transition probabilities.
- **SciPy:** For the Hermite polynomial evaluation used in the simulation.
- **Scikit-Image:** For isosurface extraction and 3D rendering.
- **Tkinter:** For the graphical user interface (GUI).
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the open-source community for their excellent libraries.
