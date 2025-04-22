import tkinter as tk
from tkinter import ttk

def create_input_panel(root, default_params, run_callback):
    frame = ttk.LabelFrame(root, text='Simulation Parameters')
    entries = {}

    for i, (key, val) in enumerate(default_params.items()):
        label = ttk.Label(frame, text=key)
        label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
        entry = ttk.Entry(frame)
        entry.insert(0, str(val))
        entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
        entries[key] = entry

    run_button = ttk.Button(frame, text='Run Simulation', command=run_callback)
    run_button.grid(row=len(default_params), columnspan=2, pady=10)


    frame.pack(side='left', fill='y', padx=10, pady=10)
    return entries
